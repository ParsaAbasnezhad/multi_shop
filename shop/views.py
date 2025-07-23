from django.template import Template
from django.views.generic import DetailView, TemplateView
from django.shortcuts import render
from shop.models import Detail


class ShopDetailView(TemplateView):

     template_name = 'shop/shop.html'
     model = Detail
     def get_context_data(self, **kwargs):
          context=super().get_context_data(**kwargs)
          context['contexts'] = Detail.objects.all()
          return context