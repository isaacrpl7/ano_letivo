# Generated by Django 3.1.2 on 2021-02-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_habilidade_disciplinas_c_h_obg'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilidade',
            name='disciplinas_c_h_ofe',
            field=models.ManyToManyField(blank=True, related_name='habilidades_ofertadas', to='dashboard.Disciplina'),
        ),
        migrations.AlterField(
            model_name='habilidade',
            name='disciplinas_c_h_obg',
            field=models.ManyToManyField(blank=True, related_name='habilidades_obrigatorias', to='dashboard.Disciplina'),
        ),
    ]
