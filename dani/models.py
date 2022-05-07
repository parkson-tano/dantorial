from django.db import models

# Create your models here.

class Carousel(models.Model):
    image = models.ImageField(upload_to='images/carousel')
    text  = models.TextField()

