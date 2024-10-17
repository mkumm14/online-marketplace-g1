from django.db import models
"""
This module defines the models for the cart application, including Discount, Cart, CartItem, ShippingAddress, Payment, and Order.
Classes:
    Discount: Model for discount codes. Has a code and discount percentage.
    Cart: Model for cart. Has a user, items, and discount. Items are linked to the cart through the CartItem model.
    CartItem: Model for cart items. Has a product, cart, quantity, total price, and discounted price.
    ShippingAddress: Model for shipping address. Has a user, address line 1, address line 2, city, state, and zip code.
    Payment: Model for payment. Has a user, card number, card expiry, and card cvv.
    Order: Model for order. Has a user, shipping address, payment, total cost, and created_at timestamp.
Methods:
    Discount.__str__: Returns the discount code as a string.
    Cart.get_total_cost: Calculates and returns the total cost of the cart, considering discounts.
    Cart.__str__: Returns a string representation of the cart, including the user's name.
    CartItem.save: Overrides the save method to calculate the total and discounted prices before saving.
    CartItem.update_discounted_price: Updates the discounted price based on the cart's discount.
    ShippingAddress.__str__: Returns a string representation of the shipping address.
    Payment.__str__: Returns a string representation of the payment, showing the last four digits of the card number.
    Order.__str__: Returns a string representation of the order, including the order ID and user's username.
"""
from django.contrib.auth.models import User
from product.models import Product

class Discount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.code


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)

    def get_total_cost(self):
        cart_items = self.cartitem_set.all()
        total_cost = sum(item.discounted_price or item.total_price for item in cart_items)
        return total_cost
    
    def __str__(self):
        return f"{self.user}'s cart"



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        self.update_discounted_price()
        super().save(*args, **kwargs)

    def update_discounted_price(self):
        if self.cart.discount:
            discount_amount = self.total_price * self.cart.discount.discount_percentage / 100
            self.discounted_price = self.total_price - discount_amount
        else:
            self.discounted_price = None


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.state}, {self.zip_code}"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=19)
    card_expiry = models.CharField(max_length=7)
    card_cvv = models.CharField(max_length=4)

    def __str__(self):
        return f"Card ending in {self.card_number[-4:]}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)  


    def __str__(self):
        return f"Order {self.pk} by {self.user.username}"
