from django import forms
from django.contrib.auth.models import User
from .models import *

class ReviewForm(admin.ModelAdmin):
  class Meta:
    model = Review
    fields = ('content', 'rating')
