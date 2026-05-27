from django.shortcuts import render
from rest_framework import viewsets
from .models import Alimento
from .serializer import AlimentoSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer