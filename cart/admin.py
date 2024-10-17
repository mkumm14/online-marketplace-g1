from django.contrib import admin
"""
This module registers the models for the admin interface of the online marketplace application.
Modules:
    admin (django.contrib.admin): The Django admin module.
    models (cart.models): The models module containing the Discount, Cart, CartItem, Order, Payment, and ShippingAddress models.
Registered Models:
    - Discount: Represents discount information.
    - Payment: Represents payment information.
    - ShippingAddress: Represents shipping address information.
    - Order: Represents order information.
"""
from .models import Discount, Cart, CartItem,Order,Payment,ShippingAddress
# Register your models here.

admin.site.register(Discount)
admin.site.register(Payment)
admin.site.register(ShippingAddress)
admin.site.register(Order)

