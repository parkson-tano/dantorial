# Generated by Django 3.2.7 on 2022-02-06 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_remove_subject_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileinfo',
            name='experience',
        ),
    ]
