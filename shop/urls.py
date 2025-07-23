from django.urls import path
from .import views
from .views import ShopDetailView

app_name = 'shop'
urlpatterns = [
    path('shop/', ShopDetailView.as_view(), name='shop'),
]

