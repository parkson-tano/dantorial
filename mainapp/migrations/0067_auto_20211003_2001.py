# Generated by Django 3.2.7 on 2021-10-03 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0066_howtouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='current_job',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='qualification',
            name='still_studying',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='upgrade',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
