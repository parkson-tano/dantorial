from django.contrib import admin
from .models import *
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender_user','name', 'receiver_user', 'date_created' ]

admin.site.register(Message, MessageAdmin)