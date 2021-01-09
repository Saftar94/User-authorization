from .models import Name, Arti
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ['title', 'password']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'О себе'
            }),


            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ArtiForm(ModelForm):
    class Meta:
        model = Arti

        fields = ['title', 'pasword', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название стати'
            }),

            'pasword': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс стати'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст стати'
            }),

            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
        }
