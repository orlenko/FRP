import csv

from django.core.management.base import BaseCommand
from memdir.models import Member


class Command(BaseCommand):
    """Export members into a csv file."""

    def handle(self, *args, **options):
        with open('all_members.csv', 'w') as outfile:
            wr = csv.DictWriter(outfile, [
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
                'location_hours',])
            for member in Member.objects.all():
                for location in member.locations.all():
                    wr.writerow({
                        'agency': member.agency,
                        'membership_number': member.memnum,
                        'renewal_date': member.formatted_renewal_date,
                        'street': member.street,
                        'city': member.city,
                        'province': member.province,
                        'postal_code': member.postal_code,
                        'phone': member.phone,
                        'fax': member.fax,
                        'website': member.website,
                        'contact_name': member.agdirect,
                        'contact_title': member.agdirect_title,
                        'email': member.email,
                        'direct_phone': member.dirphone,
                        'mail_street': member.mailing_street,
                        'mail_city': member.mailing_city,
                        'mail_province': member.mailing_province,
                        'mail_postal_code': member.mailing_postal_code,
                        'deliver_frp_program': member.format_is_frp,
                        'memebership_type': member.membership_type,
                        'frp_program_name': location.frp_program_name,
                        'location_street': location.street,
                        'location_city': location.city,
                        'location_province': location.province,
                        'location_postal_code': location.postal_code,
                        'location_mail_street': location.mailing_street,
                        'location_mail_city': location.mailing_city,
                        'location_mail_province': location.mailing_province,
                        'location_mail_postal_code':
                            location.mailing_postal_code,
                        'location_phone': location.phone,
                        'location_fax': location.fax,
                        'location_website': location.website,
                        'location_contact_name': location.main_contact.contact_name,
                        'location_contact_position':
                            location.main_contact.contact_position,
                        'location_contact_email':
                            location.main_contact.contact_email,
                        'location_extra_contacts': format_extra_contacts(
                            location.extra_contacts),
                        'location_hours': format_hours(
                            location.days_of_operations)
                    })


def format_extra_contacts(contacts):
    return '; '.join([', '.join((contact.contact_name,
                                 contact.contact_position,
                                 contact.contact_email))
                      for contact in contacts])


def format_hours(days):
    return ', '.join([': '.join((day.name, day.formatted_hours))
                      for day in days])
