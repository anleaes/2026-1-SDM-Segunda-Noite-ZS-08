from django.shortcuts import render
from .models import Anamnese
from rest_framework import viewsets
from .serializer import AnamneseSerializer

# Create your views here.
class AnamneseViewSet (viewsets.ModelViewSet):
    queryset = Anamnese.objects.all()
    serializer_class = AnamneseSerializer