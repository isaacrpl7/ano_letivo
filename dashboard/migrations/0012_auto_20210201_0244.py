# Generated by Django 3.1.2 on 2021-02-01 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20210201_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='descricao',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='escola',
            name='descricao',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='turma',
            name='descricao',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
