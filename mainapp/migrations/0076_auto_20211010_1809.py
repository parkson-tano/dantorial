# Generated by Django 3.2.7 on 2021-10-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0075_alter_profilepersonal_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='charge',
            field=models.CharField(blank=True, choices=[('Week', 'Week'), ('Month', 'Month'), ('Hour', 'Hour')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='charge',
            field=models.CharField(blank=True, choices=[('Week', 'Week'), ('Month', 'Month'), ('Hour', 'Hour')], max_length=30, null=True),
        ),
    ]