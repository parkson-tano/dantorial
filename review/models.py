from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'review_tutor')
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
    rating = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    date_created = models.DateTimeField(auto_now_add=True)
    
    @property
    def children(self):
        return Review.objects.filter(parent=self).order_by('-date_created').all()
        
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False