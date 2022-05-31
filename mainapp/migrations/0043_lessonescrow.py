# Generated by Django 3.2.13 on 2022-05-31 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0042_alter_onlinelesson_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonEscrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payout', models.BooleanField(default=False)),
                ('refund', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('reason', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.lessonpayment')),
            ],
        ),
    ]
