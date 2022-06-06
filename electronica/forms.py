from django import forms
from electronica.models import Perifericos, Monitores, Pc_Notebooks
# from django.db import models
#
# class Create_Perifericos_form(forms.Form):
#     class Meta:
#         model = Perifericos
#         fields = '__all__'

class Create_Perifericos_form(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    caracteristicas = forms.CharField(max_length=60)
    precio = forms.IntegerField()

class Create_Pcnotebooks_form(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    hdmemoria = forms.CharField(max_length=30)
    memoriaram = forms.CharField(max_length=30)
    procesador = forms.CharField(max_length=30)
    sistema = forms.CharField(max_length=30)
    pantalla = forms.CharField(max_length=30)
    precio = forms.IntegerField()

class Create_Monitores_form(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    pantalla = forms.CharField(max_length=30)
    caracteristicas = forms.CharField(max_length=200)
    precio = forms.IntegerField()