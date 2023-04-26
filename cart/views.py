
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem, Discount
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
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
        'cart':cart
    }
    return render(request, 'cart/cart.html', context)



def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.user == cart_item.cart.user:
        cart_item.delete()
    return redirect('cart')


def increase_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.user == cart_item.cart.user:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def decrease_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.user == cart_item.cart.user:
        cart_item.quantity -= 1
        if cart_item.quantity == 0:
            cart_item.delete()
        else:
            cart_item.save()
    return redirect('cart')




def apply_discount(request):
    if request.method == "POST":
        discount_code = request.POST.get("discount_code")
        try:
            discount = Discount.objects.get(code=discount_code)
        except Discount.DoesNotExist:
            messages.error(request, "Invalid discount code.")
            return redirect('cart')

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.discount = discount
        cart.save()

        # Update cart items' discounted prices
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            item.update_discounted_price()
            item.save()

        messages.success(request, "Discount applied successfully.")
        return redirect('cart')
    else:
        return redirect('cart')
    

def remove_discount(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.discount = None
    cart.save()
            # Update cart items' discounted prices
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        item.update_discounted_price()
        item.save()

    messages.success(request, "Discount removed successfully.")
    return redirect('cart')