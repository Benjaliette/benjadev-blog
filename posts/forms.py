from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget

from .models import Post

class PostForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput()
        }
