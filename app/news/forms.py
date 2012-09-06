from django import forms
from . import models
from ckeditor.widgets import CKEditorWidget
from django.contrib.admin import widgets

class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['start'].widget = widgets.AdminSplitDateTime()
        self.fields['end'].widget = widgets.AdminSplitDateTime()

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['pub_date'].widget = widgets.AdminDateWidget()
        self.fields['exp_date'].widget = widgets.AdminDateWidget()
