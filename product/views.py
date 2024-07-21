from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForm
import os
from .models import Product,Category,Brand

# Create your views here.
# '''
# def home(request):
#     data='ITVEDANT'
    
#     if os.path.exists('product/templates/product/home.html'):
#             file=open('product/templates/product/home.html', 'rb')
#             response = FileResponse(file)
#             response['Content-Disposition'] = 'attachment; filename="your_file_name.html"'
#             return response
#     else:
#         # Handle the case where the file does not exist
#         return HttpResponse("File not found", status=404)
#     # return FileResponse(request,open(''))

# '''
# def home(request):
#     from django.template.loader import render_to_string

#     def generate_html_file():
#         data = {
#         'name': 'Alice',
#         'age': 30,
#         }
#         rendered_html = render_to_string('product/home.html', data)
    
#         return rendered_html
#     from django.http import HttpResponse

    
#     rendered_html = generate_html_file()

#     response = HttpResponse(rendered_html, content_type='text/html')
#     response['Content-Disposition'] = 'attachment; filename="output.html"'

#     return response

def show_product(request):
    # name="ITVedant"
    p=Product.objects.all() #select * from Product
    categories = Category.objects.all()
    context = {
        'products':p,
        'categories':categories
    }
    return render(request,"product/products.html",context)

def filter_product_by_category(request,name):
    category = get_object_or_404(Category,name=name)  #electronic
    products = category.product_set.all()             #product which comes under electronic
    categories = Category.objects.all()                # all category
    brands = {i.brand.name for i in products.select_related('brand')}  #all the brand of filtered product 

    context = {
        'products':products,
        'category':category,
        'categories':categories,
        'brands':brands
        }
    return render(request,"product/products.html",context)
def filter_product_by_brand(request,name,category):
    pass
#     # brand = get_object_or_404(Brand,name=name)
#     category = get_object_or_404(Category,name=name)
#     products = category.product_set.all()
#     context = {
#         'products':products,
#         'category':category,
#         'categories':categories
#         }
#     return render(request,"product/products.html",context)
def add_product(request):
    if request.method == 'GET':
        context={
            'form' : ProductForm()
        }
        return render(request,'product/add_product.html',context)
    elif request.method == 'POST':
        print(request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-product')
        else:
            context={
            'form' : ProductForm(request.POST)
        }
        return render(request,'product/add_product.html',context)
        #    return redirect('add-product')

        

def show_details(request,id):
    p = get_object_or_404(Product,id=id)
    context = {
        'product':p
    }
    return render(request,'product/product_detail.html',context)

def remove_product(request,id):
    p = get_object_or_404(Product,id=id)
    p.delete()
    return redirect('show-product')


from django.views import View
class AddProduct(View):
    def get(self,request):
        context={
            'form' : ProductForm()
        }
        # print('here is information',type(request.POST),type(get_object_or_404(Product,id=5)))
        return render(request,'product/add_product.html',context)
    def post(self,request):
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show-product')
        else:
            context = {
                'form':form
            }
        return render(request,'product/add_product.html',context)



class UpdateProduct(View):
    def get(self,request,id):
        data=get_object_or_404(Product,id=id)
        context ={
            'form':ProductForm(instance=data)
        }
        return render(request,'product/update_product.html',context)
    def post(self,request,id):
        product = get_object_or_404(Product,id=id)
        form = ProductForm(request.POST,instance=product)
        if form.is_valid:
            form.save()
            return redirect('about-product',id)
        else:
            context ={
            'form':ProductForm(request.POST)
        }
        return render(request,'product/update_product.html',context)
    