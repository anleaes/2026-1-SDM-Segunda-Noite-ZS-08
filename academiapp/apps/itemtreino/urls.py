from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'itemtreino'

router = routers.SimpleRouter()
router.register('', views.ItemTreinoViewSet, basename='itemTreino')

urlpatterns = [
    path('', include(router.urls) )
]