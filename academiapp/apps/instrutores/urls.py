from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'instrutores'

router=routers.SimpleRouter()
router.register('', views.InstrutorViewSet, basename='instrutores')

urlpatterns = [
    path('', include(router.urls))
]