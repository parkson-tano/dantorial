from django.contrib import admin
from .models import Payment
# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('__str__','withdrawal', 'operator', 'status')
    list_filter = ('withdrawal','operator')
