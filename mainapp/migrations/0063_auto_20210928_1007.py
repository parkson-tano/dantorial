# Generated by Django 3.2.7 on 2021-09-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0062_alter_about_vision'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='facebook',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='instagram',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='linkedin',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='twitter',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
