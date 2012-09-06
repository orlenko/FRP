from django.db import models
import datetime
from itertools import chain

class PostManager(models.Manager):
    """
    Returns published posts via their date
    """
    def get_query_set(self):
        ret = super(PostManager,
                self).get_query_set()
        ret = ret.filter(pub_date__lte=datetime.datetime.now())
        ret = ret.exclude(exp_date__lte=datetime.datetime.now())
        return ret

class EventManager(models.Manager):
    """
    Only returns unexpired events
    """
    def get_query_set(self):
        ret = super(EventManager, self).get_query_set()
        ret = ret.filter(end__gte=datetime.datetime.now())
        return ret
