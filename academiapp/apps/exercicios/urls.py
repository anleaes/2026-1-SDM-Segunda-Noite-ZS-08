from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'exercicios'

router = routers.SimpleRouter()
router.register('', views.ExercicioViewSet, basename='exercicios')

urlpatterns = [
    path('', include(router.urls) )
]