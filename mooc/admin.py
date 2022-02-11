from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_created']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'date_created']
    list_filter = ['category', 'date_created']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'price', 'target_audience']
    list_filter = ['category', 'subcategory', 'target_audience']

class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'position', 'view_count']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['chapter','title','position','view_count']

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student','course','complete']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['enrollment','is_complete','amount']

admin.site.register(Competence)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)