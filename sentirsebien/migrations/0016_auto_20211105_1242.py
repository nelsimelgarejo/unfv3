# Generated by Django 3.2.8 on 2021-11-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentirsebien', '0015_auto_20211105_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retroalimentacion',
            name='retro_audio_url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='retroalimentacion',
            name='retro_video_url',
            field=models.TextField(),
        ),
    ]
