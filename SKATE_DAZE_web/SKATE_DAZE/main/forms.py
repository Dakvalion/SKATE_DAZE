from django import forms
from .models import *


class RegForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': "input", 'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'class': "input", 'placeholder': 'Телефон'}),
            'name': forms.TextInput(attrs={'class': "input", 'placeholder': 'Имя'}),
            'password1': forms.TextInput(attrs={'class': "input", 'placeholder': 'Пароль'}),
            'password2': forms.TextInput(attrs={'class': "input", 'placeholder': 'Пароль повторно'}),
        }


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = {'email', }
        widgets = {'email': forms.TextInput(
            attrs={'class': 'input', 'placeholder': 'email'})}
