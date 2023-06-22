from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('register/', register),
    path('login/', login),
    path('shoplogin/', shoplogin),
    path('productdetails/', productdetails),
    path('productdisplay/', productdisplay),
    path('editproduct/<int:id>', editproduct),
    path('deleteproduct/<int:id>', deleteproduct),
    path('footer/', footer),
    path('userprofile/', userprofile),
    path('wishlist/<int:id>', wishlist),
    path('mywish/', mywish),
    path('removewish/<int:id>', removewish),
    path('cart/<int:id>', cart),
    path('mycart/', mycart),
    path('removecart/<int:id>', removecart),
    path('success/', success),
    path('wishlisttocart/<int:id>',wishlisttocart),
    path('buyproduct/<int:id>',buyproduct),
    # path('soldproducts/<int:id>',soldproducts),
    path('vieworder/',vieworder)

]
