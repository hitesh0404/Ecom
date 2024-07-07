from django.db import models
from django.contrib.auth.models import User
from account.models import Address
from payment.models import Payment
from product.models import Product
# Create your models here.
ORDER_STATUS_CHOICES = [
    ('placed', 'placed'),
    ('shipped', 'shipped'),
    ('delivered', 'delivered'),
    ('cancelled', 'cancelled'),
    ('returned', 'returned'),
]
class OrderStatus(models.Model):
    info = models.CharField(choices=ORDER_STATUS_CHOICES,max_length=20)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.info + " " + str(self.updated_at.date()) +" "+ str(self.updated_at.time())
SHIPPING_METHOD_CHOICES = (
    ('standard', 'Standard Shipping'),
    ('express', 'Express Shipping'),
    ('overnight', 'Overnight Shipping'),
    ('pickup', 'In-Store Pickup'),
    ('courier', 'Courier Service'),
    ('international', 'International Shipping'),
) 
SHIPPING_CHARGES_CHOICES = {
    'standard':100,
    'express':200,
    'overnight':500,
    'pickup':0,
    'courier':700,
    'international':10000,
}
class Shipping(models.Model):
    method = models.CharField(choices=SHIPPING_METHOD_CHOICES,max_length=20)
    charges = models.IntegerField(default=0)
    def save(self,*args,**kwargs):
        self.charges = SHIPPING_CHARGES_CHOICES[self.method]
        super(Shipping,self).save(*args,**kwargs)
    def __str__(self) -> str:
        return self.method +' ' + str(self.charges)
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date_time = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address,on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(Payment,on_delete=models.DO_NOTHING,null=True,blank=True)
    order_status = models.OneToOneField(OrderStatus,on_delete=models.DO_NOTHING)
    shipping = models.ForeignKey(Shipping,on_delete=models.DO_NOTHING)

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2,max_digits=6)
    class Meta:
        unique_together = (('order', 'product'))

from payment.models import PAYMENT_STATUS_CHOICE
class Refund(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True, blank=True)
    status = models.CharField(choices=PAYMENT_STATUS_CHOICE,max_length=20, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    raised_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    settled_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"Order ID: {self.order}, Status: {self.status}"
