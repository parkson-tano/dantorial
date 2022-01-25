from django.contrib import admin
from .models import *
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    # list_filter = ['name' ]

class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name', 'country']
    list_display = ['name', 'country']
    # list_filter = ['name', 'country']

class TownAdmin(admin.ModelAdmin):
    search_fields = ['name', 'region', 'id']
    list_display = ['name', 'region', 'id']
    # list_filter = ['region' , 'id']

class QuaterAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name', ]
    # list_filter = ['name', 'town']

admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(Quater, QuaterAdmin)
admin.site.register(Address)