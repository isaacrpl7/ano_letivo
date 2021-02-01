from django.db import models
from django.conf import settings
from dashboard.models import Aluno, Disciplina

class Habilidade(models.Model):
    codigo = models.CharField(primary_key=True,verbose_name='Codigo', max_length=50)
    nome = models.CharField(max_length=50, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='habilidades', default=0)
    descricao = models.CharField(max_length=100, blank=True)
    alunos = models.ManyToManyField(Aluno, related_name='habilidades', blank=True)

    def __str__(self):
        return self.nome + " | Código: " + self.codigo