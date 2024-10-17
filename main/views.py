from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from product.filters import ProductFilter

from product.models import Product
from .forms import RegisterForm, LoginForm


"""
This module contains views for the online marketplace application.
Functions:
    index(request):
        Renders the index page.
    home(request):
        Renders the home page with a list of products. Requires user to be logged in.
    login_view(request):
        Handles user login. Redirects authenticated users to the index page.
    store(request):
        Renders the store page.
    cart(request):
        Renders the cart page.
    checkout(request):
        Renders the checkout page.
    about(request):
        Renders the about page.
    register_view(request):
        Handles user registration. Redirects to the login page upon successful registration.
    logout_view(request):
        Logs out the user and redirects to the index page.
"""

def index(request):
    return render(request,'index.html')

@login_required
def home(request):
    products = Product.objects.all()
    product_filter=ProductFilter(request.GET, queryset=Product.objects.all())
    context={
        'form':product_filter.form,
        'products':product_filter.qs
    }
    return render(request, 'main/home.html', context)
    #return render(request, 'product/all_products.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:index')  # or whatever URL you want to redirect to

    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.success(request,"logged in successfully.")
                return redirect('main:home')  # or whatever URL you want to redirect to
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})

def store(request):
    context = {}
    return render(request, 'store/store.html', context)
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
def about(request):
    context = {}
    return render(request, 'index.html', context)



def register_view(request):

    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created successfully. Please log in.")
            return redirect('main:login')
    else:
        form=RegisterForm()

    return render(request, 'authentication/register.html',{'form':form})
    


def logout_view(request):
    logout(request)
    # messages.success(request, 'logged out successfully.')
    return redirect('main:index') 
