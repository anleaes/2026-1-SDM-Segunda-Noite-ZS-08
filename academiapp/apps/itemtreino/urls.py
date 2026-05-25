from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'itemtreino'

router = routers.SimpleRouter()
router.register('', views.ItemtreinoViewSet, basename='item treino')

urlpatterns = [
    path('', include(router.urls) )
]