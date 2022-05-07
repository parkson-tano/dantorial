from django import forms
from django.contrib.auth.models import User
from .models import *

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ('content',)
    
    widgets = {
      "content": forms.Textarea(attrs= { 
			'name' : 'content',
			'class': 'form-control',
			'id': 'floatingInput',
      'rows': 8,
      'columns': 6,
			'required' : True,
      'placeholder': 'Type Your Comment here'
			}), 
        }
    labels = {
        'content' : ''
      }
