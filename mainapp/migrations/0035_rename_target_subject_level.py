# Generated by Django 3.2.6 on 2021-08-21 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0034_auto_20210821_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='target',
            new_name='level',
        ),
    ]
