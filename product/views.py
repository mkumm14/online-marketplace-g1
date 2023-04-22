from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product


# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, 'product/all_products.html', {'products': products})


def product(request, pk):
    product = Product.objects.get(id=pk)

    return render(request, "product/product.html", {'product': product})


def cart(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=user.name, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=user.name, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)
