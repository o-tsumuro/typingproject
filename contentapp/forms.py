from django.forms import ModelForm
from django import forms
from .models import Content, Category

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'sentence', 'category', 'is_public']
        widgets = {
            'category': forms.Select(choices=Category.objects.all())
        }