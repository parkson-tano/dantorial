from django.db import models
from category.models import *
from django.contrib.auth.models import User
from PIL import Image
from location.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

EL = (
    ('Bachelor Degree(Bac +3)', 'Bachelor Degree'),
    ('Master Degree(Bac +5)', 'Master Degree'),
    ('Advanced Level(Bac)', 'Advanced Level'),
    ('Doctorate', 'Doctorate'),
    ('HND', 'HND'),
    ('Others', 'Others'),
)

TAG = (
    ('Nursery', 'Nursery'),
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
    ('High School', 'High School'),
    ('University', 'University'),
    ('Others', 'Others')
)

CHARGE = (
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
    ('Hourly', 'Hourly')
)

LANG = (
    ('English', 'English'),
    ('French', 'French'),
    ('Others', 'Others')
)

TITLE = (
    ('mr', 'Mr'),
    ('mrs', 'Mrs'),
    ('miss', "Miss"),
    ('ms', 'Ms'),
    ('dr', 'Dr'),
    ('prof', 'Prof')
)


ACC = (
    ('tutor',"i'm a tutor"),
    ('student',"i'm a Student"),
    ('parent',"i'm a Parent")
)

GENDER = (
    ('male', 'Male'), 
    ('female', 'Female')
)

class ProfilePersonal(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACC, null=True, blank=True)
    title = models.CharField(max_length=10, choices=TITLE, null=True, blank=True )
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    first_name = models.CharField(max_length=30,null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default='1')
    region = ChainedForeignKey(Region, chained_field="country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        sort=True,
        default=1)
    # subregion = ChainedForeignKey(SubRegion, chained_field="region",
    #     chained_model_field="region",
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True)
    # city = ChainedForeignKey(City, chained_field="subregion",
    #     chained_model_field="subregion",
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True)
    date_of_birth = models.DateField(default=timezone.now)
    address_1 = models.CharField(max_length=50, null=True)
    address_2 = models.CharField(max_length=50, null=True, blank=True)
    level_of_education = models.CharField(max_length=50, choices=EL, null=True, blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    profile_pic = models.ImageField(upload_to='profile_img', default='media/default.png')


    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.profile_pic.path)
    #     if img.height >100 or img.width>100:
    #         output_size = (200,200)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_pic.path)

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        ProfilePersonal.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profilepersonal.save()

class ProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    language = models.CharField(max_length=30, choices=LANG, default=1)
    bio = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} profile information'

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        ProfileInfo.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profileinfo.save()

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name ='user_category')
    subcategory = ChainedForeignKey(SubCategory, chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True, related_name="user_subcategory")
    
    subject = ChainedForeignKey(Subject, chained_field="subcategory",
        chained_model_field="subcategory",
        show_all=False,
        auto_choose=True,
        sort=True, related_name="user_subject")
    level = models.CharField(max_length=30, choices=TAG, null=True, blank=True)
    charge = models.CharField(max_length=30, choices=CHARGE, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username
 