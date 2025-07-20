from django.urls import path
from .import views

app_name = 'cart'
urlpatterns = [
    path('detail', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>', views.CartAddView.as_view(), name='cart_list'),
    path('detail/<str:id>', views.OrderDetailView.as_view(), name='cart_detail'),
    path('order/<int:id>', views.OrderAddView.as_view(), name='cart_add'),
    path('apply/<int:pk>', views.ApplyDiscountView.as_view(), name='apply'),
]