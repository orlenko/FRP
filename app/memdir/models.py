from django.contrib.localflavor.us.models import PhoneNumberField
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
from geopy.geocoders import Google
from memdir.utils import unique_slugify
from south.modelsinspector import add_introspection_rules
from tinymce.models import HTMLField
import datetime
import logging


add_introspection_rules([], ["^tinymce\.models\.HTMLField"])

google = Google()

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

log = logging.getLogger(__name__)


class AddressMixin(models.Model):
    '''Common address fields used by several models.
    '''
    street = models.CharField(_("Street Address"), max_length=255, blank=True, null=True)
    city = models.CharField(_("City/Town"), max_length=255, blank=True, null=True)
    postal_code = models.CharField(_("Postal Code"), max_length=20, blank=True, null=True)
    province = models.CharField(_("Province"), max_length=10, choices=PROVINCE_CHOICES, default='BC')

    # Geo-API fields, populated automatically
    geo_place = models.CharField(max_length=255, blank=True, null=True)
    geo_lat = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    geo_lng = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    geo_last_updated = models.DateTimeField(blank=True, null=True)
    geo_last_address = models.CharField(max_length=255, blank=True, null=True)

    @property
    def address(self):
        return ('%(street)s, %(city)s, %(province)s %(postal_code)s'
                % self.__dict__)

    def update_geo(self):
        address = self.address
        if address == self.geo_last_address:
            # Do not repeat the same request again.
            return
        self.geo_last_address = address
        self.geo_last_updated = datetime.datetime.now()
        try:
            (self.geo_place,
             (self.geo_lat, self.geo_lng)) = google.geocode(self.address)
        except:
            log.debug('Failed to get geo data for %s' % self.address, exc_info=True)
        self.save()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.address


class MailingAddressMixin(models.Model):
    mailing_street = models.CharField(_("Street Address"), max_length=255, blank=True, null=True)
    mailing_city = models.CharField(_("City/Town"), max_length=255, blank=True, null=True)
    mailing_postal_code = models.CharField(_("Postal Code"), max_length=7, blank=True, null=True)
    mailing_province = models.CharField(_("Province"), max_length=2, choices=PROVINCE_CHOICES, default='BC')

    @property
    def mailing_address(self):
        return ('%(mailing_street)s, %(mailing_city)s, %(mailing_province)s %(mailing_postal_code)s'
                % self.__dict__)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.geo_mailing_address


class Member(AddressMixin, MailingAddressMixin):

    REGION_CHOICES = (
        ('other', _("Other")),
        ('fraservalley', _("Fraser Valley")),
        ('interior', _("Interior")),
        ('vancoast', _("Vancouver Coastal")),
        ('vanisle', _("Vancouver Island")),
        ('northern', _("Northern")),
        ('unknown', _("Unknown")),
    )

    MEMBERSHIP_CHOICES = (
        ('joint', _('Joint Member')),
        ('bc-only', _('BC-Only Member')),
    )

    agency = models.CharField(_("Member-Agency Name"), max_length=200)
    # Address fields are inherited from AddressMixin
    phone = PhoneNumberField(_("Agency Phone Number"), blank=True, null=True)
    fax = PhoneNumberField(_("Agency Fax Number"), blank=True, null=True)
    website = models.URLField(_("Website"), blank=True)
    region = models.CharField(choices=REGION_CHOICES, max_length=12, default='fraservalley')
    # Mailing Address fields are inherited from MailingAddressMixin

    agdirect = models.CharField(_("Contact Name"), max_length=255, blank=True)
    agdirect_title = models.CharField(_('Title'),
        max_length=255,
        default=_('Agency Executive Director / ECD Program Manager'))
    dirphone = PhoneNumberField(_("Direct Phone Number"), blank=True, null=True)
    email = models.EmailField(_("General Email"), blank=True)

    memnum = models.IntegerField(_("Membership Number"))
    renewal_date = models.DateField(_("Renewal Date"), blank=True, null=True)
    membership_type = models.CharField(_('Membership Type'),
                                       choices=MEMBERSHIP_CHOICES,
                                       default='joint',
                                       max_length=255)

    # Advanced fields
    fee = models.DecimalField(_("FRP Fee"), max_digits=9,
            decimal_places=2, blank=True, null=True)
    receipt = models.IntegerField(_("Reciept"), blank=True, null=True)
    paidfrp = models.BooleanField(_("Paid FRP fee"))
    description = HTMLField(_("Description (for directory)"), blank=True,
            help_text=_("Please describe your program and its goals."))
    notes = models.TextField(_("Notes"), blank=True,
            help_text=_("Internal notes about the member."))

    # Auto-updated fields
    join_date = models.DateField(_("FRP Member Since"), null=True)
    updated = models.DateField(_("Updated"))
    slug = models.SlugField(_("URL-friendly name"),
        max_length=255,
        unique=True,
        help_text=_("The slug must be a unique URL identifier."))


    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")
        ordering = ('agency', 'updated',)

    def __unicode__(self):
        return self.agency

    @models.permalink
    def get_absolute_url(self):
        return ('member_view', [str(self.slug)],)

    def save(self, *args, **kwargs):
        slugstr = "%s %s" % (self.agency, self.region)
        unique_slugify(self, slugstr)
        self.updated = datetime.datetime.now()
        super(Member, self).save(*args, **kwargs)


class Location(AddressMixin, MailingAddressMixin):
    """
    A basic optional location field for reverse geoadd usage
    """
    member = models.ForeignKey('Member', null=True, blank=True, related_name="locations")
    order = models.IntegerField(default=0)
    frp_program_name = models.CharField(_('Name of Family Resource Program'),
                                        max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return str(self.frp_program_name)


class LocationContact(models.Model):
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    contact_position = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(max_length=255, null=True, blank=True)
    location = models.ForeignKey(Location, related_name='contacts')

    def __unicode__(self):
        return ('%s, %s'
                % (self.contact_name, self.contact_position))


class HoursOfOperation(models.Model):
    DAY_CHOICES = (
        ('0', 'Sun'),
        ('1', 'Mon'),
        ('2', 'Tue'),
        ('3', 'Wed'),
        ('4', 'Thur'),
        ('5', 'Fri'),
        ('6', 'Sat'),
        )
    location = models.ForeignKey(Location, related_name="hours_of_operation")
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    open_time = models.TimeField(default='09:00:00')
    close_time = models.TimeField(default='17:00:00')

    @property
    def hours(self):
        return "%s - %s" % (self.open_time.strftime('%I:%M%p'),
                            self.close_time.strftime('%I:%M%p'))

    def __unicode__(self):
        return ('%s: %s>'
                % (self.day, self.hours))


def encode_location(sender, **kwargs):
    member = kwargs['instance']
    member.update_geo()
    for location in member.locations.all():
        location.update_geo()


post_save.connect(encode_location, sender=Member)
