from rest_framework import viewsets
from .models import PlanoAlimentar
from .serializer import PlanoAlimentarSerializer

class PlanoAlimentarViewSet(viewsets.ModelViewSet):
    queryset = PlanoAlimentar.objects.all()
    serializer_class = PlanoAlimentarSerializer