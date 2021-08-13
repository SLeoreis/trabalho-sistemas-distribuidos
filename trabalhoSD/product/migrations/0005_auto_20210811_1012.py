# Generated by Django 3.2.5 on 2021-08-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210806_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geral',
            name='cobertura',
            field=models.CharField(max_length=30, null=True, verbose_name='Cobertura'),
        ),
        migrations.AlterField(
            model_name='geral',
            name='descricao',
            field=models.CharField(max_length=800, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='metadados_tecnicos',
            name='duracao',
            field=models.TimeField(verbose_name='Duracao'),
        ),
    ]