from django import forms
from .models import Customer, CustomerDetails


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']


class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['address', 'phone_number']
