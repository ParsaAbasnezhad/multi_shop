from enum import unique

from django.contrib.sites import requests

CART_SESSION_ID = 'caet'


class Cart:
    def __init__(self, request):
        self.session = requests.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            detail = detail.objects.get(id=item['id'])
            item['detail'] = detail
            item['total'] = int(item['quantity']) * int(item['detail'])
            item['unique_id'] = self.unique_id_generaton(detail.id, item['color'], item['size'])

            yield item

    def unique_id_generaton(self, id, color, size):
        result = f'{id}-{color}-{size}'
        return result

    def add(self, detail, quantity, size, color):
        unique = self.unique_id_generaton(detail.id, color, size)
        if unique in self.cart:
            self.cart[unique] = {'quantity': 0, 'price': str(detail.price), 'size': size, 'color': color, id: detail.id}

        self.cart['quantity'][unique] += int(quantity)

    def save(self):
        self.session.modified = True
