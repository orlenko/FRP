from django.db import models
from django.db.utils import IntegrityError
from django.db.models.signals import post_save
from tinymce.models import HTMLField
import datetime
from django.contrib.auth.models import User, UserManager, Permission
import re

from django.utils.translation import ugettext as _
from django.contrib.localflavor.us.models import PhoneNumberField
from django.template.defaultfilters import slugify

# Local slugify-checking utilities
from utils import *

# Local geocoding precaching
from geopy.geocoders import Google
g = Google()
geocode = g.geocode

class Location(models.Model):
    """
    A basic optional location field for reverse geoadd usage
    """
    place = models.CharField(_("Place"), max_length=200)
    lat = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)

    def __unicode__(self):
        return self.place

class MemberUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,
            related_name="member")
    def __unicode__(self):
        return self.user.username

class Member(models.Model):
    """
    Members are imported from the membership Excel docs
    """
    users = models.ManyToManyField(MemberUser, null=True, blank=True,
        related_name="member")
    slug = models.SlugField(_("URL-friendly name"), max_length=80,
            unique=True, help_text=_("The slug must be a unique url identifier."))

    REGION_CHOICES = (
        ('other', _("Other")),
        ('fraservalley', _("Fraser Valley")),
        ('interior', _("Interior")),
        ('vancoast', _("Vancouver Coastal")),
        ('vanisle', _("Vancouver Island")),
        ('northern', _("Northern")),
        ('unknown', _("Unknown")),
    )

    ## Fields ordered by EXCEL ROWS
    # A
    memnum = models.IntegerField(_("FRP-BC Member Number"))
    # B, C
    renewal = models.DateField(_("Renewal Due Date"), blank=True, null=True)
    # D
    region = models.CharField(choices=REGION_CHOICES, max_length=12)
    # E
    agency = models.CharField(_("Member-Agency Name"), max_length=200)
    # F
    address = models.CharField(_("Street Address"), max_length=200)
    # G
    city = models.CharField(_("City/Town"), max_length=150)
    PROVINCE_CHOICES = (
        ("BC", _("British Columbia")),
        ("AB", _("Alberta")),
        ("SK", _("Saskatchewan")),
        ("MB", _("Manitoba")),
        ("ON", _("Ontario")),
        ("QC", _("Quebec")),
        ("PE", _("Prince Edward Island")),
        ("NL", _("Newfoundland and Labrador")),
        ("NS", _("Nova Scotia")),
        ("NB", _("New Brunswick")),
        ("YT", _("Yukon Territory")),
        ("NT", _("Northwest Territories")),
        ("NU", _("Nunavut")),
    )
    # H
    province = models.CharField(_("Province"), max_length=2, choices=PROVINCE_CHOICES)
    # I the standard is only 6, but whatever
    postal_code = models.CharField(_("Postal Code"), max_length=7)
    @property
    def geo_address(self):
        ret = "%(street)s, %(city)s, %(province)s %(postalcode)s" % {
                'street': self.address,
                'city': self.city,
                'province': self.province,
                'postalcode': self.postal_code,
            }
        return ret

    @property
    def full_address(self):
        ret = \
        """
            %(agency)s
            %(street)s
            %(city)s, %(province)s
            %(postalcode)s
        """ % {
                'agency': self.agency,
                'street': self.address,
                'city': self.city,
                'province': self.province,
                'postalcode': self.postal_code,
            }
        return ret
    # for internal use
    location = models.ForeignKey(Location, blank=True, null=True,
related_name="members")
    successful_location_save = models.BooleanField(_("Successful location\
    encoding"), help_text=_("If True, you will need to change your\
            address details and re-run 'encodegeo' (or wait for the database\
            to update itself"),
            default=False)

    # J
    agphone = PhoneNumberField(_("Agency Phone Number"), blank=True, null=True)
    # K
    agfax = PhoneNumberField(_("Agency Fax Number"), blank=True, null=True)

    # L 
    agdirect = models.CharField(_("Agency Executive Director / ECD Program Manager"),
            max_length=200, blank=True)
    # M
    dirphone = PhoneNumberField(_("Direct Phone Number"), blank=True, null=True)
    # N
    email = models.EmailField(_("Executive Director's Email"), blank=True)
    # O
    resname = models.CharField(_("FRP Name"), max_length=180)
    # P
    frpphone = PhoneNumberField(_("FRP Phone Number"), blank=True, null=True)
    # Q perhaps make the coordinator a foreign key?
    coordinator = models.CharField(_("FRP Coordinator / Manager"),
            max_length=200, blank=True)
    # R
    coemail = models.EmailField(_("Coordinator's Email"), blank=True)
    # S
    website = models.URLField(_("Website"), blank=True)
    # T
    joint = models.BooleanField(_("Joint Member"))
    # U
    prior = models.BooleanField(_("FRP Canada Member prior to Joint Offer"))
    # New Joint booleans
    # V
    newjoint2009 = models.BooleanField(_("New Joint Member (2009)"))
    # W
    newjoint2010 = models.BooleanField(_("New Joint Member (2010)"))
    # X
    newjoint2011 = models.BooleanField(_("New Joint Member (2011)"))
    # Y
    newbc2010 = models.BooleanField(_("New FRP-BC Member (2010)"))
    # Z
    frpbcfee = models.DecimalField(_("FRP-BC Fee"), max_digits=9,
            decimal_places=2, blank=True, null=True)
    # AA
    jointmemfee = models.DecimalField(_("Joint Member Fee"), max_digits=9,
            decimal_places=2, blank=True, null=True)
    # AB
    @property
    def totalfee(self):
        return self.frpbcfee + self.joinmemfee
    # AC -- ## TK! check if this should be auto
    updated = models.DateField(_("Updated"))
    # AD
    receipt = models.IntegerField(_("Reciept"), blank=True, null=True)
    # AE
    owecanada = models.DecimalField(_("Amount FRP-BC owes FRP Canada"),
            blank=True, max_digits=9, decimal_places=2, null=True)
    # AF
    paidfrpc = models.BooleanField(_("Paid (FRPC)"))
    # AG
    owefrpbc = models.DecimalField(_("Amount FRP Canada owes FRP-BC"),
            blank=True, max_digits=9, decimal_places=2, null=True)
    # AH
    paidfrpbc = models.BooleanField(_("Paid (FRPBC)"))
    # AI
    notes = models.TextField(_("Notes"), blank=True,
            help_text=_("Internal notes about the member."))
    # added for new site
    # important for management scripts:
    next_expiry = models.DateField(_("Next expiry date for unrenewed member."),
            help_text=_("The next expiry for an unrenewed member, set this at\
                a high amount for permanent members"), blank=True, null=True)
    site_updated = models.DateField(_("Last Updated (On Site)"), blank=True)
    description = HTMLField(_("Description (for directory)"), blank=True,
            help_text=_("Please describe your program and its goals."))
    is_active = models.BooleanField(_("Member is Active"), blank=True,
        help_text=_("True if the Member is active. This field is typically\
            automatically set by the system"), default=True)
    is_subscribed = models.BooleanField(_("Member recieves emails/notices"), blank=True,
        help_text=_("True if the Member is recieving emails. This field is typically\
            true, but may be set to off if a member is kept in the record for\
            other reasons."), default=True)
    rec_upcoming_notice = models.BooleanField(_("Recieved Upcoming Expiry Notice"), blank=True,
        help_text=_("True if the Member has recieved an expiry notice. This field is typically\
            automatically set by the system"), default=False)
    rec_expiry_notice = models.BooleanField(_("Member is Active"), blank=True,
        help_text=_("True if the Member has recieved an expiry notice. This field is typically\
            automatically set by the system"), default=False)

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")
        ordering = ('agency', 'site_updated',)

    def __unicode__(self):
        return self.agency

    @models.permalink
    def get_absolute_url(self):
        return ('member_view', [str(self.slug)],)

    def save(self, *args, **kwargs):
        slugstr = "%s %s" % (self.agency, self.region)
        unique_slugify(self, slugstr)
        self.updated = datetime.datetime.now()
        self.site_updated = datetime.datetime.now()
        super(Member, self).save(*args, **kwargs)

def encode_location(sender, **kwargs):
    """
        Encodes location of lat and long from geocoder upon saving
    """
    if not kwargs['created']:
        return
    member = kwargs['instance']
    # don't save if it's already in the record
    try:
        p = Location.objects.get(members=member.location)
    except Location.DoesNotExist:
        georet = geocode(member.geo_address)
        location = Location(
            place = georet[0],
            lat = "%s" % georet[1][0],
            lng = "%s" % georet[1][1]
        )
        location.save()

post_save.connect(encode_location, sender=Member)
