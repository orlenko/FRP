from django.contrib import admin
from . import models
from . import forms

class EventAdmin(admin.ModelAdmin):
    form = forms.EventForm
    list_display = ('title', 'start', 'end',)
    prepopulated_fields = {'slug': ('title',)}

class BlogPostAdmin(admin.ModelAdmin):
    form = forms.BlogPostForm
    list_display = ('title', 'pub_date',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Post, BlogPostAdmin)
