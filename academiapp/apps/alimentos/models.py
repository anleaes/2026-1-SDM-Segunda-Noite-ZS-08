from django.db import models

# Create your models here.
class Alimento(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Alimento")
    calorias_por_100g = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Calorias por 100g (kcal)")
    proteinas_g = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Proteínas (g)")
    carboidratos_g = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Carboidratos (g)")
    gorduras_g = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Gorduras (g)")
    fibras_g = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name="Fibras (g)")