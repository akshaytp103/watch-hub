
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Product,Cart,CartItem
from django.contrib.auth import logout

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'main/index.html',context)
    
        
def product_details(request,slug):
    item =Product.objects.filter(slug=slug)
    context= {'items':item}
    return render(request,'main/product_details.html',context)

def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
        print(9999999999,cart)
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if not request.method == 'POST':
        return redirect('login')
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    print(1212121212121,cart)
    try:
        cart_item = CartItem.objects.filter(product=product,quantity=1,cart=cart)
        # cart_item.quantity += 1
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,
                                            cart=cart, quantity=1)
    cart.save()
    print(1111111111111)
    return redirect('cart')



def cart(request,total=0,quantity=0,cart_items=None):

    try:
        
        grand_total= 0

        if request.user.is_authenticated:
            cart_items=CartItem.objects.filter(is_active=True)

        else:    
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cart_items=CartItem.objects.get(cart=cart,is_active=True)
            print(55555,cart_items)
        for cart_item in cart_items:
            total +=(cart_item.product.price * cart_item.quantity)
            quantity +=cart_item.quantity
        
        grand_total= total
            
    except ObjectDoesNotExist:
        pass      



    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,      
        'grand_total' : grand_total,
    } 
    print(33333333)
    return render(request,'main/cart.html',context)




def logoutuser(request):
    logout(request)
    return redirect('/')