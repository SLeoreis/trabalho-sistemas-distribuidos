# Generated by Django 3.2.5 on 2021-08-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_cadastro_tempo_de_aprendizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='data_anotacao',
            field=models.DateField(default=None, verbose_name='Data'),
        ),
    ]