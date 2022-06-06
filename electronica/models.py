from django.db import models

# Create your models here.

class Pc_Notebooks(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    hdmemoria = models.CharField(max_length=30)
    memoriaram = models.CharField(max_length=30)
    procesador = models.CharField(max_length=30)
    sistema = models.CharField(max_length=30)
    pantalla = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f'Marca: {self.marca} Modelo: {self.modelo} Precio: $ {self.precio}'

class Perifericos(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    caracteristicas = models.CharField(max_length=60)
    precio = models.IntegerField()

    def __str__(self):
        return f'Marca: {self.marca} Modelo: {self.modelo} Precio: $ {self.precio}'

class Monitores(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    pantalla = models.CharField(max_length=30)
    caracteristicas = models.CharField(max_length=200, null=True)
    precio = models.IntegerField()

    def __str__(self):
        return f'Marca: {self.marca} Modelo: {self.modelo} Pantalla: {self.pantalla} Precio: $ {self.precio}'