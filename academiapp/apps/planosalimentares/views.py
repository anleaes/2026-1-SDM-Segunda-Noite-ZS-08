from django.shortcuts import render
from .models import PlanoAlimentar
from rest_framework import viewsets
from .serializer import PlanoAlimentarSerializer

# Create your views here.
class PlanoAlimentarViewSet(viewsets.ModelViewSet):
    queryset = PlanoAlimentar.objects.all()
    serializer_class = PlanoAlimentarSerializer  