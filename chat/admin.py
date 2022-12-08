from django.contrib import admin
from .models import PersonalRoom, PersonalMessage

# Register your models here.


class PersonalMessageInline(admin.TabularInline):
    model = PersonalMessage


class UserRoomAdmin(admin.ModelAdmin):
    inlines = [PersonalMessageInline]

    class Meta:
        model = PersonalRoom


admin.site.register(PersonalRoom, UserRoomAdmin)
admin.site.register(PersonalMessage)
