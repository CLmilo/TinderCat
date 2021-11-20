from django.shortcuts import render

def inicio(request):
    return render(request, 'Front/index.html')
    
def register(request):
    return render(request, 'Front/register.html')

def login(request):
    return render(request, 'Front/login.html')

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