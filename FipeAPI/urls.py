"""Fipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'fipeapi'
urlpatterns = [
    path('', views.consultar_mes, name='meses'),
    path('mes/<int:referencia_id>/carro/', views.consultar_marcas_de_carros, name='marcas'),
    path('mes/<int:referencia_id>/carro/<int:marca_id>/', views.consultar_modelos_de_carros, name='modelos'),
    path('mes/<int:referencia_id>/carro/<int:marca_id>/ano/<str:ano>/', views.consultar_modelos_de_ano_de_carro, name='modelosano'),
    path('mes/<int:referencia_id>/carro/<int:marca_id>/modelo/<int:modelo_id>/', views.consultar_anos_de_modelo_de_carro, name='anos'),
    path('mes/<int:referencia_id>/carro/<int:marca_id>/modelo/<int:modelo_id>/ano/<str:ano>/', views.consultar_valor_de_carro, name='valor'),
    path('armazenar', views.armazenar, name='armazenar'),
]
