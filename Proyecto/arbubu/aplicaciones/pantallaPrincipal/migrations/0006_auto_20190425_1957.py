# Generated by Django 2.2 on 2019-04-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0005_auto_20190425_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='nombre',
            field=models.CharField(max_length=80, verbose_name='Nombres'),
        ),
    ]