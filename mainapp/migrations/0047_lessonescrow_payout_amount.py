# Generated by Django 3.2.13 on 2022-06-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0046_onlinelesson_is_compelte'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonescrow',
            name='payout_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
