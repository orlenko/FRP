from django.conf.urls.defaults import *
from views import *
from feeds import LatestPostFeed

urlpatterns = patterns('',
    # Consolidated views
    url(r'^$', consolidated_news_view, name='news_home'),
    # Blog views
    url(r'^blog/feed/$', LatestPostFeed(), name='post_feed'),
    url(r'^blog/$', archive_blog_post_view, name='post_archive_list'),
    url(r'^blog/(?P<year>\d{4})/$',
        year_blog_post_view,
        name='post_archive_year'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/$',
        month_blog_post_view,
        name='post_archive_month'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        day_blog_post_view,
        name='post_archive_day'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w\-]+)/$',
        blog_post_view, name="blog_post_view"),

    # Events for calendar
    url(r'calendar/$', archive_event_view, name='event_archive_list'),
    url(r'^calendar/(?P<year>\d{4})/$',
        year_event_view,
        name='event_archive_year'),
    url(r'^calendar/(?P<year>\d{4})/(?P<month>\d{2})/$',
        month_event_view,
        name='event_archive_month'),
    url(r'^calendar/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        day_event_view,
        name='event_archive_day'),

    url(r'^calendar/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w\-]+)/$',
        event_view, name="news_event_view"),
)

