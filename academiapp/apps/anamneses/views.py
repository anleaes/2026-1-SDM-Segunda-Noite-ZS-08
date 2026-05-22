from django.shortcuts import render
from .models import Anamneses
from rest_framework import viewsets
from .serializer import AnamneseSerializer

# Create your views here.
class AnamneseViewSet (viewsets.ModelViewSet):
    queryset = Anamneses.objects.all()
    serializer_class = AnamneseSerializer