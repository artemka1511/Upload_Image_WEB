from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class BaseRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(label='Электронная почта',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Введите Email'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]