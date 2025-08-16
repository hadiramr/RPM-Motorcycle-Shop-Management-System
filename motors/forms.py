from django import forms
from .models import Car, Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country', 'founded_year', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand name'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country'}),
            'founded_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter founded year'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter brand description'}),
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'name', 'model', 'year', 'price', 'mileage', 'fuel_type', 
                 'transmission', 'engine_size', 'description', 'image', 'is_available']
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car name'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car model'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter year'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price', 'step': '0.01'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter mileage'}),
            'fuel_type': forms.Select(attrs={'class': 'form-control'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
            'engine_size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter engine size', 'step': '0.1'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter car description'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make brand field required and add empty choice
        self.fields['brand'].empty_label = "Select a brand"
        self.fields['brand'].required = True
