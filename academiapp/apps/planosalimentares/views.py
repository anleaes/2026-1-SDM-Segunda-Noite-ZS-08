from django.shortcuts import render, get_object_or_404, redirect
from .models import PlanoAlimentar
from rest_framework import viewsets
from .serializers import PlanoAlimentarSerializer
from planosalimentares.models import PlanoAlimentar
from itemtreino.models import Treino
from exercicios.models import Exercicio
from refeicoes.models import Refeicao
from employees.models import Employee


class PlanoAlimentarViewSet(viewsets.ModelViewSet):
    queryset = PlanoAlimentar.objects.all()
    serializer_class = PlanoAlimentarSerializer  
    
    