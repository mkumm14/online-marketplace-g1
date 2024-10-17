from django.urls import path
from . import views


"""
URL configuration for the cart application.
This module defines the URL patterns for the cart-related views in the online marketplace project.
Routes:
- '' : Displays the cart page.
- 'add_to_cart/<int:product_id>/' : Adds a product to the cart.
- 'remove_from_cart/<int:cart_item_id>/' : Removes an item from the cart.
- 'increase_cart_item/<int:cart_item_id>/' : Increases the quantity of a cart item.
- 'decrease_cart_item/<int:cart_item_id>/' : Decreases the quantity of a cart item.
- 'apply_discount/' : Applies a discount to the cart.
- 'remove_discount/' : Removes a discount from the cart.
- 'checkout/' : Initiates the checkout process.
- 'order_success/' : Displays the order success page.
- 'order_history/' : Displays the order history page.
"""




urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
     path('increase_cart_item/<int:cart_item_id>/', views.increase_cart_item, name='increase_cart_item'),
    path('decrease_cart_item/<int:cart_item_id>/', views.decrease_cart_item, name='decrease_cart_item'),
    path('apply_discount/', views.apply_discount, name='apply_discount'),
        path('remove_discount/', views.remove_discount, name='remove_discount'),
           path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
        path('order_history/', views.order_history, name='order_history'),




]