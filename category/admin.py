from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Section)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'name']
    list_filter = ['category', ]

admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Subject)