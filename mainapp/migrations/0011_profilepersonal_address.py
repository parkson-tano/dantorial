# Generated by Django 3.2.7 on 2022-01-25 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20220125_0424'),
        ('mainapp', '0010_auto_20211126_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepersonal',
            name='address',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='location.address'),
        ),
    ]
