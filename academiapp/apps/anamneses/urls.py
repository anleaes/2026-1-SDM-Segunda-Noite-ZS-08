from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'anamnese'

router = routers.SimpleRouter()
router.register('', views.AnamneseViewSet, basename='anamnese')

urlpatterns = [
    path('', include(router.urls))
]
