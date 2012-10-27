from django.contrib import admin

from memdir import forms
from memdir import models


class InlineHours(admin.TabularInline):
    model = models.HoursOfOperation
    extra = 1


class InlineContact(admin.TabularInline):
    model = models.LocationContact
    extra = 1


class InlineLocation(admin.StackedInline):
    model = models.Location
    inlines = [InlineHours, InlineContact,]
    extra = 1
    fieldsets = (
        (None, {
            'fields': (
                'frp_program_name',
                'street',
                'city',
                'province',
                'postal_code',
                'phone',
                'fax',
            )
        }),
        ('Mailing Address (if different from physical address)', {
            'classes': ('collapse',),
            'fields': (
                'mailing_street',
                'mailing_city',
                'mailing_postal_code',
                'mailing_province',
            )
        }),
    )



class MemberAdmin(admin.ModelAdmin):
    form = forms.MemberAdminForm
    actions_on_top = True
    actions_on_bottom = True
    list_display = ('agency', 'renewal_date', 'region', 'memnum')
    search_fields = ('agency',)
    list_filter = ('region', 'renewal_date',)
    date_hierarchy = 'renewal_date'
    ordering = ('agency',)
    change_form_template = 'admin_edit_agency2.html'
    inlines = [InlineLocation,]
    readonly_fields = ['slug']
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': (
                'agency',
                'street',
                'city',
                'postal_code',
                'province',
                'phone',
                'fax',
                'website',
                'region',
                'community',
                'join_date',
                'updated',
                'notes',
            )
        }),
        (#'Contact', {
         None, {
            'fields': (
                'agdirect',
                'agdirect_title',
                'dirphone',
                'email',
            )
        }),
        (#'Membership', {
         None, {
            'fields': (
                'memnum',
                'renewal_date',
                'membership_type',
            )
        }),
        ('Mailing Address (if different from physical address)', {
            'classes': ('collapse',),
            'fields': (
                'mailing_street',
                'mailing_city',
                'mailing_postal_code',
                'mailing_province',
            )
        }),
        ('Payment Information', {
            'classes': ('collapse',),
            'fields': (
                'fee',
                'receipt',
                'paidfrp',
            )
        }),
    )


class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.HoursOfOperation)
admin.site.register(models.LocationContact)
