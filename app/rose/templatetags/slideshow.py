# -*-coding: utf8-*-
"""
slideshow templatetags
"""
from django import template
from django.utils.translation import ugettext_lazy as _
from rose.models import Slide ## this may get placed in verbena

register = template.Library()

@register.inclusion_tag('rose/templatetags/slideshow.html', takes_context=True)
def slideshow(context):
    """
    Displays a slideshow based on the model
    eg:
        {% slideshow "frontpage" %} -> frontpage slideshow model
    """
    slides = ''
    slides = Slide.published.all()
    ret = dict(slides=slides)
    return ret

