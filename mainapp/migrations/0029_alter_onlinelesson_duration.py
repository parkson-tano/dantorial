# Generated by Django 3.2.7 on 2022-03-13 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0028_auto_20220313_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinelesson',
            name='duration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
