# Generated by Django 5.0.6 on 2024-06-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videostore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='hls_playlist',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
    ]