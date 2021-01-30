from django.db import models
from dashboard.models import Turma

class Disciplina(models.Model):
    turma = models.ForeignKey(Turma, related_name='disciplinas',on_delete=models.CASCADE)
    codigo = models.IntegerField(primary_key=True,verbose_name='Codigo')
    descricao = models.CharField(max_length=100)