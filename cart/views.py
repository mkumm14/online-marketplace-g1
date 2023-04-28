
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem, Discount, Order, ShippingAddress, Payment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal

from .forms import ShippingAddressForm, PaymentForm


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
        product = cart_item.product
        if product.quantity > cart_item.quantity:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.error(request, "Insuffucient stock.")
            return redirect('cart')
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




def checkout(request):
    if request.method == 'POST':
        address_form = ShippingAddressForm(request.POST, prefix='address')
        payment_form = PaymentForm(request.POST, prefix='payment')
        if address_form.is_valid() and payment_form.is_valid():
            shipping_address = address_form.save(commit=False)
            shipping_address.user = request.user
            shipping_address.save()

            payment = payment_form.save(commit=False)
            payment.user = request.user
            payment.save()

            user = request.user
            cart = Cart.objects.get(user=user)
            total_cost = cart.get_total_cost() * Decimal('1.0825')  # Add 8.25% sales tax

            order = Order.objects.create(user=user, shipping_address=shipping_address, payment=payment, total_cost=total_cost)
            
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                product = item.product
                product.quantity -= item.quantity
                product.save()

            # Clear the user's cart
            CartItem.objects.filter(cart=cart).delete()
            cart.discount = None
            cart.save()

            return redirect('order_success')
    else:
        address_form = ShippingAddressForm(prefix='address')
        payment_form = PaymentForm(prefix='payment')

    cart = Cart.objects.get(user=request.user)
    total_cost = cart.get_total_cost()
    total_price_with_tax = total_cost * Decimal('1.085')
    context = {
        'address_form': address_form,
        'payment_form': payment_form,
        'total_price_with_tax': total_price_with_tax,
    }   
    return render(request, 'checkout/checkout.html', context)


def order_success(request):
    return render(request, 'checkout/order_success.html')
