from django.core.management.base import BaseCommand, CommandError
from memdir.models import MemberUser, Member
import datetime
import notification
from pprint import pprint

def notify_member(member, notif):
    context = {
            'member': member,
            }
    for user in member.users.all():
        user = user.user
        notification.send([user], notif, context)
        pprint("User %s was notified with notification %s for agency %s" %
                (user.username, notif, member.agency))
    member.rec_expiry_notice=True
    member.save()

class Command(BaseCommand):
    args = '<None>'
    help = """Sends a notification via web and email interfaces about:
            * expired members,
            * expiries happening within a month,
            """
    def handle(self, *args, **options):
        next_month = datetime.datetime.now() + datetime.timedelta(365/12)
        upcoming_members =\
            Member.objects.filter(is_subscribed=True).filter(is_active=True).filter(rec_upcoming_notice=False).filter(rec_expiry_notice=False).filter(next_expiry__lte=next_month)
        expired_members =\
            Member.objects.filter(is_subscribed=True).filter(is_active=False).filter(rec_expiry_notice=False)
        for member in expired_members:
            notify_member(member, "member_expired")
        for member in upcoming_members:
            notify_member(member, "upcoming_expired")

