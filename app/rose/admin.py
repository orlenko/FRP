from django.contrib import admin

from rose.models import Slide

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'description', 'link', 'weight')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Slide, SlideAdmin)
