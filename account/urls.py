from django.urls import path
from . import views
from .views import LoginView, RegisterView, CheckOtpView



app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('check/', CheckOtpView.as_view(), name='check'),
]
