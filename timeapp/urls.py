from django.urls import path
from timeapp import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('product-details/<slug:slug>/',views.product_details,name="product-details"),
    path('cart',views.cart,name='cart'),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('logout/',views.logoutuser,name='logout'),
]
