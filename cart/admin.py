from django.contrib import admin
from .models import Order, DiscountCode
from .models import OrderItem
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(DiscountCode)

