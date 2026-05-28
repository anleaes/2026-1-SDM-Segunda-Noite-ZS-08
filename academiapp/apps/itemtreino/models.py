from django.db import models
from exercicios.models import Exercicio
from treinos.models import Treino



# Create your models here.
class ItemTreino(models.Model):
    
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, related_name='itens')
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE, related_name='itens_treino')
    
    series = models.IntegerField()
    repeticoes = models.IntegerField()
    carga_kg = models.DecimalField(max_digits=5, decimal_places=2)
    intervalo_segundos = models.IntegerField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.series}x{self.repeticoes} de {self.exercicio.nome} no {self.treino.nome}"