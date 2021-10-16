# Generated by Django 3.2.7 on 2021-10-15 16:34

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField()),
                ('mission', ckeditor.fields.RichTextField()),
                ('vision', ckeditor.fields.RichTextField()),
                ('goal', ckeditor.fields.RichTextField()),
                ('bg', models.ImageField(blank=True, null=True, upload_to='bg_img')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HowToUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='how_img')),
                ('how_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='tram_img')),
                ('facebook', models.CharField(blank=True, max_length=256, null=True)),
                ('twitter', models.CharField(blank=True, max_length=256, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=256, null=True)),
                ('instagram', models.CharField(blank=True, max_length=256, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('passport', 'Passport'), ('national ID', 'National ID Card'), ('others', 'Others')], default='national ID', max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('photo_back', models.ImageField(default='media/default.png', upload_to='verifi')),
                ('photo_front', models.ImageField(default='media/default.png', upload_to='verifi')),
                ('is_verified', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('complete', 'complete'), ('in progress', 'in progress'), ('canceled', 'canceled')], max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Upgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('payment_method', models.CharField(choices=[('MTN Mobile Money', 'MTN Mobile Money'), ('Orange Money', 'Orange Money')], max_length=40)),
                ('phone_number', models.CharField(max_length=15)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('operator', models.CharField(blank=True, max_length=100, null=True)),
                ('operator_ref', models.CharField(blank=True, max_length=100, null=True)),
                ('external_ref', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge', models.CharField(blank=True, choices=[('Week', 'Weekly'), ('Month', 'Monthly'), ('Hour', 'Hourly')], max_length=30, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_category', to='category.category')),
                ('subcategory', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, related_name='user_subcategory', to='category.subcategory')),
                ('subject', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='subcategory', chained_model_field='subcategory', on_delete=django.db.models.deletion.CASCADE, related_name='user_subject', to='category.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=256, null=True)),
                ('instagram', models.CharField(blank=True, max_length=256, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=256, null=True)),
                ('website', models.CharField(blank=True, max_length=256, null=True)),
                ('youtube', models.CharField(blank=True, max_length=256, null=True)),
                ('github', models.CharField(blank=True, max_length=256, null=True)),
                ('twitter', models.CharField(blank=True, max_length=256, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=200)),
                ('certificate', models.CharField(max_length=200)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('still_studying', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileViewed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('viewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_view', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(blank=True, choices=[('tutor', "i'm a tutor"), ('student', "i'm a Student"), ('parent', "i'm a Parent")], max_length=10, null=True)),
                ('title', models.CharField(blank=True, choices=[('mr', 'Mr'), ('mrs', 'Mrs'), ('miss', 'Miss'), ('ms', 'Ms'), ('dr', 'Dr'), ('prof', 'Prof')], max_length=10, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address_1', models.CharField(max_length=50, null=True)),
                ('address_2', models.CharField(blank=True, max_length=50, null=True)),
                ('level_of_education', models.CharField(blank=True, choices=[('Bachelor Degree(Bac +3)', 'Bachelor Degree'), ('Master Degree(Bac +5)', 'Master Degree'), ('Advanced Level(Bac)', 'Advanced Level'), ('Doctorate', 'Doctorate'), ('HND', 'HND'), ('Others', 'Others')], max_length=50, null=True)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('paid', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(default='media/default.png', upload_to='profile_img')),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='region', chained_model_field='region', default=1, on_delete=django.db.models.deletion.CASCADE, to='location.city')),
                ('country', models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='location.country')),
                ('favourite', models.ManyToManyField(related_name='saved_user', to=settings.AUTH_USER_MODEL)),
                ('region', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', default=1, on_delete=django.db.models.deletion.CASCADE, to='location.region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('English', 'English'), ('French', 'French'), ('Others', 'Others')], max_length=30)),
                ('bio', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('charge', models.CharField(blank=True, choices=[('Week', 'Weekly'), ('Month', 'Monthly'), ('Hour', 'Hourly')], max_length=30, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_category', to='category.category')),
                ('subcategory', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='category', chained_model_field='category', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_subcategory', to='category.subcategory')),
                ('subject', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='subcategory', chained_model_field='subcategory', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_subject', to='category.subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_post', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('current_job', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('is_confirm', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
                ('user_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.day')),
                ('hour', models.ManyToManyField(to='mainapp.Hour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
