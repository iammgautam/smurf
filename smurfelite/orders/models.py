from django.db import models
# smurfelite
from users.models import Profile
from games.models import Product


class Cart(models.Model):
    customer = models.ForeignKey(Profile, related_name='cart', on_delete=models.SET_NULL, blank=True, null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    cart = models.ForeignKey(Cart,related_name="order_item", on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='order_item',on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
