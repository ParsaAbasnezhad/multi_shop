from django.urls import path
from . import views
from .views import ShopDetailView

app_name = 'shop'
urlpatterns = [
    path('', ShopDetailView.as_view(), name='shop'),
    path('shop/detail', ShopDetailView.as_view(), name='shap_detail'),
]
