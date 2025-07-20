from django.db import models

from account.models import User
from shop.models import Detail


# products that the user must register
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user


# Products registered by the user
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # profition
    product = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=11)
    color = models.CharField(max_length=11)
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.order


class DiscountCode(models.Model):
    name = models.CharField(max_length=20)
    discount = models.PositiveIntegerField(default=0, unique=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
