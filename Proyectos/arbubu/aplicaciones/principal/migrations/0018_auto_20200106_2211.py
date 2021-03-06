# Generated by Django 2.2.6 on 2020-01-06 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0017_auto_20191115_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='especie',
            options={'ordering': ['nombreCientificoEspecie']},
        ),
        migrations.AlterModelOptions(
            name='individuos',
            options={'ordering': ['nombreComun']},
        ),
        migrations.RemoveField(
            model_name='genero',
            name='fotoGenero',
        ),
        migrations.AlterField(
            model_name='individuos',
            name='latitud',
            field=models.DecimalField(decimal_places=7, default=1, max_digits=11, verbose_name='Latitud'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='longitud',
            field=models.DecimalField(decimal_places=9, default=1, max_digits=11, verbose_name='Longitud'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='ubicacion',
            field=models.CharField(choices=[('Campus Río Vena', 'Campus Río Vena'), ('Hospital del Rey', 'Hospital del Rey'), ('Hospital Militar', 'Hospital Militar'), ('Campus de Educación', 'Campus de Educación'), ('Campus de Ciencias', 'Campus de Ciencias')], max_length=50, verbose_name='Ubicación'),
        ),
    ]
