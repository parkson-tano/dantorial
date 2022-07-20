from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from mainapp.models import OnlineLesson
# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    lesson = models.ForeignKey(
        OnlineLesson, null=True, blank=True, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    withdrawal = models.BooleanField(default=False)
    reason_payment = models.CharField(max_length=30, null=True, blank=True)
    reference = models.CharField(null=True, blank=True, max_length=100)
    status = models.CharField(null=True, blank=True, max_length=100)
    reason = models.CharField(null=True, blank=True, max_length=100)
    code = models.CharField(null=True, blank=True, max_length=100)
    operator = models.CharField(null=True, blank=True, max_length=100)
    operator_ref = models.CharField(null=True, blank=True, max_length=100)
    external_ref = models.CharField(null=True, blank=True, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.user.profilepersonal.first_name)} {str(self.user.profilepersonal.last_name)}'
