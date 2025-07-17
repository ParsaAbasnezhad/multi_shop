import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View

from .forms import SendOTPForm, VerifyOTPForm, SetPasswordForm, AddressForm
from .models import User, OTPCode, Address
from django.contrib.auth.hashers import make_password


def send_otp(request):
    if request.method == 'POST':
        form = SendOTPForm(request.POST)
        if form.is_valid():
            email_or_phone = form.cleaned_data['email_or_phone']
            code = str(random.randint(100000, 999999))
            OTPCode.objects.create(email_or_phone=email_or_phone, code=code)
            print(f"{email_or_phone} OTP code: {code}")
            return redirect('verify_otp')
        else:
            return render(request, 'account/send_otp.html', {'form': form})
    else:
        form = SendOTPForm()
        return render(request, 'account/send_otp.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        form = VerifyOTPForm(request.POST)
        if form.is_valid():
            email_or_phone = form.cleaned_data['email_or_phone']
            code = form.cleaned_data['code']
            otp = OTPCode.objects.filter(email_or_phone=email_or_phone, code=code).last()
            if otp and otp.is_valid():
                user, created = User.objects.get_or_create(email_or_phone=email_or_phone)
                login(request, user)
                if created or not user.has_usable_password():
                    return redirect('set_password')
                return redirect('home')
            else:
                form.add_error('code', 'کد OTP معتبر نیست.')
        return render(request, 'account/verify_otp.html', {'form': form})
    else:
        form = VerifyOTPForm()
        return render(request, 'account/verify_otp.html', {'form': form})



def set_password(request):
    if not request.user.is_authenticated:
        return redirect('send_otp')

    if request.method == 'POST':
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            request.user.password = make_password(form.cleaned_data['password'])
            request.user.save()
            return redirect('home')
        else:
            return render(request, 'account/set_password.html', {'form': form})
    else:
        form = SetPasswordForm()
        return render(request, 'account/set_password.html', {'form': form})



class AddAddressView(View):
    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            address =form.save(commit=False)
            address.user = request.user
            form.save()
        return render(request, 'account/checkout.html',{'form': form})