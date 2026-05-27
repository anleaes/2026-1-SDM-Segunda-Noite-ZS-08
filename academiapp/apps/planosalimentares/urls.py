from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'planosalimentares'

router = routers.SimpleRouter()
router.register('', views.PlanoAlimentarViewSet, basename='planosalimentares')

urlpatterns = [
    path('', include(router.urls))
]