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
      'columns': 8,
			'required' : True
			}), 
        }
    labels = {
        'content' : ''
      }
