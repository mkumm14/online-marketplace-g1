from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product
from .filters import ProductFilter

# Create your views here.




def product(request, pk):
    product = Product.objects.get(id=pk)

    related_products = Product.objects.filter(categories__in=product.categories.all()).exclude(id=pk)[:4]

    return render(request, "product/product.html", {'product': product, 'related_products': related_products})