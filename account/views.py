from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginUserForm, ChackOtpForm, OtpLoginForm
from django.views.generic import View
from random import randint
from uuid import uuid4
from .models import Otp, User
from django.urls import reverse


class LoginView(View):
    def get(self, request):
        form = LoginUserForm()
        return render(request, "account/login.html", context={'form': form})

    def post(self, request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get('phone'), password=data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('phone', 'شماره تلفن یا رمز عبور اشتباه است.')
        else:
            form.add_error('phone', 'شماره تلفن یا رمز عبور اشتباه است.')

        return render(request, 'account/login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = OtpLoginForm()
        return render(request, "account/register.html", {'form': form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            randcode = randint(10000, 99999)
            token = str(uuid4())
            Otp.objects.create(phone=data['phone'], code=randcode, token=token)
            print(randcode)
            return redirect(reverse('account:check_otp') + f'?token={token}')
        else:
            form.add_error('phone', 'شماره تلفن وارد شده صحیح نیست.')

        return render(request, 'account/register.html', {'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = ChackOtpForm()
        return render(request, "account/check_otp.html", context={'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = ChackOtpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            if Otp.objects.filter(code=data['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user, backend='account.authentication.EmailAuthBackend')
                otp.delete()
                return redirect('/')
            else:
                form.add_error('code', 'کد وارد شده اشتباه است.')
        else:
            form.add_error('code', 'کد وارد شده صحیح نیست.')

        return render(request, 'account/check_otp.html', {'form': form})
