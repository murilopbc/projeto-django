from django.urls import path
from . import views

urlpatterns = [
    path('', views.abrir_index, name='abrir_index'),
    path('listar_dados', views.listar_dados, name='listar_dados'),
    path('editar_dados', views.editar_dados, name='editar_dados'),
    path('excluir_dados/<int:id>', views.excluir_dados, name='excluir_dados'),
    path('abrir_edicao/<int:id>',views.abrir_edicao, name='abrir_edicao'),


    
]