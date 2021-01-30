from django.db import models
from dashboard.models import Disciplina

class Professor(models.Model):
    disciplina = models.ForeignKey(Disciplina, related_name='professores', on_delete=models.CASCADE)
    codigo = models.IntegerField(primary_key=True,verbose_name='Codigo')
    descricao = models.CharField(max_length=100)