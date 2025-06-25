from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, Cart, CartItem

# Create your views here.

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    return render(request, 'orders/cart.html', {'items': items})
