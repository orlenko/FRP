from django.contrib.sitemaps import Sitemap
from models import Member

class MemberSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Member.objects.filter(is_active=True)
    def last_mod(self, obj):
        return obj.site_updated
