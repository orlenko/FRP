from django.core.management.base import BaseCommand, CommandError
from memdir.models import Member
import datetime
from pprint import pprint

class Command(BaseCommand):
    args = '<None>'
    help = """Finds all the Members in the database with an expired entry and
            tags them as expired. This command should be run right before the
        send_notices command.
            """
    def handle(self, *args, **options):
        now = datetime.datetime.now()
        expired_members = Member.objects.filter(renewal__lte=now)
        for member in expired_members:
            member.is_active=False
            pprint("Agency %s is expired" % member.agency)
            try:
                member.save()
            except:
                pprint("ERROR: Agency %s could not be saved" % member.agency)
