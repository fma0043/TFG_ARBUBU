# Generated by Django 2.2 on 2019-04-25 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0003_auto_20190425_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='familia',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pantallaPrincipal.Familia'),
        ),
        migrations.AlterField(
            model_name='individuos',
            name='especie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pantallaPrincipal.Especie'),
        ),
    ]
