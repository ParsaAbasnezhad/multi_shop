from django.template.context_processors import request
from django.template import Template
from django.views.generic import DetailView, TemplateView, ListView
from django.shortcuts import render
from shop.models import Detail


class ShopDetailView(TemplateView):
    template_name = 'shop/shop.html'
    model = Detail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contexts'] = Detail.objects.all()
        return context


class ProductListView(ListView):
    template_name = 'shop/shop.html'
    queryset = Detail.objects.all()

    def get_context_data(self, **kwargs):
        request = self.request
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        min_price = request.GET.getlist('min_price')
        max_price = request.GET.getlist('max_price')
        queryset = Detail.objects.all()

        if colors:
            queryset = queryset.filter(color__title__in=colors).distinct()
        if sizes:
            queryset = queryset.filter(size__title__in=sizes).distinct()
        if min_price and max_price:
            queryset = queryset.filter(price__lte=max_price, price__gte=min_price)
        context = super(ProductListView, self).get_context_data()
        context['objects_list'] = queryset



def new_product_view(request):
    new_product = Detail.objects.order_by('created_at')[:10]
    return render(request, 'home/index.html', {'product': new_product})
