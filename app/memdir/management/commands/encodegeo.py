from django.core.management.base import BaseCommand
from memdir.models import Member


class Command(BaseCommand):
    '''Encode the addresses of the members into a Location'''
    args = '<None>'
    help = 'Encodes addresses into lat & lng for all Members'
    def handle(self, *args, **options):
        members = Member.objects.all()
        for mem in members:
            mem.update_geo()
            for location in mem.locations:
                location.update_geo()


