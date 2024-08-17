from django.shortcuts import render,redirect,get_object_or_404
from .forms import LoginForm,RegisterCustomer,RegisterSupplier
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.views import View
from django.http import HttpResponse
from .models import Customer,Supplier
from django.contrib import messages
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
            messages.error(request,'wrong Credentials')
            return choice(request,'login')
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

from random import randint
def generate_otp(request):
    otp = randint(1000,9999)
    request.session['otp']=str(otp)
    print(otp)
    request.session['attempts']='3'

class ResetPassword(View):
    def get(self, request):
        username = request.GET.get('username')
        user = get_object_or_404(User,username = username )
        # user = User.objects.filter(username=username)
        # if user:
        #     # token = PasswordResetTokenGenerator().make_token(user[0])
        #     # email = EmailMessage('Reset Password', f'Your reset password token is {token}', to
        #     #                      [user[0].email])
        #     # email.send()
        #     user = user[0]
        # else:
        #     messages.error(request,"something Went Wrong")
        #     return choice(request,'login')
        request.session['username']=user.username
        
        if user.email :
            request.session['email']=user.email
            return render(request,'account/verify_email.html')
        else:
            messages.error(request,"Can't procced with this username provided by you")
            return choice(request,'login')
    def post(self,request):
        email=request.session.get('email')
        user_provided_email = request.POST.get('email')
        if user_provided_email == email:
            generate_otp(request)
            return render(request,'account/verify_otp.html')
        else:
            messages.error(request,"Can't procced with this username provided by you")
            return choice(request,'login')


def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp == request.session.get('otp'):
            return render(request,'account/change_password.html')
        elif  int(request.session['attempts'])>1 :
            request.session['attempts']=str(int(request.session['attempts'])-1)
            return render(request,'account/verify_otp.html')
        else:
            messages.error(request,"Something Went Wrong")
            return choice(request,'login')
            

def change_password(request):
    username = request.session['username']
    if request.method == 'POST' and username:
        password = request.POST.get('new_password')
        user = get_object_or_404(User,username=username)
        user.set_password(password)
        print(password)
        user.save()
        messages.success(request,"Password Reset Successfully")
        return choice(request,'login')
    else:
        messages.error(request, "Invalid OTP")
        return choice(request,'login')
    