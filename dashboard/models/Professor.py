from django.db import models
from django.conf import settings
from dashboard.models import Disciplina

class Professor(models.Model):
    disciplina = models.ManyToManyField(Disciplina, related_name='professores')
    nome = models.CharField(max_length=50, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='professores', default=0)
    codigo = models.CharField(primary_key=True,verbose_name='Codigo', max_length=50)
    descricao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome + " | Código: " + self.codigo

    class Meta:
        ordering = ['-codigo']