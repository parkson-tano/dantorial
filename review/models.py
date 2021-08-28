from django.db import models
from django.contrib.auth.models import User
from mainapp.models import ProfilePersonal
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    profile = models.ForeignKey(ProfilePersonal, on_delete=models.PROTECT, related_name='user_profile')
    content = models.TextField()
    rating = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.profile
