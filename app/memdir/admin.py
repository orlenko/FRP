from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import forms
from . import models

class MemberAdmin(admin.ModelAdmin):
    form = forms.StaffMemberAdminForm
    prepopulated_fields = {'slug': ('agency',)}
    list_display = ('agency', 'renewal', 'region', 'memnum',
            'successful_location_save')

class MemberUserAdmin(admin.ModelAdmin):
    model = models.MemberUser

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.MemberUser, MemberUserAdmin)
admin.site.register(models.Location, LocationAdmin)
