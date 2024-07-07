from django.urls import path
from . import views
urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.payment,name='checkout'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='add-to-cart'),
    path('remove_from_cart/<int:id>',views.remove_from_cart,name='remove-from-cart'),
    path('clear_cart',views.clear_cart,name='clear-cart')   
]

