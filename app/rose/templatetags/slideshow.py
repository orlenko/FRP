# -*-coding: utf8-*-
"""
slideshow templatetags
"""
from django import template
from rose.models import Slide ## this may get placed in verbena

register = template.Library()


@register.inclusion_tag('rose/templatetags/slideshow.html', takes_context=True)
def slideshow(context):
    """
    Displays a slideshow based on the model
    eg:
        {% slideshow "frontpage" %} -> frontpage slideshow model
    """
    slides = Slide.objects.filter(is_published=True)
    ret = dict(slides=slides)
    return ret

