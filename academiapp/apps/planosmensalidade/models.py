from django.db import models

# Create your models here.
class PlanosMensalidade(models.Model):
    opcoes_vigencia=[
        (30, '30 dias'),
        (90, '90 dias'),
        (180, '180 dias'),
        (365, '365 dias'),
    ]

    nome = models.CharField('Nome do plano', max_length=50)
    descricao = models.TextField('Descrição do plano')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2) 
    duracao_dias = models.IntegerField('Vigência do plano', help_text='Em dias, exemplo: 30 dias',choices=opcoes_vigencia)
    ativo = models.BooleanField ('Plano ativo', default=True)