# Generated by Django 3.2.7 on 2021-09-27 12:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0060_about_ourteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='vision',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
