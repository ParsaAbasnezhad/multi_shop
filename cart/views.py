from django.shortcuts import render, redirect
from django.views import View


class CartDetailView(View):
    def get(self, request):
        return render(request, 'cart/cart.html', {})


class CartListView(View):
    def post(self, request):
        color ,size, quantity = request.POST.get('color'), request.POST.color('size'), request.POST.get('quantity')
        return redirect('cart:cart_detail')
