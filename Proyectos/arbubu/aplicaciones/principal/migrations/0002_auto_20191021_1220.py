# Generated by Django 2.2.6 on 2019-10-21 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especie',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='genero',
            name='familia',
        ),
        migrations.RemoveField(
            model_name='individuos',
            name='especie',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Especie',
        ),
        migrations.DeleteModel(
            name='Familia',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Individuos',
        ),
    ]
