from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Wishlist)
admin.site.register(Review)
admin.site.register(Carousel)