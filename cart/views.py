from django.http import HttpResponseBadRequest
from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart,Customer,Product
from django.contrib.auth.models import User
from order.models import Order,OrderItem
from account.models import Address
from django.contrib import messages 
from django.views.decorators.csrf import csrf_exempt
import razorpay
from payment.models import Payment


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
    # user = User.objects.get(username=request.user)
    # customer_object = Customer.objects.get(user_id=user)
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
    customer_object = Customer.objects.select_related('user').get(user=request.user)
    product_object = get_object_or_404(Product,id=id)
    item=Cart.objects.filter(user=customer_object,product=product_object)
    item.delete()
    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)


def clear_cart(request):
    customer_object = Customer.objects.select_related('user').get(user=request.user)
    cart = Cart.objects.filter(user=customer_object)
    cart.delete()
    return redirect('cart')


def increase_quantity(request,id):
    customer_object = Customer.objects.select_related('user').get(user=request.user)
    product_object = Product.objects.get(id=id)
    item=get_object_or_404(Cart,user=customer_object,product=product_object)
    item.quantity+=1
    item.save()
    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)

def decrease_quantity(request,id):
    customer_object = Customer.objects.select_related('user').get(user=request.user)
    product_object = Product.objects.get(id=id) 
    item=get_object_or_404(Cart,user=customer_object,product=product_object)
    if item.quantity>1:
        item.quantity-=1
        item.save()
    else:
        item.delete()
    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)
from order.models import OrderStatus,Shipping
import uuid
from django.conf import settings
def checkout(request):
    if request.method == 'POST':
        customer_object = Customer.objects.select_related('user').get(user=request.user)
        cart = Cart.objects.filter(user=customer_object)
        
        add_id = request.POST.get('address')
        address = Address.objects.get(id = add_id)
        order_status = OrderStatus.objects.get(id= 1)
        shipping = Shipping.objects.get(id= 1)

        order = Order(
            uuid= str(uuid.uuid4().hex),                #
            user=customer_object.user,
            address = address,
            order_status = order_status,
            shipping=shipping,
            amount = 0  )
        order.save()       
        total =0                     
        for item in cart:
                price= Product.objects.get(id = item.product.id).price
                total = total + (item.quantity * price)
                order_item_obj = OrderItem(order=order,product=item.product,quantity = item.quantity)
                order_item_obj.save()
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        data = { "amount":int(total)*100, "currency": "INR", "receipt": order.uuid  }      #
        payment = client.order.create(data=data)
        order.payment_id = payment.get('id')                  #
        order.amount=total                           
        order.save()                                
        return render(request,'cart/payment.html',{'total': total,'payment':payment})
    else:
        address = Address.objects.filter(user=request.user)
        if not address:
            messages.error('please add atleast one address into your profile')
            return redirect('home')
        return render(request,'cart/checkout.html',{'address':address})
 
@csrf_exempt
def success(request):
    if request.method=='POST':
        try:
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            client.utility.verify_payment_signature({
                'razorpay_order_id': request.POST.get("razorpay_order_id"),
                'razorpay_payment_id':request.POST.get("razorpay_payment_id"),
                'razorpay_signature': request.POST.get("razorpay_signature")
            })
            order = Order.objects.get(payment_id=request.POST.get('razorpay_order_id'))
            amount = order.amount
            # order.order_status = OrderStatus.objects.get(id=2)
            order.save()
            user_obj = User.objects.get(username=request.user)
            Payment.objects.create(
                user=user_obj,
                payment_id = request.POST.get("razorpay_payment_id"),
                payment_signature= request.POST.get('razorpay_signature'),
                amount = amount / 100,  
                status='completed',
                method='Razorpay',
                order=order
            )
            cust_obj = Customer.objects.get(user = user_obj)
            cart_obj = Cart.objects.filter(user=cust_obj)
            cart_obj.delete()
            return render(request, 'cart/success.html')
        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest("Signature verification failed")
    
    return HttpResponseBadRequest("Invalid request")


       
       
            

            
         
        
    