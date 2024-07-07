from django.db import models
from account.models import Customer
from product.models import Product


class Cart(models.Model):
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.user.user.username + ' added ' + self.product.name
    class Meta:
        unique_together=(('user','product'))