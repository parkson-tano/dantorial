from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
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
    date_created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dantorial:category_detail", kwargs={"slug": self.slug})

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dantorial:subcategory_detail", kwargs={"category_slug": self.category.slug, 'subcat_slug': self.slug})

class Subject(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length = 40)
    slug = AutoSlugField(populate_from='name')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dantorial:subject_detail", kwargs={"slug": self.slug})