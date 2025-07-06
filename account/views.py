from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.views.generic import View


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account/login.html" , context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
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

        return render(request,'account/login.html', {'form': form})

