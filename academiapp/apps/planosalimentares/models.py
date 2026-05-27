from django.db import models

class PlanoAlimentar(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    objetivo = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    calorias_diarias = models.IntegerField()
    
    class Meta:
        db_table = 'planos_alimentares'
        verbose_name = 'Plano Alimentar'
        verbose_name_plural = 'Planos Alimentares'

    def __str__(self):
        return self.titulo