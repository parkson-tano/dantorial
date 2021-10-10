# Generated by Django 3.2.7 on 2021-10-07 21:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0073_auto_20211007_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepersonal',
            name='favourite',
            field=models.ManyToManyField(blank=True, null=True, related_name='saved_user', to=settings.AUTH_USER_MODEL),
        ),
    ]