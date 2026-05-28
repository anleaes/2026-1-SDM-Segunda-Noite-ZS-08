from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'anamnese'

router = routers.SimpleRouter()
router.register('', views.AnamneseViewSet, basename='anamnese')

urlpatterns = [
    path('listar/', views.list_anamneses, name='list_anamneses'),
    path('adicionar/', views.add_anamnese, name='add_anamnese'),
    path('editar/<int:id_anamnese>/', views.edit_anamnese, name='edit_anamnese'),
    path('excluir/<int:id_anamnese>/', views.delete_anamnese, name='delete_anamnese'),

    path('', include(router.urls))
]