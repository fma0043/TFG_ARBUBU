# Generated by Django 2.2 on 2019-04-25 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEspecie', models.CharField(max_length=80, verbose_name='nombre_Especie')),
                ('caracteristicas', models.TextField(blank=True, verbose_name='Caracteristicas')),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantallaPrincipal.Familia')),
            ],
        ),
    ]
