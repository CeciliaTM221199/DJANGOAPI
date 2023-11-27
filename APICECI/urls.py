"""APICECI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import Login, Index, Iconos, LoginRegistro,InserUser
from api.views import *
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',LoginInicio.as_view(), name='LoginInicio'),
    path('loginRegistro.html',LoginRegistro.as_view(), name='LoginRegistro'),
    path('index/',Index.as_view(), name='Index'),
    path('icons.html',Iconos.as_view(), name='Iconos'),
    path('InserUser/',InserUser.registro, name='insert_user'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('', views.chart_view, name='chart_view'),
    #('producto/', views.ProductView, name='products')
    
]
