# Generated by Django 2.2.6 on 2019-11-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20191107_1132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genero',
            options={'ordering': ['nombreGenero']},
        ),
        migrations.AlterField(
            model_name='especie',
            name='nombreCientificoEspecie',
            field=models.CharField(max_length=40, verbose_name='Nombre Cientifico'),
        ),
        migrations.AlterField(
            model_name='familia',
            name='nombreFamilia',
            field=models.CharField(choices=[('Aceráceas', 'Aceráceas'), ('Adoxáceas', 'Adoxáceas'), ('Anacardiáceas', 'Anacardiáceas'), ('Aquifoliáceas', 'Aquifoliáceas'), ('Araliáceas', 'Araliáceas'), ('Betuláceas', 'Betuláceas'), ('Buxáceas', 'Buxáceas'), ('Bignoniáceas', 'Bignoniáceas'), ('Caprifoliáceas', 'Caprifoliáceas'), ('Celastráceas', 'Celastráceas'), ('Cornáceas', 'Cornáceas'), ('Cupresáceas', 'Cupresáceas'), ('Eleagnáceas', 'Eleagnáceas'), ('Ericácas', 'Ericácas'), ('Fagáceas', 'Fagáceas'), ('Fabaceaes', 'Fabaceaes'), ('Juglandáceas', 'Juglandáceas'), ('Lauráceas', 'Lauráceas'), ('Leguminosas', 'Leguminosas'), ('Magnoliáceas', 'Magnoliáceas'), ('Malvaceae', 'Malvaceae'), ('Meliáceas', 'Meliáceas'), ('Mirtáceas', 'Mirtáceas'), ('Moráceas', 'Moráceas'), ('Oleáceas', 'Oleáceas'), ('Palmáceas', 'Palmáceas'), ('Pináceas', 'Pináceas'), ('Pinus', 'Pinus'), ('Platanáceas', 'Platanáceas'), ('Punicáceas', 'Punicáceas'), ('Ramnáceas', 'Ramnáceas'), ('Rosáceas', 'Rosáceas'), ('Salicáceas', 'Salicáceas'), ('Simaroubáceas', 'Simaroubáceas'), ('Solanáceas', 'Solanáceas'), ('Tamariacáceas', 'Tamariacáceas'), ('Taxáceas', 'Taxáceas'), ('Tiliáceas', 'Tiliáceas'), ('Ulmáceas', 'Ulmáceas')], max_length=30, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='fotoGenero',
            field=models.ImageField(blank=True, upload_to='static/imagenes'),
        ),
    ]