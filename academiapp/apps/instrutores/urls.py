from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'instrutores'

router=routers.SimpleRouter()
router.register('', views.InstrutorViewSet, basename='instrutores')

urlpatterns = [
    path('listar/', views.list_instrutores, name='list_instrutores'),
    path('adicionar/', views.add_instrutor, name='add_instrutor'),
    path('editar/<int:id_instrutor>/', views.edit_instrutor, name='edit_instrutor'),
    path('excluir/<int:id_instrutor>/', views.delete_instrutor, name='delete_instrutor'),

    path('', include(router.urls))
]