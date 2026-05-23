from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Alimentos'

router = routers.SimpleRouter()
router.register('', views.AlimentoViewSet, basename='Alimentos')

urlpatterns = [
    path('', include(router.urls) )
]