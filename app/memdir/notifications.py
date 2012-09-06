"""
This is both the help file and the general location of the location-building
index for the memdir project

There are 2 different types of time-based notifications which can go out:
        * member_expired : when a membership has passed its date
            without a indication of renewal.
        * upcoming_expiry : when a member has a month or less to renew a
            membership.

    These go to all users in the group (Member.users), and to the admin
    (perhaps in a separate email?)). These are stored in this file but are
    triggered in a management command "send_notices" and can be triggered as
    such:
        $ python manage.py send_notices

    Note that this will also need a proper Email-Dispatcher working, and the
    templates will likely need some tweaking.

    The rest of the notifications are simple greetings. They are triggered in
    the signals.py file, but may also be in this file for reference (?)

    Web-notices (default=emailed too):
        * welcome_old : welcomes old members to the memdir
        * welcome_new : welcomes new registrants to create a Member or add
        themselves to one.
        * notify_join : notifies member-users about a new addition.

    Notifications should be imported after signals in __init__.py
        from signals import *
        from notifications import *
    from notifications import *
"""
