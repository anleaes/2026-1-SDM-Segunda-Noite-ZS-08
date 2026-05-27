from django.shortcuts import render
from .models import PlanoAlimentar
from rest_framework import viewsets
from .serializer import PlanoAlimentarSerializer


class PlanoAlimentarViewSet(viewsets.ModelViewSet):
    pass
