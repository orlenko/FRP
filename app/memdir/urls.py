from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^create/$', member_create_view, name='member_create'),
    url(r'^unknown/$', unknown_directory, name='unknown_dir'),
    url(r'^other/$', other_directory, name='other_dir'),
    url(r'^northern/$', northern_directory, name='northern_dir'),
    url(r'^fraser/$', fraser_directory, name='fraser_dir'),
    url(r'^interior/$', interior_directory, name='interior_dir'),
    url(r'^vanisle/$', vanisle_directory, name='vanisle_dir'),
    url(r'^vancoast/$', vancoast_directory, name='vancoast_dir'),
    url(r'^(?P<slug>[\w\-]+)/edit', member_change_view, name='member_edit'),
    url(r'^(?P<slug>[\w\-]+)', member_detail_view, name='member_view'),
    url(r'^$', member_directory_view, name='member_dir'),
)
