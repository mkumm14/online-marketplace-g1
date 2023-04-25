from .models import Cart, CartItem

def cart_quantity(request):
    user = request.user
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitem_set.all()
        total_items = sum(item.quantity for item in cart_items)
    else:
        total_items = 0

    return {'cart_quantity': total_items}