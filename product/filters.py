import django_filters
"""
This module defines filters for the Product model using django_filters.
Classes:
    ProductFilter: A FilterSet class for filtering Product instances based on price range and categories.
Filters:
    - price: A RangeFilter for filtering products within a specified price range.
    - categories: A ModelMultipleChoiceFilter for filtering products by categories, using checkboxes for selection.
Meta:
    - model: Specifies the Product model to be filtered.
    - fields: Defines the fields that can be filtered, including:
        - 'name': Allows filtering by product name using case-insensitive containment.
        - 'categories': Allows filtering by exact category match.
"""
from .models import Product,Category
from django import forms





class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    categories = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Product
        fields={
            'name':['icontains'],
            'categories':['exact']
        }

