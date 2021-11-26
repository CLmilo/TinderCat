from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    email = forms.CharField(label='Correo Electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'fecha_nacimiento']
        help_texts = {k:"" for k in fields}

class InicioForm(UserCreationForm):
    email = forms.CharField(label='Correo Electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']
        help_texts = {k:"" for k in fields}