# Generated by Django 3.2.7 on 2022-02-11 22:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_remove_profilepersonal_quater'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy_policy', ckeditor.fields.RichTextField()),
                ('terms', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
