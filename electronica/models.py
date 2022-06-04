from django.db import models

# Create your models here.

class computadoras(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    hdmemoria = models.CharField(max_length=30)
    memoriaram = models.CharField(max_length=30)
    procesador = models.CharField(max_length=30)
    sistema = models.CharField(max_length=30)
    pantalla = models.CharField(max_length=30)
    precio = models.IntegerField(max_length=30)

class perifericos(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    características = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=30)

class monitores(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    pantalla = models.CharField(max_length=30)
    precio = models.IntegerField(max_length=30)