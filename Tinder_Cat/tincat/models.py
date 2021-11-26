from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Persona(models.Model):
    id_persona = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=100, null=False)
    dni = models.CharField(max_length=8, null=False)
    sexo = models.CharField(max_length=9, null=False)

class Cliente(models.Model):
    id_cliente = models.PositiveIntegerField(primary_key=True)
    id_persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=False)
    cantidad_perfiles = models.PositiveSmallIntegerField(null=False)

class Trabajador(models.Model):
    id_trabajador = models.PositiveIntegerField(primary_key=True)
    id_persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    sueldo = models.PositiveSmallIntegerField(null=False)
    anterior_cargo = models.CharField(max_length=50, null=False)
    fecha_inicio_trabajo = models.DateField(null=False)
    fecha_pago = models.DateField(null=False)
    sede_trabajo = models.CharField(max_length=50, null=False)
    fecha_fin_trabajo = models.DateField(null=False)

class Empleado(models.Model):
    id_trabajador = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    area_designada = models.CharField(max_length=50, null=False)
    jefe_inmediato = models.PositiveIntegerField(null=False)
    rol = models.CharField(max_length=50, null=False)

class Gerencia(models.Model):
    area_encargada = models.CharField(max_length=30, null=False)
    superior_inmediato = models.PositiveIntegerField(null=False)
    id_trabajador = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    id_gerente = models.PositiveIntegerField(primary_key=True)

class Moderador(models.Model):
    id_trabajador = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    id_moderador = models.PositiveIntegerField(primary_key=True)
    sede_encargada = models.CharField(max_length=50, null=False)

class Usuario_reportados_total(models.Model):
    id_cliente_reportado = models.PositiveIntegerField(null=False)
    id_cliente_acusante = models.PositiveIntegerField(null=False)
    fecha_reporte = models.DateField(null=False)
    razon_reporte = models.TextField(null=False)

class Usuario_advertidos_total(models.Model):
    id_cliente_reportado = models.PositiveIntegerField(null=False)
    fecha_advertencia = models.DateField(null=False)
    razon_reporte = models.TextField(null=False)
    razon_advertencia = models.TextField(null=False)

class Usuario_baneados_total(models.Model):
    id_cliente_baneado = models.PositiveIntegerField(null=False)
    id_cliente_acusante = models.PositiveIntegerField(null=False)
    razon_reporte = models.TextField(null=False)
    razon_baneado = models.TextField(null=False)
    fecha_baneo = models.DateField(null=False)

class Perfil_usuario(models.Model):
    id_usuario = models.PositiveIntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    nombre_gato = models.CharField(max_length=50, null=False)
    sexo_gato = models.CharField(max_length=9, null=False)
    raza_gato = models.CharField(max_length=30, null=False)
    edad_gato = models.PositiveIntegerField(null=False)

class Mensaje_chat(models.Model):
    id_usuario = models.ForeignKey(Perfil_usuario, null=False, blank=False, on_delete=models.CASCADE)
    fecha_mensaje = models.DateField(null=False)
    mensaje = models.TextField(null=False)
    reaccion = models.CharField(max_length=10, null=False)

class Usuario_interes(models.Model):
    id_usuario = models.ForeignKey(Perfil_usuario, null=False, blank=False, on_delete=models.CASCADE)
    id_usuario_interes = models.PositiveIntegerField(null=False)
    fecha_like = models.DateField(null=False)

class Usuario_interesado(models.Model):
    id_usuario = models.ForeignKey(Perfil_usuario, null=False, blank=False, on_delete=models.CASCADE)
    id_usuario_reportado = models.PositiveIntegerField(null=False)
    fecha_like = models.DateField(null=False)

class Usuarios_reportados(models.Model):
    id_usuario = models.ForeignKey(Perfil_usuario, null=False, blank=False, on_delete=models.CASCADE)
    id_usuario_reportado = models.PositiveIntegerField(null=False)
    fecha_reporte = models.DateField(null=False)
    razon_reporte = models.TextField(null=False)
