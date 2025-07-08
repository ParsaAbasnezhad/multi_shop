from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginUserForm, ChackOtpForm ,OtpLoginForm
from django.views.generic import View
from random import randint
from uuid import uuid4
from .models import Otp
from django.urls import reverse

class LoginView(View):
    def get(self, request):
        form = LoginUserForm()
        return render(request, "account/login.html", context={'form': form})

    def post(self, request):
        form = LoginUserForm(self.request)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get('phone'), password=data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('phone', 'error in phone')
        else:
            form.add_error('phone', 'error in phone or password')

        return render(request, 'account/login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = OtpLoginForm()
        return render(request, "account/register.html", context={'form': form})
    def post(self, request):
        form = OtpLoginForm(self.request)
        if form.is_valid():
            data = form.cleaned_data
            randcode = randint(10000, 99999)
            token = str(uuid4())
            Otp.objects.create(phone=data['phone'], code=randcode, token=token)
            print(randcode)
            return redirect(reverse('account/chech_otp.html') + f'?token= + {token}')
        else:
            form.add_error('phone', 'error in phone or password')

        return render(request, 'account/register.html', {'form': form})