from django.shortcuts import render,redirect
from .models import Cart,Customer,Product
from django.contrib.auth.models import User

# Create your views here.


# Create your views here.
def add_to_cart(request,id):
    # user = User.objects.get(username=request.user)
    # customer_object = Customer.objects.get(user=user.id)
    customer_object = Customer.objects.select_related('user').get(user=request.user)
    product_object = Product.objects.get(id=id)
    print(customer_object)
    item , create =Cart.objects.get_or_create(user=customer_object,product=product_object)
    if create:
        pass
    else:
        item.quantity+=1
        item.save()
    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)


def cart(request):
    user = User.objects.get(username=request.user)
    customer_object = Customer.objects.get(user_id=user)
    customer_object = Customer.objects.select_related('user').get(user=request.user)

    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)


def payment(request):
    print('this is payment view')
    return render(request,'cart/payment.html')

def remove_from_cart(request,id):
    customer_object = Customer.objects.get(user_id=request.user.id)
    product_object = Product.objects.get(id=id)
    item=Cart.objects.filter(user=customer_object,product=product_object)
    item.delete()
    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)


def clear_cart(request):
    customer_object = Customer.objects.get(user_id=request.user.id)
    cart = Cart.objects.filter(user=customer_object)
    cart.delete()
    return redirect('cart')
