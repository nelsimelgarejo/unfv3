# Generated by Django 3.2.8 on 2021-10-21 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsTopicos',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('item', models.TextField(max_length=2000)),
                ('topico', models.CharField(choices=[('sa_mental', 'SALUD MENTAL POSITIVA'), ('asertividad', 'ASERTIVIDAD'), ('das_ansiedad', 'ANSIEDAD'), ('das_estres', 'ESTRÉS'), ('das_depresion', 'DEPRESIÓN'), ('ap_social', 'APOYO SOCIAL'), ('vi_pareja', 'VIOLENCIA DE PAREJA')], max_length=20)),
                ('inverso', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('codigo_universitario', models.CharField(blank=True, max_length=20, null=True)),
                ('universidad', models.CharField(blank=True, choices=[('unfv', 'Universidad Nacional Federico Villareal'), ('red_acacia', 'Red Acacia')], max_length=20, null=True)),
                ('tipo_usuario', models.CharField(blank=True, choices=[('admin', 'Admin'), ('estudiante', 'Estudiante'), ('docente', 'Docente'), ('administrativo', 'Personal administrativo')], max_length=20, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoPerfil',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('topico', models.CharField(choices=[('sa_mental', 'SALUD MENTAL POSITIVA'), ('asertividad', 'ASERTIVIDAD'), ('das_ansiedad', 'ANSIEDAD'), ('das_estres', 'ESTRÉS'), ('das_depresion', 'DEPRESIÓN'), ('ap_social', 'APOYO SOCIAL'), ('vi_pareja', 'VIOLENCIA DE PAREJA')], max_length=100)),
                ('puntaje', models.FloatField(default=0.0)),
                ('resultado', models.CharField(blank=True, max_length=255)),
                ('estado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentirsebien.perfil')),
            ],
            options={
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='RespuestasPuente',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('respuesta', models.SmallIntegerField()),
                ('completado', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentirsebien.itemstopicos')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentirsebien.perfil')),
            ],
            options={
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='FichaSociodemografica',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('anio_ingreso', models.PositiveIntegerField(default=0)),
                ('anio_estudio_actual', models.CharField(blank=True, max_length=10, null=True)),
                ('is_becario', models.BooleanField(default=False)),
                ('facultad', models.CharField(blank=True, max_length=30, null=True)),
                ('escuela', models.CharField(blank=True, max_length=30, null=True)),
                ('sexo', models.CharField(blank=True, max_length=30, null=True)),
                ('genero', models.CharField(blank=True, max_length=30, null=True)),
                ('estado_civil', models.CharField(blank=True, max_length=30, null=True)),
                ('nacimiento_departamento', models.CharField(blank=True, max_length=30, null=True)),
                ('nacimiento_provincia', models.CharField(blank=True, max_length=30, null=True)),
                ('nacimiento_distrito', models.CharField(blank=True, max_length=30, null=True)),
                ('residencia_departamento', models.CharField(blank=True, max_length=30, null=True)),
                ('residencia_provincia', models.CharField(blank=True, max_length=30, null=True)),
                ('residencia_distrito', models.CharField(blank=True, max_length=30, null=True)),
                ('tipo_colegio', models.CharField(blank=True, max_length=30, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=30, null=True)),
                ('tiempo_lugar_residencia', models.PositiveIntegerField(default=0)),
                ('religion', models.CharField(blank=True, max_length=30, null=True)),
                ('nivel_socioeconomico', models.CharField(blank=True, max_length=30, null=True)),
                ('vives_solo', models.BooleanField(default=False)),
                ('vive_con', models.CharField(blank=True, max_length=100, null=True)),
                ('con_cuantos_vives', models.PositiveIntegerField(default=0)),
                ('situacion_ocupacional', models.CharField(blank=True, max_length=100, null=True)),
                ('situacion_de_trabajo', models.CharField(blank=True, max_length=100, null=True)),
                ('horas_apoyo_voluntariado', models.PositiveIntegerField(default=0)),
                ('problema_fisico', models.CharField(blank=True, max_length=255, null=True)),
                ('problema_psicologico', models.CharField(blank=True, max_length=255, null=True)),
                ('tuvo_atencion_psicologica', models.BooleanField(default=False)),
                ('sintomas_covid_19', models.BooleanField(default=False)),
                ('familiar_sintomas_covid_19', models.BooleanField(default=False)),
                ('tuvo_fallecimiento', models.CharField(blank=True, max_length=30, null=True)),
                ('tiempo_de_fallecimiento', models.PositiveIntegerField(default=0)),
                ('adaptado_clases_virtuales', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentirsebien.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='ComponenteBienestar',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('topico', models.CharField(choices=[('sa_mental', 'SALUD MENTAL POSITIVA'), ('asertividad', 'ASERTIVIDAD'), ('das_ansiedad', 'ANSIEDAD'), ('das_estres', 'ESTRÉS'), ('das_depresion', 'DEPRESIÓN'), ('ap_social', 'APOYO SOCIAL'), ('vi_pareja', 'VIOLENCIA DE PAREJA')], max_length=20)),
                ('completado', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('perfil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sentirsebien.perfil')),
            ],
            options={
                'ordering': ['-creado'],
            },
        ),
    ]
