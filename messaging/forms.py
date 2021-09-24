from django import forms
from django.contrib.auth.models import User
from .models import *

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('name', 'email', 'phone_number', 'message')