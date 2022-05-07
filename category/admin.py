from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Section)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'name']
    list_filter = ['category', ]

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subcategory', 'name']
    list_filter = ['subcategory']

admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Subject, SubjectAdmin)