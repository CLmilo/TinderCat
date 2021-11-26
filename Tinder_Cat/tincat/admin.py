from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Trabajador)
admin.site.register(Empleado)
admin.site.register(Gerencia)
admin.site.register(Moderador)
admin.site.register(Usuario_reportados_total)
admin.site.register(Usuario_advertidos_total)
admin.site.register(Usuario_baneados_total)
admin.site.register(Perfil_usuario)
admin.site.register(Mensaje_chat)
admin.site.register(Usuario_interes)
admin.site.register(Usuario_interesado)
admin.site.register(Usuarios_reportados)