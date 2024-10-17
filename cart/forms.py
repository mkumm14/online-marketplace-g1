from django import forms
"""
This module defines form classes for handling shipping addresses and payment information using Django's forms framework.
Classes:
    ShippingAddressForm (forms.ModelForm):
        A form for creating and updating ShippingAddress instances.
        Inherits from Django's ModelForm.
        Meta:
            model (ShippingAddress): The model associated with this form.
            fields (tuple): The fields to include in the form.
    PaymentForm (forms.ModelForm):
        A form for creating and updating Payment instances.
        Inherits from Django's ModelForm.
        Meta:
            model (Payment): The model associated with this form.
            fields (list): The fields to include in the form.
            widgets (dict): Custom widgets for form fields to provide placeholders.

"""
from .models import ShippingAddress, Payment

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'zip_code')

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'card_expiry', 'card_cvv']
        widgets = {
            'card_number': forms.TextInput(attrs={'placeholder': 'XXXX XXXX XXXX XXXX'}),
            'card_expiry': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
            'card_cvv': forms.TextInput(attrs={'placeholder': 'XXX'})
        }
