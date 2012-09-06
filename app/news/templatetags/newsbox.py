from django import template
from .. import models

register = template.Library()

@register.inclusion_tag('news/newsbox.html', takes_context=True)
def newsbox(context):
    '''
        A Basic news box with no input on the template tag
    '''
    posts = models.Post.published.all()
    events = models.Event.published.all()
    return dict(posts=posts, events=events, request=context['request'],
        STATIC_URL=context['STATIC_URL'])

