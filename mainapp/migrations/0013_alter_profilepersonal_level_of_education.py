# Generated by Django 3.2.7 on 2022-02-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_profilepersonal_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepersonal',
            name='level_of_education',
            field=models.CharField(blank=True, choices=[('Bachelor Degree(Bacc+3)', 'Bachelor Degree'), ('Master Degree(Bacc +5)', 'Master Degree'), ('Advanced Level(Bacc)', 'Advanced Level'), ('Doctorate', 'Doctorate'), ('HND', 'HND'), ('Others', 'Others')], max_length=50, null=True),
        ),
    ]
