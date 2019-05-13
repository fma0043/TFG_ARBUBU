# Generated by Django 2.2 on 2019-05-09 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0006_auto_20190509_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='individuos',
            name='especie',
            field=models.ForeignKey(default='Acer pseudoplatanus', on_delete=django.db.models.deletion.CASCADE, to='pantallaPrincipal.Especie'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='fotoArbol',
            field=models.ImageField(upload_to='static/imagenes'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='fotoFrutos',
            field=models.ImageField(blank=True, upload_to='static/imagenes'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='fotoHojas',
            field=models.ImageField(blank=True, upload_to='static/imagenes'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='fotoTronco',
            field=models.ImageField(blank=True, upload_to='static/imagenes'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='motivoSingular',
            field=models.TextField(choices=[('AN', 'Antigüedad'), ('DI', 'Elevado Diámetro'), ('HI', 'Lo plantó un personaje histórico')], verbose_name='Motivo de Singularidad'),
        ),
    ]