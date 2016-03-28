from __future__ import with_statement
import csv

from django.core.management.base import BaseCommand
from memdir.models import Member


def t(s):
    return s.encode('utf8')


headers = [
    'agency',
    'membership_number',
    'renewal_date',
    'street',
    'city',
    'province',
    'postal_code',
    'phone',
    'fax',
    'website',
    'contact_name',
    'contact_title',
    'email',
    'direct_phone',
    'mail_street',
    'mail_city',
    'mail_province',
    'mail_postal_code',
    'deliver_frp_program',
    'memebership_type',
    'frp_program_name',
    'location_street',
    'location_city',
    'location_province',
    'location_postal_code',
    'location_mail_street',
    'location_mail_city',
    'location_mail_province',
    'location_mail_postal_code',
    'location_phone',
    'location_fax',
    'location_website',
    'location_contact_name',
    'location_contact_position',
    'location_contact_email',
    'location_extra_contacts',
    'location_hours',
]


class Command(BaseCommand):
    """Export members into a csv file."""

    def handle(self, *args, **options):
        with open('all_members.csv', 'w') as outfile:
            outfile.write(u'\ufeff'.encode('utf8'))
            wr = csv.DictWriter(outfile, headers)
            wr.writerow(dict((fn, fn) for fn in headers))
            for member in Member.objects.all():
                for location in member.locations.all():
                    wr.writerow({
                        'agency': t(member.agency),
                        'membership_number': t(member.memnum),
                        'renewal_date': t(member.formatted_renewal_date),
                        'street': t(member.street),
                        'city': t(member.city),
                        'province': t(member.province),
                        'postal_code': t(member.postal_code),
                        'phone': t(member.phone),
                        'fax': t(member.fax),
                        'website': t(member.website),
                        'contact_name': t(member.agdirect),
                        'contact_title': t(member.agdirect_title),
                        'email': t(member.email),
                        'direct_phone': t(member.dirphone),
                        'mail_street': t(member.mailing_street),
                        'mail_city': t(member.mailing_city),
                        'mail_province': t(member.mailing_province),
                        'mail_postal_code': t(member.mailing_postal_code),
                        'deliver_frp_program': t(member.format_is_frp),
                        'memebership_type': t(member.membership_type),
                        'frp_program_name': t(location.frp_program_name),
                        'location_street': t(location.street),
                        'location_city': t(location.city),
                        'location_province': t(location.province),
                        'location_postal_code': t(location.postal_code),
                        'location_mail_street': t(location.mailing_street),
                        'location_mail_city': t(location.mailing_city),
                        'location_mail_province': t(location.mailing_province),
                        'location_mail_postal_code':
                            t(location.mailing_postal_code),
                        'location_phone': t(location.phone),
                        'location_fax': t(location.fax),
                        'location_website': t(location.website),
                        'location_contact_name': t(getattr(
                            location.main_contact, 'contact_name', '')),
                        'location_contact_position': t(getattr(
                            location.main_contact, 'contact_position', '')),
                        'location_contact_email': t(getattr(
                            location.main_contact, 'contact_email', '')),
                        'location_extra_contacts': format_extra_contacts(
                            location.extra_contacts),
                        'location_hours': format_hours(
                            location.days_of_operations)
                    })


def format_extra_contacts(contacts):
    return '; '.join([', '.join((t(contact.contact_name),
                                 t(contact.contact_position),
                                 t(contact.contact_email)))
                      for contact in contacts])


def format_hours(days):
    return ', '.join([': '.join((t(day.name), t(day.formatted_hours)))
                      for day in days])
