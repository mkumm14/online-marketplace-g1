from django.db import models
"""
This module defines the models for the product application in the online marketplace project.
Classes:
    Category(models.Model): Represents a category for products.
        Attributes:
            name (CharField): The name of the category.
        Methods:
            __str__(): Returns the name of the category.
    Product(models.Model): Represents a product in the marketplace.
        Attributes:
            name (CharField): The name of the product.
            description (TextField): A detailed description of the product.
            image (ImageField): An image of the product, uploaded to the 'products/' directory.
            price (DecimalField): The price of the product, with a maximum of 7 digits and 2 decimal places.
            quantity (PositiveIntegerField): The available quantity of the product.
            categories (ManyToManyField): The categories to which the product belongs.
        Methods:
            __str__(): Returns the name of the product.
"""
from django.contrib.auth.models import User

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


