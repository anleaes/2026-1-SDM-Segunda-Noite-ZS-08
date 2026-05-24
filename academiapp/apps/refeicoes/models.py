from django.db import models
from alimentos.models import Alimento
from planosalimentares.models import PlanoAlimentar

# Create your models here.
class Refeicao(models.Model):
    alimentos = models.ManyToManyField(Alimento, verbose_name="Alimentos da refeição")
    plano_alimentar = models.ForeignKey(PlanoAlimentar,on_delete=models.CASCADE,related_name='refeicoes',verbose_name='Plano Alimentar', null=True, blank=True)
    nome = models.CharField('Nome da Refeição', max_length=50)
    horario = models.TimeField('Horário')
    descricao = models.TextField('Descrição', blank=True, null=True)

    class Meta:
        verbose_name = 'Refeição'
        verbose_name_plural = 'Refeições'
        ordering = ['horario']

    def __str__(self):
        return f"{self.nome} - {self.horario}"