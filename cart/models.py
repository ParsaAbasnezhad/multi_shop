from django.db import models

from account.models import User
from shop.models import Detail


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=20,blank=True,null=True)
    phone = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email_or_phone



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Detail, on_delete=models.CASCADE)
    size = models.CharField(max_length=11)
    color = models.CharField(max_length=11)
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.order.user
