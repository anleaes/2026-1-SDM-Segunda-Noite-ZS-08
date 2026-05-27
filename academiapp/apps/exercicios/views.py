from django.shortcuts import render
from .models import Exercicio
from rest_framework import viewsets
from .serializers import ExercicioSerializer

# Create your views here.
class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer  