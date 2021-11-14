# Generated by Django 3.2.7 on 2021-11-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20211108_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepersonal',
            name='online_lesson',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profilepersonal',
            name='show_whatsapp_number',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profilepersonal',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
