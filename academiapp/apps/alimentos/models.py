from django.db import models

class Alimento(models.Model):
    nome = models.CharField(max_length=150)
    calorias_por_100g = models.DecimalField(max_digits=6, decimal_places=2)
    proteinas_g = models.DecimalField(max_digits=6, decimal_places=2)
    carboidratos_g = models.DecimalField(max_digits=6, decimal_places=2)
    gorduras_g = models.DecimalField(max_digits=6, decimal_places=2)
    fibras_g = models.DecimalField(max_digits=6, decimal_places=2)

