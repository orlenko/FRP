from django import template
from memdir import models


register = template.Library()


@register.filter
def region_name(region):
    return dict(models.REGION_CHOICES)[region]