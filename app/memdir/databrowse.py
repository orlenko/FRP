from django.contrib import databrowse
from memdir import models

databrowse.site.register(models.Member)
databrowse.site.register(models.Location)
databrowse.site.register(models.HoursOfOperation)
databrowse.site.register(models.LocationContact)



