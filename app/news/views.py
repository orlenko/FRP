from django.views.generic import DateDetailView, MonthArchiveView,\
    ArchiveIndexView, YearArchiveView, DayArchiveView

from django.http import HttpResponse
from django.shortcuts import render

from . import models

def consolidated_news_view(request, *args, **kwargs):
    posts = models.Post.published.all()
    #events = models.Event.objects.all()
    #ret = dict(events=events, posts=posts)
    ret = dict(posts=posts)
    return render(request, 'news/home.html', ret)

# Blog Views
class ArchiveBlogPostView(ArchiveIndexView):
    allow_empty = True
    queryset = models.Post.published.all()
    model = models.Post

archive_blog_post_view = ArchiveBlogPostView.as_view(date_field='pub_date')

class YearBlogPostView(YearArchiveView):
    queryset = models.Post.published.all()
    model = models.Post

year_blog_post_view = YearBlogPostView.as_view(date_field = 'pub_date')

class MonthBlogPostView(MonthArchiveView):
    queryset = models.Post.published.all()
    model = models.Post
    month_format = "%m"

month_blog_post_view = MonthBlogPostView.as_view(date_field='pub_date')

class DayBlogPostView(DayArchiveView):
    queryset = models.Post.published.all()
    model = models.Post
    month_format = "%m"

day_blog_post_view = DayBlogPostView.as_view(date_field='pub_date')

class BlogPostView(DateDetailView):
    queryset = models.Post.published.all()
    model = models.Post
    month_format = "%m"
    context_object_name = "post"

blog_post_view = BlogPostView.as_view(date_field='pub_date')

# Event Views
class ArchiveEventView(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    model = models.Event

archive_event_view = ArchiveEventView.as_view(date_field='start')

class YearEventView(YearArchiveView):
    allow_empty = True
    allow_future = True
    make_object_list = True
    context_object_name = "events"
    model = models.Event

year_event_view = YearEventView.as_view(date_field='start')

class MonthEventView(MonthArchiveView):
    model = models.Event
    allow_future = True
    make_object_list = True
    context_object_name = "events"
    month_format = "%m"

month_event_view = MonthEventView.as_view(date_field='start')

class DayEventView(DayArchiveView):
    model = models.Event
    allow_future = True
    make_object_list = True
    context_object_name = "events"
    month_format = "%m"

day_event_view = DayEventView.as_view(date_field='start')

class EventView(DateDetailView):
    model = models.Event
    allow_future = True
    make_object_list = True
    month_format = "%m"
    context_object_name = "event"

event_view = EventView.as_view(date_field='start')
