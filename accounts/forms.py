from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise ValidationError("パスワードは8文字以上にしてください。")
        return password

    def clean_username(self):
        username = self.cleaned_data('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('このユーザーネームは既に使用されています。')
        return username