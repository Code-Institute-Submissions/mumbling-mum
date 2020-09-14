from django import forms
from .models import Item, Category

class ItemForm(forms.ModelForm):
    """Item form used to input new store items and edit current ones """
    class Meta:
        model=Item
        fields='__all__' #include all thefields

class CategoryForm(forms.ModelForm):
    """Category form used to input new categories and edit current ones"""
    class Meta:
        model=Category
        fields='__all__' #include all thefields
