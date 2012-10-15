from django.conf.urls import defaults
from memdir import views


urlpatterns = defaults.patterns('',
    defaults.url(r'^report/([^/]+)/(\d+)/', views.report_pdf, name='report'),
    defaults.url(r'^unknown/$', views.unknown_directory, name='unknown_dir'),
    defaults.url(r'^other/$', views.other_directory, name='other_dir'),
    defaults.url(r'^northern/$', views.northern_directory, name='northern_dir'),
    defaults.url(r'^fraser/$', views.fraser_directory, name='fraser_dir'),
    defaults.url(r'^interior/$', views.interior_directory, name='interior_dir'),
    defaults.url(r'^vanisle/$', views.vanisle_directory, name='vanisle_dir'),
    defaults.url(r'^vancoast/$', views.vancoast_directory, name='vancoast_dir'),
    defaults.url(r'^(?P<slug>[\w\-]+)', views.member_detail_view, name='member_view'),
    defaults.url(r'^$', views.member_directory_view, name='member_dir'),
)
