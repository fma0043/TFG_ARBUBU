# Generated by Django 2.2.6 on 2019-11-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_genero_fotogenero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='fotoGenero',
            field=models.ImageField(upload_to='static/imagenes'),
        ),
    ]
