from django.contrib import admin
from .models import *
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender_user','is_read', 'receiver_user', 'date_created' ]

class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name','email','date_created' ]


admin.site.register(Message, MessageAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Chat)