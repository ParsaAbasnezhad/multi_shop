from django.urls import path
from .import views
from .views import Detail


app_name = 'shop'
urlpatterns = [
    path('detail/<int:id>', Detail.as_view(), name='detail'),
]