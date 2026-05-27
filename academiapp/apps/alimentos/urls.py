from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'alimentos'

router = routers.SimpleRouter()
router.register('', views.AlimentoViewSet, basename='alimentos')

urlpatterns = [
    path('', include(router.urls))
]