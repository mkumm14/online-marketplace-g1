from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product
from .filters import ProductFilter

# Create your views here.

def products(request):
    products = Product.objects.all()
    product_filter=ProductFilter(request.GET, queryset=Product.objects.all())
    context={
        'form':product_filter.form,
        'products':product_filter.qs
    }
    return render(request, 'product/all_products.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)

    return render(request, "product/product.html", {'product':product})