# Generated by Django 2.2.6 on 2019-11-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_auto_20191111_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='nombreCientificoEspecie',
            field=models.CharField(max_length=50, verbose_name='Nombre Cientifico'),
        ),
    ]
