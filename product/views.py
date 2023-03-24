from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def products(request):
    return HttpResponse('products page')