from django.db import models
from mainapp.models import ProfilePersonal
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey(
        ProfilePersonal, on_delete=models.CASCADE, related_name='user_profile')
    content = models.TextField()
    rating = models.CharField(max_length=2, null=True,
                              blank=True, choices=RATING)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.profile)

    # def average_rating(self):
    #     all_rating = list(map(lambda x: x.rating, self.review_set.all()))
    #     return np.mean(all_rating)
