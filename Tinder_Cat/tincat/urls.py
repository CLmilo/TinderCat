from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', LoginView.as_view(template_name='Front/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('perfil/', views.perfil, name='perfil'),
    path('miperfil/', views.miperfil, name='miperfil'),
    path('principal/', views.principal, name='principal'),
    path('chat/', views.chat, name='chat'),
    path('baneo/', views.baneo, name='baneo'),
]