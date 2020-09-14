from django import forms 
from .models import Order

class OrderForm(forms.ModelForm):
    """Order form based on the Order model"""
    class Meta:
        model=Order
        fields=('full_name', 'email', 'phone_number', 
                'street_address1','street_address2', 
                'town_or_city', 'county', 
                'postcode', 'country',)
    
    def __init__(self, *args, **kwargs):
        """Add placeholders and classes, remove auto generated
        labels and set auto focus on first field"""
        # set up the form as it would be as default.
        super().__init__(*args, **kwargs)
        # declare the placeholders for the fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number' :'Phone Number', 
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City', 
            'county' : 'County',
            'postcode': 'Postal Code',
            'country' : 'Country',
        }

        # set the auto focus so the cursor is in the Full Name field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # iterate through the fields 
        for field in self.fields:# 
            # adding a * to the required fields placeholders
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder =  placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # add a class for the form fields
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # remove the labels as the placeholders are now set.
            self.fields[field].label = False

