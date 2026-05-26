from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=100) 
    email = models.EmailField('E-mail', max_length=100)
    telefone = models.CharField('Número de telefone', max_length=15)
    data_nascimento = models.DateField('Data de nascimento', auto_now=False, auto_now_add=False)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    foto = models.ImageField('Foto', upload_to='pessoas/fotos', blank=True,null=True)