from django.urls import path
from . import views

urlpatterns = [
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('set-password/', views.set_password, name='set_password'),
]
