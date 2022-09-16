from django.contrib import admin
from .models import *
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
class UserAdmin(BaseUserAdmin):
    # form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )
admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_type', 'first_name',
                    'phone_number', 'level_of_education']
    list_filter = ['account_type', 'level_of_education']


class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'language', ]
    list_filter = ['language']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'subject', 'category', 'subcategory']
    list_filter = ['subject', 'category', 'subcategory']


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'day']
    list_filter = ['hour', 'day']


class OnlineLessonAdmin(admin.ModelAdmin):
    list_display = ['student', 'teacher', 'is_confirm', 'is_decline']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'work_post', 'position', 'start_date', 'end_date']


class QualificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'school', 'certificate', 'start_year', 'end_year']


# class UpgradeAdmin(admin.ModelAdmin):
#     search_fields = ['user__username', 'operator', 'status']
#     list_filter = ['user', 'operator', 'status', 'date_created']
#     list_display = ['user', 'amount', 'operator', 'status', 'date_created']


class ProfileViewedAdmin(admin.ModelAdmin):
    search_fields = ['user', 'user_by']
    list_filter = ['user', 'viewed_by', 'date_created']
    list_display = ['user', 'viewed_by', 'date_created']


class LessonEscrowAdmin(admin.ModelAdmin):
    # search_fields = ['user', 'teacher', 'status']
    list_filter = ['payout', 'refund', 'complete', 'payment_method']
    list_display = ['__str__', 'payout',
                    'refund', 'complete', 'payment_method']


class BillingPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment', 'billing')


admin.site.register(BillingPayment, BillingPaymentAdmin)
admin.site.register(ProfilePersonal, ProfileAdmin)
admin.site.register(ProfileInfo, TutorProfileAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Day)
admin.site.register(Hour)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(SocialMedia)
# admin.site.register(Booked)
admin.site.register(Verification)
admin.site.register(LessonEscrow, LessonEscrowAdmin)
admin.site.register(ProfileViewed, ProfileViewedAdmin)
admin.site.register(OnlineLesson, OnlineLessonAdmin)
admin.site.register([About, OurTeam,  HowToUse, SearchHistory,
                    Privacy, Contract, AccountBalance])
