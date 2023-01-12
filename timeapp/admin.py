from django.contrib import admin
from timeapp.models import *


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug' : ('productname',)}
    


class CartAdmin(admin.ModelAdmin):
    list_display =('cart_id','date_added')

class CartItemAdmin(admin.ModelAdmin):
    list_display =('product','cart','quantity','is_active')

admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartItemAdmin)