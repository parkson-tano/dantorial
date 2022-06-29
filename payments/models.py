from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    escrow_payment = models.BooleanField(default=False)
    purpose = models.CharField(max_length=20, null=True, blank=True)
    reference = models.CharField(null=True, blank=True, max_length=100)
    status = models.CharField(null=True, blank=True, max_length=100)
    reason = models.CharField(null=True, blank=True, max_length=100)
    code = models.CharField(null=True, blank=True, max_length=100)
    operator = models.CharField(null=True, blank=True, max_length=100)
    operator_ref = models.CharField(null=True, blank=True, max_length=100)
    external_ref = models.CharField(null=True, blank=True, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' payment'
