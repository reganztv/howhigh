# Generated by Django 4.1.4 on 2023-01-07 16:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_article_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
