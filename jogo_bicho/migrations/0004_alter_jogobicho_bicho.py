# Generated by Django 4.1.2 on 2022-10-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogo_bicho', '0003_remove_jogobicho_resultado_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogobicho',
            name='bicho',
            field=models.CharField(max_length=200, verbose_name='Nome do Bicho:'),
        ),
    ]
