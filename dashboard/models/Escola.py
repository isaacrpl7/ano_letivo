from django.db import models

class Escola(models.Model):
    codigo = models.IntegerField(primary_key=True,verbose_name='Codigo')
    descricao = models.CharField(max_length=100)