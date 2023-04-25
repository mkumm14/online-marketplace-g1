from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Discount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.DecimalField(max_digits=3, decimal_places=2)

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



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        if self.cart.discount:
            discount_amount = self.total_price * self.cart.discount.discount_percentage / 100
            self.discounted_price = self.total_price - discount_amount
        else:
            self.discounted_price = None
        super().save(*args, **kwargs)
