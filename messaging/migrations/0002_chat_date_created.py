# Generated by Django 3.2.13 on 2022-06-20 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]