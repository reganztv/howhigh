# Generated by Django 4.1.4 on 2022-12-26 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_project_likes_project_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.date(2022, 12, 26)),
        ),
    ]