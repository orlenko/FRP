from django.db import models
import datetime
from itertools import chain

import logging

log = logging.getLogger(__name__)


class PostManager(models.Manager):
    """
    Returns published posts via their date
    """
    def get_query_set(self):
        log.debug('Creating query set for Posts...')
        ret = super(PostManager,
                self).get_query_set()
        now = datetime.datetime.now()
        log.debug('Will filter out by date: %s' % now)
        ret = ret.filter(pub_date__lte=now)
        ret = ret.exclude(exp_date__lte=now)
        return ret

class EventManager(models.Manager):
    """
    Only returns unexpired events
    """
    def get_query_set(self):
        ret = super(EventManager, self).get_query_set()
        ret = ret.filter(end__gte=datetime.datetime.now())
        return ret
