from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Category
from shop.models import Detail


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['product']= Detail.objects.all()
        return context


class CategoryListView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



