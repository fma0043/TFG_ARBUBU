# Generated by Django 2.2.1 on 2019-05-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individuos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivoSingular', models.CharField(choices=[('Antigüedad', 'Antigüedad'), ('Elevado Diámetro', 'Elevado Diámetro'), ('Plantado por un personaje histórico', 'Plantado por un personaje histórico'), ('Vistosidad', 'Vistosidad'), ('Madera codiciada', 'Madera codiciada'), ('Frutos peculiares', 'Frutos peculiares'), ('Utilidad medicinal', 'Utilidad medicinal')], max_length=50, verbose_name='Motivo de Singularidad')),
                ('explicacionMotivoSingular', models.TextField(verbose_name='Explicacion de Singularidad')),
                ('x', models.IntegerField(default=1, verbose_name='X')),
                ('y', models.IntegerField(default=1, verbose_name='Y')),
                ('fotoArbol', models.ImageField(upload_to='static/imagenes')),
                ('fotoHojas', models.ImageField(blank=True, upload_to='static/imagenes')),
                ('fotoTronco', models.ImageField(blank=True, upload_to='static/imagenes')),
                ('fotoFrutos', models.ImageField(blank=True, upload_to='static/imagenes')),
                ('altura', models.IntegerField(default=0, verbose_name='Altura')),
                ('perimetro', models.IntegerField(default=0, verbose_name='Perimetro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('primerApellido', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('segundoApellido', models.CharField(max_length=30, verbose_name='Segundo Apellido')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('contrasenia', models.CharField(max_length=30, verbose_name='Contraseña')),
                ('tipo', models.CharField(choices=[('Administrador', 'Administrador'), ('Usuario', 'Usuario')], default='Usuario', max_length=30, verbose_name='Tipo')),
                ('activo', models.BooleanField(default=False, verbose_name='Activo')),
            ],
        ),
    ]