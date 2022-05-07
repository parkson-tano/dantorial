# Generated by Django 3.2.7 on 2022-03-12 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_rename_like_profilepersonal_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booked',
            old_name='user_1',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='booked',
            old_name='user_2',
            new_name='teacher',
        ),
        migrations.RemoveField(
            model_name='booked',
            name='amount',
        ),
        migrations.AddField(
            model_name='booked',
            name='mode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='booked',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='OnlineLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.booked')),
            ],
        ),
    ]
