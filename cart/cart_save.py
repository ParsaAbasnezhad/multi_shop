from shop.models import Detail

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            detail_obj = Detail.objects.get(id=item['id'])
            item['detail'] = detail_obj
            item['total'] = int(item['quantity']) * int(detail_obj.price)
            item['unique_id'] = self.unique_id_generaton(detail_obj.id, item['color'], item['size'])
            yield item

    def unique_id_generaton(self, id, color, size):
        result = f'{id}-{color}-{size}'
        return result

    def add(self, detail, quantity, size, color):
        unique = self.unique_id_generaton(detail.id, color, size)
        if unique not in self.cart:
            self.cart[unique] = {
                'id': detail.id,
                'quantity': 0,
                'price': str(detail.price),
                'size': size,
                'color': color
            }
        self.cart[unique]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True


    def total(self):
        cart = self.cart.values()
        total = sum(int(item['price'])  * int(item['quantity']) for item in cart)
        return total