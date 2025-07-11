from wsgiref.validate import validator
from django import forms
from django.core.validators import MaxLengthValidator



class SendOTPForm(forms.Form):
    email_or_phone = forms.CharField()

class VerifyOTPForm(forms.Form):
    email_or_phone = forms.CharField()
    code = forms.CharField(min_length=6, max_length=6)


class SetPasswordForm(forms.Form):
      password = forms.CharField(widget=forms.PasswordInput())
