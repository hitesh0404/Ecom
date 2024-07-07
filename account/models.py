from django.db import models
from product.models import Product 
from django.contrib.auth.models import User

gender_choise=(
    ('M','male'),
    ('F','female'),
)
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    flat_shop_number = models.CharField(max_length=100)
    building_name = models.CharField(max_length=100)
    area_street = models.CharField(max_length=100)
    near_by = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.title + ' of user ' + self.user.first_name
    
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    users_wishlist = models.ManyToManyField(Product,through='Wishlist', blank=True)
    phone_number = models.BigIntegerField(blank=False,null=False)
    profile_image = models.ImageField(upload_to='profile_image/',default='no image')
    dob = models.DateField(null=False)
    gender = models.CharField(choices=gender_choise,max_length=20)

    def __str__(self):
        return self.user.first_name
    
class Supplier(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    company_name = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)
    phone_number = models.BigIntegerField(blank=False,null=False)
    company_logo = models.ImageField(upload_to='logo/',default='no image')
    dob = models.DateField(null=False)
    gender = models.CharField(choices=gender_choise,max_length=20)
    document_photo = models.ImageField(upload_to='documents',default='no image')
    def __str__(self):
        return self.user.first_name

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.user.first_name + ' wish for ' + self.product
  
class Review(models.Model):
    rating = models.IntegerField()
    review_text = models.TextField()
    date_of_review = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.user.first_name + ' rated '+ str(self.rating) + ' to Product ' + self.product.name




from ckeditor.fields import RichTextField
from django.utils.html import strip_tags


class Carousel(models.Model):
    image=models.ImageField(upload_to='carousel/',default='online-shopping-background-website-mobile-app_269039-166.jpg')
    title=RichTextField()
    description=RichTextField()
    def __str__(self) :
        return strip_tags(self.title)