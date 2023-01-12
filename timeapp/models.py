from django.db import models
from .models import *

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=50,null=False)
    strapcolor = models.CharField(max_length=50,null=False)
    price=models.FloatField()
    image=models.ImageField(upload_to="images/product")
    slug         = models.SlugField(max_length=200,db_index=True)
    
    
    def __str__(self):
        return self.productname
    


class Cart(models.Model):

    cart_id    = models.CharField(max_length=250,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart    = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,blank=True) 
    quantity =models.IntegerField()   
    is_active = models.BooleanField(default=True) 