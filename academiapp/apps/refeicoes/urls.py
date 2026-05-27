from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'refeicoes'

router = routers.SimpleRouter()