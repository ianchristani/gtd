from django import forms
from .models import products_model

class products_form(forms.ModelForm):
    class Meta:
        model=products_model
        fields = ['name', 'price', 'amount', 'pic']