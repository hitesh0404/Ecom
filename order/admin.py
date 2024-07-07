from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderStatus)
admin.site.register(Shipping)
admin.site.register(Refund)

