from django.shortcuts import render
from .models import Exercicio
from rest_framework import viewsets
from .serializer import ExercicioSerializer

# Create your views here.
class ExercicoViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer  