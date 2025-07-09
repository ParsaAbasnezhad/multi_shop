from django.urls import path
from .import views
from .views import ShopListView

app_name = 'shop'
urlpatterns = [
    path('shop/', ShopListView.as_view(), name='shop_list'),
]