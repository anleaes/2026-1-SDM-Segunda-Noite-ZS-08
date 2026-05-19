from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Pessoas'

router = routers.SimpleRouter()
router.register('', views.PessoaViewSet, basename = 'pessoas')

urlpatterns = [
    path('', include(router.urls) )
]
