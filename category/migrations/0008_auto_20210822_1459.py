# Generated by Django 3.2.6 on 2021-08-22 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_auto_20210822_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='image',
        ),
    ]
