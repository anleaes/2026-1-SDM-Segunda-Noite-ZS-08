from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'alunos'

router = routers.SimpleRouter()
router.register('', views.AlunoViewSet, basename='alunos')

urlpatterns = [
    path('', include(router.urls))
]

