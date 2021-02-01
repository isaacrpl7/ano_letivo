from django.db import models
from django.conf import settings
from dashboard.models import Turma

class Aluno(models.Model):
    codigo = models.CharField(primary_key=True, verbose_name='Codigo', max_length=50)
    nome = models.CharField(max_length=50, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='alunos', default=0)
    descricao = models.CharField(max_length=100, blank=True)
    turma = models.ForeignKey(Turma, related_name='alunos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + " | Código: " + self.codigo