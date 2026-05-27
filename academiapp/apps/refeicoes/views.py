from django.shortcuts import render
from .models import Refeicao
from rest_framework import viewsets
from .serializer import RefeicaoSerializer

# Create your views here.
class RefeicaoViewSet(viewsets.ModelViewSet):
    pass