from django.conf.urls import defaults
from django.views.generic import RedirectView
from memdir import views


urlpatterns = defaults.patterns('',
    defaults.url(r'^region/([^/]+)/', views.RegionView.as_view(), name='region'),
    defaults.url(r'^community/([^/]+)/', views.CommunityView.as_view(), name='community'),
    defaults.url(r'^report/region/([^/]+)/', views.report_region_pdf, name='report_region'),
    defaults.url(r'^report/([^/]+)/(\d+)/', views.report_pdf, name='report'),
    defaults.url(r'^(?P<slug>[\w\-]+)', views.location_detail_view, name='location_view'),
    defaults.url(r'^$', views.member_directory_view, name='member_dir'),
)
