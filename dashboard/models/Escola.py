from django.db import models
from django.conf import settings

class Escola(models.Model):
    codigo = models.CharField(primary_key=True,verbose_name='Codigo',max_length=50)
    nome = models.CharField(max_length=50, default='')
    descricao = models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='escolas', default=0)

    def __str__(self):
        return self.nome + " | Código: " + self.codigo