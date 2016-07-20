import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


class NewProjectForm(forms.Form):

    project_code = forms.CharField(label='Project Code', max_length=100)
    project_inc = forms.CharField(label='Increment', max_length=100)
    project_name = forms.CharField(label='Project Name', max_length=100)
    project_start = forms.CharField(label='Start Date', max_length=100)
    project_end = forms.CharField(label='Deadline', max_length=100)

    creator_id = forms.CharField(label='creator_id', max_length=100)
    assigned_user_id = forms.CharField(label='assigned_user_id', max_length=500)
    location = forms.CharField(label='location', max_length=1000)
    signedoff = forms.BooleanField(label='signedoff')
    flagdelete = forms.BooleanField(label='flagdelete')

class NewCommentForm(forms.Form):
    op_id = forms.CharField(label='op_id', max_length=100)
    item_id = forms.CharField(label='item_id', max_length=100)
    subject = forms.CharField(label='subject')
    content = forms.CharField(label='content')
    rate = forms.CharField(label='rate')
    # read = forms.BooleanField(label='read')

    parent_id = forms.CharField(label='parent_id')


class DelNote(forms.Form):
    id_to_del = forms.CharField(label='id_to_del', widget=forms.HiddenInput())

class UpdateRegistrationForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100, required=False)
    last_name = forms.CharField(label='last_name', max_length=100, required=False)
    dob = forms.CharField(label='dob', max_length=100, required=False)
    med_provider = forms.CharField(label='med_provider', max_length=100, required=False)
    med_plan = forms.CharField(label='med_plan', max_length=100, required=False)
    dent_provider = forms.CharField(label='dent_provider', max_length=100, required=False)
    dent_plan = forms.CharField(label='dent_plan', max_length=100, required=False)

class UploadMedia(forms.Form):
    op_id = forms.CharField(label='op_id', max_length=100, required=False)
    media_type = forms.CharField(label='media_type', max_length=100, required=False)
    media_name = forms.CharField(label='media_name', max_length=100, required=False)
    media_pname = forms.CharField(label='media_pname', max_length=100, required=False)
    media_pname_thumb = forms.CharField(label='media_pname_thumb', max_length=100, required=False)
    note_id = forms.CharField(label='note_id', max_length=100, required=False)
