from django.db import models

ELECTRONICS = 'ELECTRONICS'
CLOTHING = 'CLOTHING'
BOOKS = 'BOOKS'
HOME_APPLIANCES = 'HOME_APPLIANCES'
BEAUTY = 'BEAUTY'
SPORTS_AND_OUTDOORS = 'SPORTS_AND_OUTDOORS'
TOYS_AND_GAMES = 'TOYS_AND_GAMES'
FOOD_AND_GROCERY = 'FOOD_AND_GROCERY'
OTHER = 'OTHER'
CATEGORY_CHOICES = [
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (BOOKS, 'Books'),
        (HOME_APPLIANCES, 'Home Appliances'),
        (BEAUTY, 'Beauty'),
        (SPORTS_AND_OUTDOORS, 'Sports & Outdoors'),
        (TOYS_AND_GAMES, 'Toys & Games'),
        (FOOD_AND_GROCERY, 'Food & Grocery'),
        (OTHER,'Other')
    ]
  
class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    def __str__(self) -> str:
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    description = models.TextField()
    def __str__(self) -> str:
        return self.name
# Create your models here.
class Product(models.Model):
    name =  models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    size = models.DecimalField(decimal_places=2,max_digits=4)
    description = models.CharField(max_length=500)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/product_image',default='images/product_image/p1.jpeg')
    category = models.ManyToManyField(Category)
    weight = models.DecimalField(decimal_places=2,max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)
    def __str__(self) -> str:
        return "name is {} and Price is {} $".format(self.name,self.price)