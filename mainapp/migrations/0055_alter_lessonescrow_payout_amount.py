# Generated by Django 3.2.13 on 2022-06-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0054_auto_20220629_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonescrow',
            name='payout_amount',
            field=models.IntegerField(default=0),
        ),
    ]