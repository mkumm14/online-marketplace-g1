
"""
URL configuration for the product app.
This module defines the URL patterns for the product-related views in the online marketplace project.
Routes:
    - '<int:pk>': Maps to the `product` view, expecting an integer primary key (pk) as a URL parameter.
                  The URL pattern is named 'product-page'.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>', views.product, name='product-page'),
]