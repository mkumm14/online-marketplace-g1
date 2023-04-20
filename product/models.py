from django.db import models

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