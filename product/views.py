from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, 'product/all_products.html', {'products':products})