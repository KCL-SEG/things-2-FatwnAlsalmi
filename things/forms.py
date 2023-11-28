from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        exclude = ['created_at']

    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 15, 'maxlength': 120}),
        'quantity': forms.NumberInput(attrs={'min': 0, 'max': 100}),
    }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0 or quantity > 100:
            raise forms.ValidationError("Quantity must be between 0 and 100.")
        return quantity
