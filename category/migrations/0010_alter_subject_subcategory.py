# Generated by Django 3.2.6 on 2021-09-08 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_auto_20210822_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subcategory'),
        ),
    ]