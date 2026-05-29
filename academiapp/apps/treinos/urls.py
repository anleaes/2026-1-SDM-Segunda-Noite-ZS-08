from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'treinos'

router = routers.SimpleRouter()
router.register('', views.TreinoViewSet, basename='treinos')

urlpatterns = [
    path('listar/', views.list_treinos, name='list_treinos'),
    path('adicionar/', views.add_treino, name='add_treino'),
    path('editar/<int:id_treino>/', views.edit_treino, name='edit_treino'),
    path('excluir/<int:id_treino>/', views.delete_treino, name='delete_treino'),
    
    path('', include(router.urls) )
]