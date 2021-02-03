from django.db import models
from django.conf import settings
from dashboard.models import Escola

class Turma(models.Model):
    escola = models.ForeignKey(Escola, related_name='turmas', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='turmas', on_delete=models.CASCADE, default=0)
    codigo = models.CharField(primary_key=True,verbose_name='Codigo', max_length=50)
    descricao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "Turma: " + self.codigo + " | Escola: " + self.escola.nome

    class Meta:
        ordering = ['-codigo']