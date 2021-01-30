from django.contrib import admin
from dashboard.models import Disciplina, Escola, Habilidade, Professor, Turma

# Register your models here.
admin.site.register(Disciplina)
admin.site.register(Escola)
admin.site.register(Habilidade)
admin.site.register(Professor)
admin.site.register(Turma)