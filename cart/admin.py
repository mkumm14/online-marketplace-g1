from django.contrib import admin
from .models import Discount, Cart, CartItem,Order,Payment,ShippingAddress
# Register your models here.

admin.site.register(Discount)
admin.site.register(Payment)
admin.site.register(ShippingAddress)
admin.site.register(CartItem)
admin.site.register(Order)

