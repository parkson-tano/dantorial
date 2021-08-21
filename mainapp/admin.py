from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','account_type', 'first_name', 'phone_number', 'region', 'level_of_education' ]
    list_filter = ['account_type','region', 'level_of_education' ]


class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'language',]
    list_filter = ['language']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject']
    list_filter = ['subject', 'category', 'subcategory']

admin.site.register(ProfilePersonal, ProfileAdmin)
admin.site.register(ProfileInfo, TutorProfileAdmin)
admin.site.register(Subject, SubjectAdmin)
