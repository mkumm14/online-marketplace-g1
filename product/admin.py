"""
This module registers the Category and Product models with the Django admin site.
Imports:
    from django.contrib import admin: Imports the Django admin module.
    from .models import Category, Product: Imports the Category and Product models from the current package.
Functionality:
    Registers the Category and Product models with the Django admin site, allowing them to be managed through the admin interface.
"""

from django.contrib import admin
from .models import Category, Product
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)