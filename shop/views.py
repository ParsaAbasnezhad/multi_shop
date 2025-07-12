from django.views.generic import TemplateView ,ListView
from django.shortcuts import render
from .models import ShopList


class ShopListView(ListView):
    model = ShopList
    template_name = 'shop/shop.html'
    context_object_name = 'shop_list'
    paginate_by = 2



