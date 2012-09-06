from django import forms
from . import models

class MemberAdminForm(forms.ModelForm):
    class Meta():
        model = models.Member

class UserMemberAdminForm(MemberAdminForm):
    """
        The form exposed to the front-end user.
        This form is filtered when used as registration.
    """
    class Meta():
        model = models.Member
        fields = ('agency','region','address','city','province', 'postal_code',
                'agphone', 'agfax', 'agdirect', 'dirphone', 'email', 'resname',
                'frpphone', 'coordinator', 'coemail', 'website','description',)

class RegisterMemberForm(UserMemberAdminForm):
    """
        The front-end member request/registration form
        filters the fields
    def __init__(self):
        super(RegisterMemberForm, self).__init__(*args, **kwargs)
        self.fields['']
    """
    class Meta():
        model = models.Member
        fields = ('agency','region','description',)

class StaffMemberAdminForm(MemberAdminForm):
    """
        The form exposed to the staff/admin user
    """
    class Meta():
        exclude = ('updated', 'site_updated', 'location')
