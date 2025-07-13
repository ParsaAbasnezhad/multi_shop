from django.urls import path
from .import views
from .views import Detail



app_name = 'shop'
urlpatterns = [
    path('<int:pk>',views.DetailList.as_view(), name='detail'),
]
