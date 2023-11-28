from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        # Exclude the 'created_at' field from the form
        exclude = ['created_at']

    # Customize the widgets for specific fields
    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        'quantity': forms.NumberInput(attrs={'min': 1}),
    }

    # Add any additional validation if needed
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return quantity
