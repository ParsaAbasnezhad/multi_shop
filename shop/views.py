from django.views.generic import TemplateView
from django.shortcuts import render


class ShopListView(TemplateView):
    template_name = 'shop/shop.html'

