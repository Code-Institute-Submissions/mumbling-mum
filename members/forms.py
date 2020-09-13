from django import forms
from .models import MemberProfile


class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and edit auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        # Update Form labels
        self.fields['default_phone_number'].label = 'Phone Number'
        self.fields['default_postcode'].label = 'Postal Code'
        self.fields['default_town_or_city'].label = 'Town or City'
        self.fields['default_street_address1'].label = 'Street Address 1'
        self.fields['default_street_address2'].label = 'Street Address 2'
        self.fields['default_county'].label = 'County'

        # Set Auto focus on Phone Number
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
      