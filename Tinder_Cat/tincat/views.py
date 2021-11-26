from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate
from .forms import RegistroForm
from django.contrib import messages

def inicio(request):
    return render(request, 'Front/index.html')
    
def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = RegistroForm()
    
    context = { 'form' : form }
    return render(request, 'Front/register.html', context)

def perfil(request):
    return render(request, 'Front/perfil.html')

def miperfil(request):
    return render(request, 'Front/miperfil.html')

def principal(request):
    return render(request, 'Front/principal.html')

def chat(request):
    return render(request, 'Front/chat.html')

def baneo(request):
    return render(request, 'Front/baneo_usuario.html')