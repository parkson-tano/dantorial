# Generated by Django 3.2.13 on 2022-09-20 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_rename_personalrooms_personalroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalmessage',
            name='chatroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.personalroom'),
        ),
    ]
