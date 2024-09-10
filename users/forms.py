from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginFrom(AuthenticationForm):

        class Meta:
        model = User
        firlds = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label = 'Имя Пользователя',
    #     widget=forms.TextInput(
    #         attrs={"autofocus": True,
    #         'class': 'form-control', 
    #         'placeholder': 'Введите имя пользователя',})
    #     )
    # password = forms.CharField(
    #     label = 'Пароль',
    #     widget = forms.PasswordInput(
    #         attrs={"autocomplete": "current-password", 
    #         'class': 'form-control', 
    #         'placeholder': 'Введите ваш пароль',}),
    # )
