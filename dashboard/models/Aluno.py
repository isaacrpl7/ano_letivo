from django.db import models
from dashboard.models import Turma

class Aluno(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name='Codigo')
    descricao = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, related_name='alunos', on_delete=models.CASCADE)