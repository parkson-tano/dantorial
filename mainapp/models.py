from django.db import models
from django.db.models.base import Model
from django.views.generic.edit import CreateView
from category.models import *
from django.contrib.auth.models import User
from PIL import Image
from location.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from smart_selects.db_fields import ChainedForeignKey
from ckeditor.fields import RichTextField
import numpy as np
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

DOC = (
    ('passport', 'Passport'),
    ('national ID', 'National ID Card'),
    ('others', 'Others')
)

STA = (
    ('complete', 'complete'),
    ('in progress', 'in progress'),
    ('canceled', 'canceled')
    )

PAYMENT = (
    ('MTN Mobile Money', 'MTN Mobile Money'),
    ('Orange Money', 'Orange Money'),
    # ('YUP', 'yup'),
    # ('VISA', 'visa'),
    )

# User._meta.get_field('username')._unique = False

# day = (
#     ('monday','monday'),
#     ('tuesday', 'tuesday'),
#     ('wednesday', 'wednesday'),
#     ('thursday', 'thursday'),
#     ('friday', 'friday'),
#     ('sat')
# )

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
    city =  ChainedForeignKey(City, chained_field="region",
        chained_model_field="region",
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
    view_count = models.PositiveIntegerField(default=0)
    paid = models.BooleanField(default = False)
    favourite = models.ManyToManyField(User, null=True, blank=True, related_name='saved_user' )
    profile_pic = models.ImageField(upload_to='profile_img', default='media/default.png')
    

    @property
    def total_favourites(self):
        return self.favourite.count()
    

    def __str__(self):
        return self.user.username + " profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)
        if img.height >200 or img.width>200:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)



@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        ProfilePersonal.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profilepersonal.save()

class ProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=30, choices=LANG)
    bio = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name ='main_category')
    subcategory = ChainedForeignKey(SubCategory, chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True, null=True, blank=True, related_name="main_subcategory")    
    subject = ChainedForeignKey(Subject, chained_field="subcategory",
        chained_model_field="subcategory",
        show_all=False,
        auto_choose=True,
        sort=True, null=True, blank=True, related_name="main_subject")
    # level = models.CharField(max_length=30, choices=TAG, null=True, blank=True)
    charge = models.CharField(max_length=30, choices=CHARGE, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)

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
    # level = models.CharField(max_length=30, choices=TAG, null=True, blank=True)
    charge = models.CharField(max_length=30, choices=CHARGE, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    work_post = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    current_job = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + ' experience'

class Qualification(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    school = models.CharField(max_length=200)
    certificate = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    still_studying = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='qua_img', null=True, blank=True)

    def __str__(self):
        return str(self.user) + ' qualification'

class SocialMedia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=256, null=True, blank=True)
    instagram = models.CharField(max_length=256, null=True, blank=True)
    linkedin = models.CharField(max_length=256, null=True, blank=True)
    website = models.CharField(max_length=256, null=True, blank=True)
    youtube = models.CharField(max_length=256, null=True, blank=True)
    github = models.CharField(max_length=256, null=True, blank=True)
    twitter = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.user) + ' social media'

class Day(models.Model):
    day = models.CharField(max_length=30)

    def __str__(self):
        return self.day

class Hour(models.Model):
    hour = models.CharField(max_length=30)

    def __str__(self):
        return self.hour

class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.PROTECT)
    hour = models.ManyToManyField(Hour)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' available'

class Verification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50, choices = DOC, default='national ID')
    number = models.CharField(max_length=50)
    photo_back = models.ImageField(upload_to = 'verifi', default='media/default.png')
    photo_front = models.ImageField(upload_to='verifi', default='media/default.png')
    is_verified = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STA)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' verification'

class Booked(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor') 
    amount = models.IntegerField()
    is_confirm = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

class Upgrade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    # start_date = models.DateTimeField(auto_now_add=True)
    # end_date =models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=40, choices=PAYMENT)
    phone_number = models.CharField(max_length=15)
    reference = models.CharField(null=True, blank=True, max_length=100)
    status = models.CharField(null=True, blank=True, max_length=100)
    reason = models.CharField(null=True, blank=True, max_length=100)
    code = models.CharField(null=True, blank=True, max_length=100)
    operator = models.CharField(null=True, blank=True, max_length=100)
    operator_ref = models.CharField(null=True, blank=True, max_length=100)
    external_ref = models.CharField(null=True, blank=True, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' upgrade'

class About(models.Model):
    about = RichTextField()
    mission = RichTextField()
    vision = RichTextField()
    goal = RichTextField()

    bg = models.ImageField(upload_to='bg_img', null=True, blank=True)

class OurTeam(models.Model):
    name = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    pic = models.ImageField(upload_to='tram_img', null=True, blank=True)
    facebook = models.CharField(max_length=256, null=True, blank=True)
    twitter = models.CharField(max_length=256, null=True, blank=True)
    linkedin = models.CharField(max_length=256, null=True, blank=True)
    instagram = models.CharField(max_length=256, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HowToUse(models.Model):
    image = models.ImageField(upload_to='how_img')
    how_text = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height >200 or img.width>200:
            output_size = (150,150)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class ProfileViewed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    viewed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_view', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)