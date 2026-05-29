from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'refeicoes'

router = routers.SimpleRouter()
router.register('', views.RefeicaoViewSet, basename='refeicoes')

urlpatterns = [
    path('listar/', views.list_refeicoes, name='list_refeicoes'),
    path('adicionar/', views.add_refeicao, name='add_refeicao'),
    path('editar/<int:id_refeicao>/', views.edit_refeicao, name='edit_refeicao'),
    path('excluir/<int:id_refeicao>/', views.delete_refeicao, name='delete_refeicao'),
    
    path('', include(router.urls) )
]