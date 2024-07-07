from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Supplier,Customer
class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25,widget=forms.PasswordInput)


# class RegisterCustomer(ModelForm,LoginForm):
#     username = forms.CharField(max_length=25)
#     password = forms.CharField(max_length=25,widget=forms.PasswordInput)
#     firstname = forms.CharField(max_length=20)
#     lastname = forms.CharField(max_length=20)
#     class Meta:
#         model = Customer
#         fields = '__all__'
#         exclude = ['user']
#     field_order = ['username','password', '__all__']
    
# class RegisterSupplier(ModelForm):
#     username = forms.CharField(max_length=25)
#     password = forms.CharField(max_length=25,widget=forms.PasswordInput)
#     firstname = forms.CharField(max_length=20)
#     lastname = forms.CharField(max_length=20)
#     class Meta:
#         model = Supplier
#         # fields = '__all__'
#         exclude = ['user']
#     field_order = ['username','password', '__all__']
        



def create_user_from_form(form):
    return User.objects.create_user(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],
        first_name=form.cleaned_data['firstname'],
        last_name=form.cleaned_data['lastname']
    )


class RegisterSupplier(ModelForm):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)

    class Meta:
        model = Supplier
        exclude = ['user']
    field_order = ['username','password','firstname','lastname', '__all__']
    
    def save(self, commit=True):
        user = create_user_from_form(self)
        supplier = super().save(commit=False)
        supplier.user = user
        if commit:
            supplier.save()
        return supplier

class RegisterCustomer(ModelForm):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)

    class Meta:
        model = Customer
        exclude = ['user','users_wishlist']
    field_order = ['username','password','firstname','lastname', '__all__']

    def save(self, commit=True):
        user = create_user_from_form(self)
        customer = super().save(commit=False)
        customer.user = user
        if commit:
            customer.save()
        return customer
