# Generated by Django 3.2.7 on 2022-03-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_auto_20220313_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='mode',
        ),
        migrations.AddField(
            model_name='onlinelesson',
            name='mode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
