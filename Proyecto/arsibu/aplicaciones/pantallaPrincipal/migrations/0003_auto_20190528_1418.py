# Generated by Django 2.2.1 on 2019-05-28 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0002_auto_20190528_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individuos',
            name='nombreComun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantallaPrincipal.Especie'),
        ),
    ]