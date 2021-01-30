from django.db import models
from dashboard.models import Aluno

class Habilidade(models.Model):
    codigo = models.IntegerField(primary_key=True,verbose_name='Codigo')
    descricao = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno, related_name='habilidades', blank=True)