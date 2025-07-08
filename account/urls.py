from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import LoginView, RegisterView

app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
]
