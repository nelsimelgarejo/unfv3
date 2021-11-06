# Generated by Django 3.2.8 on 2021-10-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentirsebien', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataUNFV',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('facultad', models.CharField(max_length=255)),
                ('escuela', models.CharField(max_length=255)),
                ('codigo_estudiante', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('dni', models.CharField(blank=True, max_length=20, null=True)),
                ('nombre_completo', models.CharField(max_length=255)),
                ('estado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-creado'],
            },
        ),
    ]
