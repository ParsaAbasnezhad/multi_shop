from cart.cart_save import Cart
from cart.models import Order, DiscountCode
from shop.models import Detail
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        detail = get_object_or_404(Detail, id=pk)
        size = request.POST.get('size')
        color = request.POST.get('color')
        quantity = request.POST.get('quantity')
        if not size or not color or not quantity:
            messages.error(request, 'لطفاً همه گزینه‌ها را انتخاب کنید.')
            return redirect('shop:detail', pk=pk)
        cart = Cart(request)
        cart.add(detail, quantity, size, color)
        return redirect('cart:cart_detail')


class ApplyDiscountView(View):
    def post(self, request, pk):
        code = request.POST.get('code')
        order = get_object_or_404(Order, id=pk)
        discount_code = get_object_or_404(DiscountCode, name=code)
        if discount_code.quantity == 0:
            return redirect('cart:cart_detail',order.id)
        order.total_price -= discount_code.quantity * order.price
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect('cart:cart_detail',order.id)

