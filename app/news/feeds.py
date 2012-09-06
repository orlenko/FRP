from django.contrib.syndication.views import Feed
from . import models

from django.utils.translation import ugettext as _

class LatestPostFeed(Feed):
    """
        Feed of the latest posts in the blog
    """
    title = _("FRP-BC Latest Blog Posts")
    link = "/news/blog/"
    description = _("Updates on the Family Resource Centre")

    def items(self):
        return models.Post.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

