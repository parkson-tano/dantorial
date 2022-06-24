# Generated by Django 3.2.13 on 2022-06-01 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0043_lessonescrow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('successful', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('escrow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.lessonescrow')),
            ],
        ),
    ]