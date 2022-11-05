from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    id = models.CharField(primary_key = True,max_length=10)
    rol = models.IntegerField()
    cant_max = models.IntegerField()
    prestamos_actuales = models.IntegerField()

class Material(models.Model):
    id = models.CharField(primary_key = True,max_length=10)
    titulo = models.CharField(max_length=128)
    fecha_registro = models.DateField()
    cant_registrada = models.IntegerField()
    cant_actual = models.IntegerField()

class Registro(models.Model):
    tipo = models.CharField(max_length=15)
    material = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    cantidad = models.IntegerField()