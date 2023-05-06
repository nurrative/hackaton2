
import uuid

# from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from product.models import Product
from account.models import User


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts',blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def clear(self):
        pass


class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,  related_name='items' ,blank=True, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartitems',blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.IntegerField(default=1)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    cart =  models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='payments',blank=True, null=True)
    card_number = models.CharField(max_length=16) #min_length=16
    cvv = models.CharField(max_length=3)
    paid = models.BooleanField(default=False)





