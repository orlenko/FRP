from django.contrib import databrowse
from . import models

databrowse.site.register(models.Member)

