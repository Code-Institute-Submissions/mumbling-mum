from django import forms
from .models import Category, BlogEntry, Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__' #include all thefields

class BlogEntryForm(forms.ModelForm):
    class Meta:
        model=BlogEntry
        fields='__all__' #include all thefields

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__' #include all thefields
