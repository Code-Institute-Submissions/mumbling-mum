from django import forms
from .models import Category, BlogEntry, Comment
from crispy_forms.helper import FormHelper

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
        unlabelled_fields = ('body',) # Remove body label 
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        for field in CommentForm.Meta.unlabelled_fields:
            self.fields[field].label = False
