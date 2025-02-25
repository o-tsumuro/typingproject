from django.forms import ModelForm
from django import forms
from .models import Content, Category
from django.core.exceptions import ValidationError

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'sentence', 'category', 'is_public']
        widgets = {
            'category': forms.Select(choices=Category.objects.all())
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if Content.objects.filter(title=title).exists():
            raise ValidationError('このタイトルは既に使用されています。')
        return title