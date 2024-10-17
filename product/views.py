from django.http import HttpResponse
"""
Views for handling product-related requests.
Functions:
    product(request, pk):
        Retrieves a product by its primary key (pk) and renders the product detail page.
        Also fetches up to 4 related products based on shared categories.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the product to retrieve.
        Returns:
            HttpResponse: The rendered product detail page with the product and related products.
"""
from django.shortcuts import render

from product.models import Product
from .filters import ProductFilter

# Create your views here.




def product(request, pk):
    product = Product.objects.get(id=pk)

    related_products = Product.objects.filter(categories__in=product.categories.all()).exclude(id=pk)[:4]

    return render(request, "product/product.html", {'product': product, 'related_products': related_products})