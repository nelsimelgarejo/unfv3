# Generated by Django 3.2.8 on 2021-10-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentirsebien', '0008_auto_20211021_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichasociodemografica',
            name='anio_estudio_actual',
            field=models.CharField(blank=True, choices=[('anio1', 'Año 1'), ('anio2', 'Año 2'), ('anio3', 'Año 3'), ('anio4', 'Año 4'), ('anio5', 'Año 5'), ('anio6', 'Año 6'), ('egresado', 'Egresado')], max_length=10, null=True),
        ),
    ]
