# Generated by Django 3.2.13 on 2022-06-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_chat_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
