from django.core.management.base import BaseCommand
from optparse import make_option
import re
import csv
from memdir import models
import datetime
import logging


log = logging.getLogger(__name__)


re_year = re.compile(r'(\d\d\d\d)')
re_month = re.compile(r'([a-zA-Z]+)')
re_url = re.compile(r'#([#]+)#')


def parse_date(datestr):
    if not datestr:
        return None
    year = re_year.search(datestr)
    month = re_month.search(datestr)
    if not year:
        return None
    if month:
        date_format = r'%Y-%B'
        date_str = '%s-%s' % (year.group(1), month.group(1))
    else:
        date_format = r'%Y'
        date_str = year.group(1)
    return datetime.datetime.strptime(date_str, date_format)


def match_region(longregion):
    translate = {
        'Other': 'other',
        'Fraser Valley': 'fraservalley',
        'Interior': 'interior',
        'Vancouver Island': 'vanisle',
        'Northern': 'northern',
        'Vancouver Coastal': 'vancoast',
    }
    return translate.get(longregion, 'uknown')


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--noinput', action='store_false', dest='interactive', default=True,
            help='Tells Django to NOT prompt the user for input of any kind.'),
        make_option('--failfast', action='store_true', dest='failfast', default=False,
            help='Tells Django to stop running the test suite after first failed test.')
    )
    help = 'Import member data from a CSV file'
    args = 'filename'

    requires_model_validation = False

    def import_rec(self, rec):
        try:
            member, _is_new = models.Member.objects.get_or_create(agency=rec['tAgencyName'])
            member.street = rec['tAgencyAddress1']
            member.city = rec['tAgencyCity']
            member.postal_code = rec['tAgencyPC']
            member.province = rec['tAgencyProv']
            member.phone = rec['tMemberPhone']
            member.fax = rec['tMemberFax']
            url = re_url.search(rec['tAgencyWebsite'])
            if url:
                member.website = url.group(1)
            member.region = match_region(rec['tRegion'])
            if rec['bMailingSameAs'] == '1':
                member.mailing_street = member.street
                member.mailing_city = member.city
                member.mailing_postal_code = member.postal_code
                member.mailing_province = member.province
            else:
                member.mailing_street = rec['tMailingAddress1']
                member.mailing_city = rec['tMailingCity']
                member.mailing_postal_code = rec['tMailingPC']
                member.mailing_province = rec['tMailingProv']
            member.agdirect = rec['tAgencyDirector']
            member.agdirect_title = rec['tAgencyContactTitle']
            member.dirphone = rec['tAgencyDirectorPhone']
            if rec['tAgencyDirectorExt']:
                member.dirphone += ' ext %s' % rec['tAgencyDirectorExt']
            member.email = rec['tAgencyDirectorEmail']
            member.memnum = rec['tNumber']
            renewal = rec['dRenewal']
            if renewal:
                member.renewal_date = datetime.datetime.fromtimestamp(float(renewal) / 1000)
            member.membership_type = rec['tFRPJointMembership'] == '1'
            #member.fee = # TODO: what field should we use for this?
            member.receipt = rec['tReceiptNo']
            #member.paidfrp = # TODO: what field should we use for this?
            #member.description =
            member.notes = rec['tPSPProgressNotes']
            member.join_date = parse_date(rec['tJoinDate'])
            member.save()
            # Now, for FRP members with extra addresses, we create locations.
            if rec['tFRPCanadaMember'] == '1':
                location, _is_new = models.Location.objects.get_or_create(member=member,
                    frp_program_name=member.agency)

                location.street = member.street
                location.city = member.city
                location.postal_code = member.postal_code
                location.province = member.province

                location.mailing_street = member.mailing_street
                location.mailing_city = member.mailing_city
                location.mailing_postal_code = member.mailing_postal_code
                location.mailing_province = member.mailing_province

                location.frp_program_name = member.agency
                location.save()
                location_contact, _is_new = models.LocationContact.objects.get_or_create(location=location,
                                                                contact_name=rec['tAgencyDirector'])
                location_contact.contact_name = rec['tAgencyDirector']
                location_contact.contact_position = rec['tAgencyContactTitle']
                location_contact.contact_email = rec['tAgencyDirectorEmail']
                location_contact.save()
        except:
            log.debug('Failed to import record: %s' % rec, exc_info=True)

    def handle(self, *args, **options):
        header = None
        filename = args[0]
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if header:
                    log.debug('row length: %s' % len(row))
                    assert len(row) == len(header)
                    rec = dict(zip(header, row))
                    self.import_rec(rec)
                else:
                    header = row
                    log.debug('header length: %s' % len(header))
