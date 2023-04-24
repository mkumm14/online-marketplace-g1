
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem

# Create your views here.


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # Replace with the URL of your cart view



def cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = CartItem.objects.filter(cart=cart)

    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart/cart.html', context)
