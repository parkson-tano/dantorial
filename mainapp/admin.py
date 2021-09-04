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


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['user', 'day']
    list_filter = ['hour', 'day']

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'work_post','position', 'start_date', 'end_date']

class QualificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'school', 'certificate', 'start_year', 'end_year']

admin.site.register(ProfilePersonal, ProfileAdmin)
admin.site.register(ProfileInfo, TutorProfileAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Day)
admin.site.register(Hour)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(SocialMedia)
admin.site.register(Booked)
admin.site.register(Verification)