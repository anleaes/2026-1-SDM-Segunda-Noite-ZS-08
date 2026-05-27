from rest_framework import viewsets
from .models import Refeicao
from .serializer import RefeicaoSerializer

class RefeicaoViewSet(viewsets.ModelViewSet):
    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer