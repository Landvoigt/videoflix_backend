# Generated by Django 5.0.6 on 2024-06-25 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_user_id_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
