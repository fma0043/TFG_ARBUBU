# Generated by Django 2.2.1 on 2019-05-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0007_auto_20190529_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individuos',
            name='altura',
            field=models.DecimalField(decimal_places=15, default=0, max_digits=19, verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='perimetro',
            field=models.DecimalField(decimal_places=15, default=0, max_digits=19, verbose_name='Perimetro'),
        ),
    ]