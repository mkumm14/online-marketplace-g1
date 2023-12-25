import django_filters
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