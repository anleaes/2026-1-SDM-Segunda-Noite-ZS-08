from django.urls import path, include
from .import views
from rest_framework import routers

app_name = 'planosmensalidade'

router = routers.SimpleRouter()
router.register('', views.PlanosMensalidadeViewSet, basename='planosmensalidade')

urlpatterns = [
    path('', include(router.urls) )
]

