from re import S
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from PIL import Image
# Create your models here.

# class Section(models.Model):
#     name = models.CharField(max_length=30)
#     slug = AutoSlugField(populate_from='name')
#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("dantorial:sectcion_detail", kwargs={"slug": self.slug})
    
class Category(models.Model):
    # section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to='category_image', default='default.png')
    date_created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("dantorial:category", kwargs={"slug": self.slug})
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.height >200 or img.width>200:
    #         output_size = (200,200)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to='subcategory_image', default='default.png')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("dantorial:subcategory", kwargs={"category_slug": self.category.slug, 'subcat_slug': self.id})
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.height >200 or img.width>200:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
class Subject(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length = 40)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to='subject_image', default='default.png')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dantorial:subject", kwargs={"category_slug": self.subcategory.category.slug, 'subcat_slug': self.subcategory.id, "subject_slug": self.slug})
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.height >200 or img.width>200:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)