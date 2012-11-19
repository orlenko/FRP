from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.auth.decorators import login_required
#from django.contrib import databrowse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from memdir.sitemaps import MemberSitemap

sitemaps = {
    "member": MemberSitemap,
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    #url(r'^databrowse/(.*)', login_required(databrowse.site.root)),
    (r'^api/v2/', include('fiber.rest_api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User account login
    #url(r'^accounts/', include('registration.urls')),
    # User notifications
    #url(r'^notifications/', include('notification.urls')),

    # Bot helpers
    url(r'sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)


# News urls
urlpatterns += patterns('',
    url(r'^news/', include('news.urls')),
    url(r'^dir/', include('memdir.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^$', "frontpage.views.front_page_view"),
    url(r'^/$', "frontpage.views.front_page_view"),
    (r'^ckeditor/', include('ckeditor.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        #    'document_root': settings.STATIC_ROOT,
        #}),
    )

urlpatterns += patterns('',
    url(r'', 'fiber.views.page'),
)