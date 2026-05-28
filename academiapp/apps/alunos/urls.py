from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'alunos'

router = routers.SimpleRouter()
router.register('', views.AlunoViewSet, basename='alunos')

urlpatterns = [
    path('listar/', views.list_alunos, name='list_alunos'),
    path('adicionar/', views.add_aluno, name='add_aluno'),
    path('editar/<int:id_aluno>/', views.edit_aluno, name='edit_aluno'),
    path('excluir/<int:id_aluno>/', views.delete_aluno, name='delete_aluno'),

    path('', include(router.urls))
]