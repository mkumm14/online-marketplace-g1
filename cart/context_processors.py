from .models import Cart, CartItem
"""
Context processor to add the total quantity of items in the user's cart to the context.
Functions:
    cart_quantity(request): Returns a dictionary with the total quantity of items in the user's cart.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        dict: A dictionary containing the total quantity of items in the user's cart under the key 'cart_quantity'.
"""

def cart_quantity(request):
    user = request.user
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitem_set.all()
        total_items = sum(item.quantity for item in cart_items)
    else:
        total_items = 0

    return {'cart_quantity': total_items}