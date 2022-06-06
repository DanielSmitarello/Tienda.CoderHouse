"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from electronica.views import pc_notebooks, perifericos, screen, index, create_product_monitores, create_product_pcnotebooks, create_product_perifericos, search_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('pc_notebooks/', pc_notebooks, name = 'pc_notebooks'),
    path('perifericos/', perifericos, name = 'perifericos'),
    path('monitores/', screen, name = 'monitores'),
    path('create_product_monitores/', create_product_monitores, name = 'create_product_monitores'),
    path('create_product_pcnotebooks/', create_product_pcnotebooks, name = 'create_product_pcnotebooks'),
    path('create_product_perifericos/', create_product_perifericos, name = 'create_product_perifericos'),
    path('search_product/', search_product, name = 'search_product'),

]
