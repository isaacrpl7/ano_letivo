# Generated by Django 3.1.2 on 2021-01-31 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0005_disciplina_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='professores', to=settings.AUTH_USER_MODEL),
        ),
    ]