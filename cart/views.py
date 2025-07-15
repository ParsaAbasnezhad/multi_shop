from cart.cart_save import Cart
from shop.models import Detail
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


class CartDetailView(View):
    def get(self, request):
        return render(request, 'cart/cart.html', {})


class CartAddView(View):
    def post(self, request, pk):
        detail = get_object_or_404(Detail, id=pk)
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        cart = Cart(request)
        cart.add(detail,size, color, quantity)
        return redirect('cart:cart_detail')
