from django import forms
from django.db import models
from django.db.models import fields
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name' , 'category' , 'quantity']
