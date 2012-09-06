from django.db import models
from photologue.models import Photo
import datetime
#from tinymce.models import HTMLField

from ckeditor.fields import RichTextField as HTMLField
from managers import PostManager, EventManager

from django.utils.translation import ugettext as _

class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    pub_date = models.DateField(_("Publish Date"),
        default=datetime.datetime.today())
    exp_date = models.DateField(_("Expiry Date"),
        help_text=_("If specified, this will be when the post is removed."),
        blank=True, null=True)
    content = HTMLField()

    objects = models.Manager()
    published = PostManager()

    class Meta:
        ordering = ['-pub_date',]
        verbose_name = "News Post"

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_view', (), {
            'year': str(self.pub_date.year),
            'month': str(self.pub_date.strftime("%m")),
            'day': str(self.pub_date.strftime("%d")),
            'slug': self.slug,
        })

class Event(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    description = HTMLField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    objects = models.Manager()
    published = EventManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-start']
        verbose_name = "Event Calendar"
        verbose_name_plural = "Event Calendar"


    @models.permalink
    def get_absolute_url(self):
        return ('news_event_view', (), {
            'year': str(self.start.year),
            'month': str(self.start.strftime("%m")),
            'day': str(self.start.strftime("%d")),
            'slug': self.slug,
        })


class SlideImage(Photo):
    """
        Using photologue model here, perhaps inappropriately.
    """
    order = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ("order",)

class Slide(models.Model):
    image = models.OneToOneField(SlideImage, related_name='slide')

class Marquee(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField()
    slides = models.ManyToManyField(Slide, related_name='marquee')

