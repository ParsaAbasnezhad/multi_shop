from django.views.generic import DetailView
from django.shortcuts import render
from shop.models import Detail


class DetailList(DetailView):
    template_name = 'shop/detail.html'
    model = Detail


