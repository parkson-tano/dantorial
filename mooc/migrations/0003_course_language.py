# Generated by Django 3.2.7 on 2022-02-08 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0002_auto_20220208_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('French', 'French')], default='English', max_length=600),
        ),
    ]
