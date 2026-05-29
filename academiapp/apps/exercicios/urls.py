from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'exercicios'

router = routers.SimpleRouter()
router.register('', views.ExercicioViewSet, basename='exercicios')

urlpatterns = [
    path('listar/', views.list_exercicios, name='list_exercicios'),
    path('adicionar/', views.add_exercicio, name='add_exercicio'),
    path('editar/<int:id_exercicio>/', views.edit_exercicio, name='edit_exercicio'),
    path('excluir/<int:id_exercicio>/', views.delete_exercicio, name='delete_exercicio'),

    path('', include(router.urls) )
]