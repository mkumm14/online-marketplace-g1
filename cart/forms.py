from django import forms
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
