from django.shortcuts import render
from electronica.models import Pc_Notebooks, Perifericos, Monitores

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