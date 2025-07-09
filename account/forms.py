from wsgiref.validate import validator
from django import forms
from django.core.validators import MaxLengthValidator



class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError('username too short')
        return username


class OtpLoginForm(forms.Form):
    phone=forms.CharField(max_length=14,widget=forms.TextInput(attrs={'class': 'form-control'}))


class ChackOtpForm(forms.Form):
    code=forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class': 'form-control'}))

