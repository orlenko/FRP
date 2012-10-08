from django import forms
from memdir import models

class MemberAdminForm(forms.ModelForm):
    class Meta():
        model = models.Member
