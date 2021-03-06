# Generated by Django 2.2.6 on 2019-10-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('idEspecie', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCientificoEspecie', models.CharField(max_length=30, unique=True, verbose_name='Nombre Cientifico')),
                ('nombreComunEspecie', models.CharField(max_length=30, unique=True, verbose_name='Nombre Común')),
                ('autoctona', models.BooleanField(default=False, verbose_name='Autóctona')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('ecologia', models.TextField(verbose_name='Ecologia')),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('idFamilia', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreFamilia', models.CharField(choices=[('Aceráceas', 'Aceráceas'), ('Anacardiáceas', 'Anacardiáceas'), ('Aquifoliáceas', 'Aquifoliáceas'), ('Betuláceas', 'Betuláceas'), ('Buxáceas', 'Buxáceas'), ('Caprifoliáceas', 'Caprifoliáceas'), ('Celastráceas', 'Celastráceas'), ('Cornáceas', 'Cornáceas'), ('Cupresáceas', 'Cupresáceas'), ('Eleagnáceas', 'Eleagnáceas'), ('Ericácas', 'Ericácas'), ('Fagáceas', 'Fagáceas'), ('Juglandáceas', 'Juglandáceas'), ('Lauráceas', 'Lauráceas'), ('Leguminosas', 'Leguminosas'), ('Meliáceas', 'Meliáceas'), ('Mirtáceas', 'Mirtáceas'), ('Moráceas', 'Moráceas'), ('Oleáceas', 'Oleáceas'), ('Palmáceas', 'Palmáceas'), ('Pináceas', 'Pináceas'), ('Platanáceas', 'Platanáceas'), ('Punicáceas', 'Punicáceas'), ('Ramnáceas', 'Ramnáceas'), ('Rosáceas', 'Rosáceas'), ('Salicáceas', 'Salicáceas'), ('Simaroubáceas', 'Simaroubáceas'), ('Solanáceas', 'Solanáceas'), ('Tamariacáceas', 'Tamariacáceas'), ('Taxáceas', 'Taxáceas'), ('Tiliáceas', 'Tiliáceas'), ('Ulmáceas', 'Ulmáceas')], max_length=30, unique=True, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('primerApellido', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('segundoApellido', models.CharField(max_length=30, verbose_name='Segundo Apellido')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('contrasenia', models.CharField(max_length=30, verbose_name='Contraseña')),
                ('tipo', models.CharField(choices=[('Administrador', 'Administrador'), ('Usuario', 'Usuario')], default='Usuario', max_length=30, verbose_name='Tipo')),
                ('activo', models.BooleanField(default=False, verbose_name='Activo')),
            ],
        ),
        migrations.CreateModel(
            name='Individuos',
            fields=[
                ('idIndividuo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreComun', models.CharField(max_length=30, unique=True, verbose_name='Nombre Común')),
                ('motivoSingular', models.CharField(choices=[('Antigüedad', 'Antigüedad'), ('Elevado Diámetro', 'Elevado Diámetro'), ('Plantado por un personaje histórico', 'Plantado por un personaje histórico'), ('Vistosidad', 'Vistosidad'), ('Madera codiciada', 'Madera codiciada'), ('Frutos peculiares', 'Frutos peculiares'), ('Utilidad medicinal', 'Utilidad medicinal')], max_length=50, verbose_name='Motivo de Singularidad')),
                ('explicacionMotivoSingular', models.TextField(verbose_name='Explicacion de Singularidad')),
                ('x', models.DecimalField(decimal_places=15, default=1, max_digits=19, verbose_name='X')),
                ('y', models.DecimalField(decimal_places=15, default=1, max_digits=19, verbose_name='Y')),
                ('fotoArbol', models.ImageField(upload_to='static/imagenes')),
                ('fotoHojas', models.ImageField(blank=True, upload_to='static/imagenes')),
                ('fotoTronco', models.ImageField(blank=True, upload_to='static/imagenes')),
                ('fotoFrutos', models.ImageField(blank=True, upload_to='static/imagenes')),
                ('altura', models.DecimalField(decimal_places=15, default=0, max_digits=19, verbose_name='Altura')),
                ('perimetro', models.DecimalField(decimal_places=15, default=0, max_digits=19, verbose_name='Perimetro')),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Especie')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreGenero', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Familia')),
            ],
        ),
        migrations.AddField(
            model_name='especie',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Genero'),
        ),
    ]
