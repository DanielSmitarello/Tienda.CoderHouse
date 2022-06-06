from django.shortcuts import render
from django.http import HttpResponse
from electronica.models import Pc_Notebooks, Perifericos, Monitores
from electronica.forms import Create_Perifericos_form, Create_Pcnotebooks_form, Create_Monitores_form


# Create your views here.

def index(request):
    context = {
    }
    return render(request, 'index.html', context = context)

def pc_notebooks(request):
    pc_notebooks = Pc_Notebooks.objects.all()
    context = {
        'pc_notebooks':pc_notebooks,
    }
    return render(request, 'pc_notebooks.html', context = context)

def perifericos(request):
    impresoras = Perifericos.objects.all()
    context = {
        'impresoras':impresoras,
    }
    return render(request, 'perifericos.html', context = context)

def screen(reques):
    monitorespc = Monitores.objects.all()
    context = {
        'monitorespc': monitorespc,
    }
    return render(reques, 'monitores.html', context = context)

def create_product_monitores(request):
    if request.method == 'GET':
        form_monitores = Create_Monitores_form()
        context = {
        'form_monitores':form_monitores,
        }
        return render(request, 'create_product_monitores.html', context = context)
    else:
        form_monitores = Create_Monitores_form(request.POST)
        if form_monitores.is_valid():
            nuevo_monitor = Monitores.objects.create(
                marca =form_monitores.cleaned_data['marca'],
                modelo=form_monitores.cleaned_data['modelo'],
                pantalla=form_monitores.cleaned_data['pantalla'],
                caracteristicas=form_monitores.cleaned_data['caracteristicas'],
                precio=form_monitores.cleaned_data['precio'],
            )
            context = {
                'nuevo_monitor':nuevo_monitor,
            }
    return render(request, 'create_product_monitores.html', context=context)

def create_product_pcnotebooks(request):
    if request.method == 'GET':
        form_pcnotebooks = Create_Pcnotebooks_form()
        context = {
            'form_pcnotebooks': form_pcnotebooks,
        }
        return render(request, 'create_product_pcnotebooks.html', context=context)
    else:
        form_pcnotebooks = Create_Pcnotebooks_form(request.POST)
        if form_pcnotebooks.is_valid():
            nuevo_pcnotebook = Pc_Notebooks.objects.create(
                marca=form_pcnotebooks.cleaned_data['marca'],
                modelo=form_pcnotebooks.cleaned_data['modelo'],
                hdmemoria=form_pcnotebooks.cleaned_data['hdmemoria'],
                memoriaram=form_pcnotebooks.cleaned_data['memoriaram'],
                procesador=form_pcnotebooks.cleaned_data['procesador'],
                sistema=form_pcnotebooks.cleaned_data['sistema'],
                pantalla=form_pcnotebooks.cleaned_data['pantalla'],
                precio = form_pcnotebooks.cleaned_data['precio'],
            )
            context = {
                'nuevo_pcnotebook': nuevo_pcnotebook,
            }
    return render(request, 'create_product_pcnotebooks.html', context = context)

def create_product_perifericos(request):
    if request.method == 'GET':
        form_perifericos = Create_Perifericos_form()
        context = {
        'form_perifericos': form_perifericos,
        }
        return render(request, 'create_product_perifericos.html', context = context)
    else:
        form_perifericos = Create_Perifericos_form(request.POST)
        if form_perifericos.is_valid():
            nuevo_periferico = Perifericos.objects.create(
                marca = form_perifericos.cleaned_data['marca'],
                modelo = form_perifericos.cleaned_data['modelo'],
                caracteristicas = form_perifericos.cleaned_data['caracteristicas'],
                precio = form_perifericos.cleaned_data['precio'],
                )
            context = {
                'nuevo_periferico': nuevo_periferico,
            }
        return render(request, 'create_product_perifericos.html', context = context)
