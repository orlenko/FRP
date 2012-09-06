from django.core.management.base import BaseCommand, CommandError
import notification
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = '<None>'
    help = "A test command to try out sending notifications"
    def handle(self, *args, **options):
        admin = User.objects.get(id=1)
        user = User.objects.get(username="franky")
        notification.send([user], "member_expired", {"from_user": admin})
