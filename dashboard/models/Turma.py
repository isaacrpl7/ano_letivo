from django.db import models
from dashboard.models import Escola

class Turma(models.Model):
    escola = models.ForeignKey(Escola, related_name='turmas', on_delete=models.CASCADE)
    codigo = models.IntegerField(primary_key=True,verbose_name='Codigo')
    descricao = models.CharField(max_length=100)