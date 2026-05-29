from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'treinos'

router = routers.SimpleRouter()
router.register('', views.TreinoViewSet, basename='treinos')

urlpatterns = [
    path('listar/', views.list_treinos, name='list_treinos'),
    path('exercicios/', views.list_exercicios_add, name='list_exercicios_add'),
    path('montar/', views.montar_treino, name='montar_treino'),
    path('montar/adicionar/<int:id_exercicio>/', views.add_exercicio_treino, name='add_exercicio_treino'),
    path('montar/editar/<int:id_exercicio>/', views.edit_exercicio_treino, name='edit_exercicio_treino'),
    path('montar/excluir/<int:id_exercicio>/', views.delete_exercicio_treino, name='delete_exercicio_treino'),
    path('finalizar/', views.finalizar_treino, name='finalizar_treino'),
    path('visualizar/<int:id_treino>/', views.view_treino, name='view_treino'),
    path('excluir/<int:id_treino>/', views.delete_treino, name='delete_treino'),
    
    path('', include(router.urls) )
]