# Generated by Django 3.2.6 on 2021-09-06 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0056_auto_20210906_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
