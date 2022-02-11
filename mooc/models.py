from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

PAYMENT = (
    ('MTN Mobile Money', 'MTN Mobile Money'),
    ('Orange Money', 'Orange Money'),
    # ('YUP', 'yup'),
    # ('VISA', 'visa'),
    )

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course:category_detail", kwargs={"slug": self.slug})

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    slug = AutoSlugField(populate_from='name')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course:subcategory_detail", kwargs={"category_slug": self.category.slug, 'subcategory_slug':self.slug})
    
class Course(models.Model):
    CHARGE = (
    ('FREE', 'FREE'),
    ('PAID', 'PAID'),
    )

    LEARNER = (
        ('All', 'all'),
        ('Beginners', 'beginner'),
        ('Intermediate', 'intermediate'),
        ('Advanced', 'advanced'),
        ('Professional', 'professional'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=60)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='course_image', blank=True, null=True)
    cover_video = models.FileField(upload_to='course_video', blank=True, null=True) 
    charge = models.CharField(max_length=20, choices=CHARGE, default='FREE')
    price = models.PositiveIntegerField(blank=True, null=True)
    target_audience = models.CharField(max_length=40, choices = LEARNER, default='all')
    language = models.CharField(max_length=600, choices=(('English', 'English'),('French', 'French')), default='English')
    apply_discount = models.FloatField(default=0)
    attended_no = models.PositiveIntegerField(default=0)
    view_count = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course:course_detail", kwargs={"slug": self.slug})

class Competence(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    competence_1 = models.TextField(blank=True, null=True)
    competence_2 = models.TextField(blank=True, null=True)
    competence_3 = models.TextField(blank=True, null=True)
    competence_4 = models.TextField(blank=True, null=True)
    competence_5 = models.TextField(blank=True, null=True)

    def __str__(self):
        self.course 

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length=254, null=True, blank=True)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("course:chapter_deatil", kwargs={"slug": self.slug})
    
class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=260)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='lesson_image', blank=True, null=True)
    video =models.FileField(upload_to='lesson_video', blank=True, null=True)
    position = models.PositiveIntegerField(default=0, null=True)
    view_count = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course:lesson_detail", kwargs={"chapter_slug": self.chapter.slug, "lesson_slug": self.slug })
    

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.profilepersonal.first_name

class Payment(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
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
        return str(self.enrollment.profilepersonal.first_name) + ' payment'
