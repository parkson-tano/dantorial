# Generated by Django 3.2.7 on 2021-11-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20211113_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchhistory',
            name='result',
        ),
        migrations.AddField(
            model_name='searchhistory',
            name='keyword',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
