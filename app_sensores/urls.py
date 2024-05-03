from django.urls import path
from . import views

urlpatterns = [
    path('', views.abrir_index, name='abrir_index'),
    path('listar_dados', views.listar_dados, name='listar_dados'),

]