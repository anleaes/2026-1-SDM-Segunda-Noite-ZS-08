from django.shortcuts import render
from .models import PlanosMensalidade
from rest_framework import viewsets
from .serializer import PlanosMensalidadeSerializer

# Create your views here.
class PlanosMensalidadeViewSet(viewsets.ModelViewSet):
    queryset = PlanosMensalidade.objects.all()
    serializer_class = PlanosMensalidadeSerializer