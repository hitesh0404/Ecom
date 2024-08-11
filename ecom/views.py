from django.http import HttpResponse
from django.shortcuts import render,redirect

from account.models import Carousel
from product.models import Product  
            #
def home(request):
    # return HttpResponse("Hello world")
    # content={'name':'ItVedant'}
    data=Carousel.objects.all()
    total = range(data.count())
    products = Product.objects.all()[:3]       #
    context={
        'car':data,
        'n':total,
        'p':products                            #
    }
    
    # print(Carousel.objects.get(id =1).get('image'))
    return render(request,'index.html',context)

def about_us(request):
    return render(request,'about_us.html')

def contact_us(request):
    return render(request,'contact_us.html')




from .forms import LoginForm

def form(request):
    return render(request, 'form.html',{'form':LoginForm()})