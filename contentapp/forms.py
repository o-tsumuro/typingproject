from django.forms import ModelForm
from django import forms
from .models import Content

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'sentence', 'category', 'is_public']
        widgets = {
            'category': forms.Select(),
        }