from django.urls import path
from .import views
from .views import LoginView


app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]