from django.views.generic import DetailView
from django.shortcuts import render
from .models import ShopDetail


class Detail(DetailView):
    model = ShopDetail
    template_name = 'shop/detail.html'




