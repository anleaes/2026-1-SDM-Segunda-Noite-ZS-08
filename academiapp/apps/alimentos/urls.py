from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Alimentos'

router = routers.SimpleRouter()
router.register('', views.AlimentoViewSet, basename='Alimentos')

urlpatterns = [
    path('listar/', views.list_alimentos, name='list_alimentos'),
    path('adicionar/', views.add_alimento, name='add_alimento'),
    path('editar/<int:id_alimento>/', views.edit_alimento, name='edit_alimento'),
    path('excluir/<int:id_alimento>/', views.delete_alimento, name='delete_alimento'),
]

urlpatterns = [
    path('', include(router.urls) )
]