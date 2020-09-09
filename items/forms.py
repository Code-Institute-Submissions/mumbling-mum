from django import forms
from .models import Item, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__' #include all thefields

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__' #include all thefields
