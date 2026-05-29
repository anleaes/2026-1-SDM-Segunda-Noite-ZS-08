from django.urls import path, include
from .import views
from rest_framework import routers

app_name = 'planosmensalidade'

router = routers.SimpleRouter()
router.register('', views.PlanosMensalidadeViewSet, basename='planosmensalidade')

urlpatterns = [
    path('listar/', views.list_planos, name='list_planos'),
    path('adicionar/', views.add_plano, name='add_plano'),
    path('editar/<int:id_plano>/', views.edit_plano, name='edit_plano'),
    path('excluir/<int:id_plano>/', views.delete_plano, name='delete_plano'),

    path('', include(router.urls) )
]