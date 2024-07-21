from django.shortcuts import render,redirect,get_object_or_404
from .forms import LoginForm,RegisterCustomer,RegisterSupplier
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.views import View
from django.http import HttpResponse
from .models import Customer,Supplier
# Create your views here.
class LoginView(View):
    def get(self,request,user_type):
        context={
            'form' :LoginForm(),
            'user_type':user_type,
        }
        return render(request,'account/login.html',context)
    def post(self,request,user_type):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
           
            u= get_object_or_404(User,username=username)
            if user_type == 'customer':
                if hasattr(u,'customer'):
                    request.session['user_type']='customer'
            elif user_type=='supplier':
                if hasattr(u,'supplier'):
                    request.session['user_type']='supplier'
            else:
                return HttpResponse('You are not Customer Nor Supplier')

                    
            user = authenticate(request,username=username,password=password)
            print(type(user))
            if user:
                login(request, user)
                return redirect('index')
            return redirect('login')
        else:
            return render(request,'account/login.html',{'form':form})


# def login_user(request):
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request,'account/login.html',{'form':form})

#     elif request.method=='POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form['username'].value()
#             password = form['password'].value()
#             user = authenticate(request,username=username,password=password)
#             print(type(user))
#             if user:
#                 login(request, user)
#                 return redirect('index')
#             return redirect('login')
#         else:
#             return render(request,'account/login.html',{'form':form})
def register_user(request):
    if request.method == 'GET':
        context={
            'form':1
        }
    return render(request,'account/test_register.html')
    
    
def logout_user(request):
    logout(request)
    return redirect('login','customer')
    

# def register_supplier(request):
#     if request.method=='GET':
#         context={
#             'form': RegisterSupplier()
#         }
#         return render(request,'account/test_register.html',context)
#     elif request.method=='POST':
#         form = RegisterSupplier(request.POST, request.FILES)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         if get_user_model().objects.filter(username=username).exists():
#             context={
#             'form': RegisterSupplier(request.POST, request.FILES)
#             }
#             return render(request,'account/test_register.html',context)
#         else:
#             user = get_user_model().objects.create_user(username=username, password=password,firstname=firstname,lastname=lastname) # Use create_user to handle password hashing     
#         if form.is_valid():
#             supplier = form.save(commit=False)
#             supplier.user = user
#             supplier.save()
#             return redirect('login')
#         else:
#             context={
#             'form': RegisterSupplier(request.POST,request.FILES)
#         }   
#         return render(request,'account/test_register.html',context)
   
# def register_customer(request):
#     if request.method=='GET':
#         pass
#     elif request.method=='POST':
#         pass

# # User.objects.all().values('username')



def register_user(request, user_type):
    if user_type not in ['supplier', 'customer']:
        return redirect('home')  # Redirect to a default page if user_type is invalid

    form_class = RegisterSupplier if user_type == 'supplier' else RegisterCustomer

    if request.method == 'GET':
        form = form_class()
        return render(request, 'account/register.html', {'form': form, 'user_type': user_type})
    
    elif request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(login)
        else:
            return render(request, 'account/register.html', {'form': form, 'user_type': user_type})




def choice(request,request_for):
    context={
        'request_for':request_for
    }
    return render(request,'account/choice.html',context)