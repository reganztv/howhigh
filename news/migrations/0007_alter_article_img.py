# Generated by Django 4.1.4 on 2023-01-07 16:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_article_body_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
