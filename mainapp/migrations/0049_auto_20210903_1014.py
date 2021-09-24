# Generated by Django 3.2.6 on 2021-09-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0048_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hide_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]