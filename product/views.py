from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product
from .filters import ProductFilter

# Create your views here.




def product(request, pk):
    product = Product.objects.get(id=pk)

    return render(request, "product/product.html", {'product':product})