# Generated by Django 3.2.7 on 2022-03-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_alter_onlinelesson_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinelesson',
            name='duration',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
