# Generated by Django 4.1.2 on 2022-10-25 23:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jogo_bicho', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogobicho',
            name='resultado_hora',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
    ]
