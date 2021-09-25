from django.db import models
from django.contrib.auth.models import User
from review.models import Review
from django.contrib.sessions.models import Session
# Create your models here.

# class ThreadModel(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
# 	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

# class Notification(models.Model):
# 	# 1 = Like, 2 = Comment, 3 = Follow, #4 = DM
# 	notification_type = models.IntegerField()
# 	to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
# 	from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
# 	post = models.ForeignKey(TutorProfile, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
# 	review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
# 	thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
# 	date_created = models.DateTimeField(auto_now_add=True)
# 	user_has_seen = models.BooleanField(default=False)


# class MessageModel(models.Model):
# 	thread = models.ForeignKey(ThreadModel, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
# 	sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
# 	receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
# 	body = models.CharField(max_length=1000)
# 	image = models.ImageField(upload_to='uploads/message_photos', blank=True, null=True)
# 	date_created = models.DateTimeField(auto_now_add=True)
# 	is_read = models.BooleanField(default=False)


class Message(models.Model):
	sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
	receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	name = models.CharField(max_length=256, null=True, blank=True)
	email =models.EmailField(null=True, blank=True)
	phone_number = models.IntegerField()
	message = models.TextField()
	is_read = models.BooleanField(default=False)


	date_created = models.DateTimeField(auto_now_add=True)
