from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Category


class HomePageView(TemplateView):
    template_name = 'home/index.html'



class CategoryListView(TemplateView):
    template_name = 'include/navbar.html'

    def get_context_data(self, **kwargs):
        context =super(CategoryListView,self).get_context_data()
        context['category'] = Category.objects.all()
        return context
