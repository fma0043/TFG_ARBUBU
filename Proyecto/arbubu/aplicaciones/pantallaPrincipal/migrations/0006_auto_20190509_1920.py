# Generated by Django 2.2 on 2019-05-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0005_auto_20190509_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='distribucion',
            field=models.CharField(choices=[('AS', 'Asia'), ('AN', 'Antártida'), ('EU', 'Europa'), ('AF', 'África'), ('OC', 'Oceanía'), ('AM', 'América')], max_length=30, verbose_name='Distribucion'),
        ),
        migrations.AlterField(
            model_name='familia',
            name='nombre',
            field=models.CharField(choices=[('AC', 'Aceráceas'), ('AN', 'Anacardiáceas'), ('AQ', 'Aquifoliáceas'), ('BE', 'Betuláceas'), ('BU', 'Buxáceas'), ('CA', 'Caprifoliáceas'), ('CE', 'Celastráceas'), ('CO', 'Cornáceas'), ('CU', 'Cupresáceas'), ('EL', 'Eleagnáceas'), ('ER', 'Ericácas'), ('FA', 'Fagáceas'), ('JU', 'Juglandáceas'), ('LA', 'Lauráceas'), ('LE', 'Leguminosas'), ('ME', 'Meliáceas'), ('MI', 'Mirtáceas'), ('MO', 'Moráceas'), ('OL', 'Oleáceas'), ('PA', 'Palmáceas'), ('PI', 'Pináceas'), ('PL', 'Platanáceas'), ('PU', 'Punicáceas'), ('RA', 'Ramnáceas'), ('RO', 'Rosáceas'), ('SA', 'Salicáceas'), ('SI', 'Simaroubáceas'), ('SO', 'Solanáceas'), ('TA', 'Tamariacáceas'), ('TA', 'Taxáceas'), ('TI', 'Tiliáceas'), ('UL', 'Ulmáceas')], max_length=30, unique=True, verbose_name='Nombre'),
        ),
    ]