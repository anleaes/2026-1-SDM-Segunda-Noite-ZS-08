from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'treinos'

router = routers.SimpleRouter()
router.register('', views.TreinoViewSet, basename='treinos')

urlpatterns = [
    path('', include(router.urls) )
]