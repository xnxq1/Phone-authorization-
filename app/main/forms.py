
from django import forms
from django.contrib.auth.models import User

from .validators import validate_username
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
                               label='Номер телефона',
                               widget=forms.TextInput(attrs={'placeholder': '+79999999999'}),
                               validators=[validate_username])
    password = forms.CharField(max_length=100,
                               label='Пароль',
                               widget=forms.PasswordInput(attrs={'placeholder': 'пароль'}))




class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               label='Номер телефона',
                               widget=forms.TextInput(attrs={'placeholder': '+79999999999'}),
                               validators=[validate_username])
    password1 = forms.CharField(max_length=100, label='Пароль',
                               widget=forms.PasswordInput(attrs={'placeholder': 'пароль'}))
    password2 = forms.CharField(max_length=100, label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'placeholder': 'пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('Пароли не совпадают')

        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Такой пользователь уже существует')

        return username