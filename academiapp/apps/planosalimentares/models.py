from django.db import models

class PlanoAlimentar(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    objetivo = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    calorias_diarias = models.IntegerField()