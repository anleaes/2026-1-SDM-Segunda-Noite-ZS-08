from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'planosalimentares'

router = routers.SimpleRouter()
router.register('', views.PlanoAlimentarViewSet, basename='planosalimentares')

urlpatterns = [
    path('listar/', views.list_planosalimentares, name='list_planosalimentares'),
    path('adicionar/', views.add_planoalimentar, name='add_planoalimentar'),
    path('editar/<int:id_plano>/', views.edit_planoalimentar, name='edit_planoalimentar'),
    path('excluir/<int:id_plano>/', views.delete_planoalimentar, name='delete_planoalimentar'),

    path('', include(router.urls) )
]