# Generated by Django 2.2.6 on 2019-11-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0015_auto_20191111_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individuos',
            name='x',
        ),
        migrations.RemoveField(
            model_name='individuos',
            name='y',
        ),
        migrations.AddField(
            model_name='individuos',
            name='latitud',
            field=models.DecimalField(decimal_places=15, default=1, max_digits=19, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='individuos',
            name='longitud',
            field=models.DecimalField(decimal_places=18, default=1, max_digits=19, verbose_name='Longitud'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='fotoArbol',
            field=models.ImageField(blank=True, upload_to='static/imagenes'),
        ),
    ]
