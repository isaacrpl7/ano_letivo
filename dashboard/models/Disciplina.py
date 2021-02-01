from django.db import models
from django.conf import settings
from dashboard.models import Turma, Habilidade

class Disciplina(models.Model):
    turma = models.ForeignKey(Turma, related_name='disciplinas',on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='disciplinas', default=0)
    codigo = models.CharField(primary_key=True,verbose_name='Codigo', max_length=50)
    descricao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome + " | Código: " + self.codigo