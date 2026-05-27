from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'refeicoes'

router = routers.SimpleRouter()
router.register('', views.RefeicaoViewSet, basename='refeicoes')

urlpatterns = [
    path('', include(router.urls))
]