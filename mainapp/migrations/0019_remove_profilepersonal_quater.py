# Generated by Django 3.2.7 on 2022-02-08 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_remove_profileinfo_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepersonal',
            name='quater',
        ),
    ]
