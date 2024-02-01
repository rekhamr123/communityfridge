from django.contrib import admin
from . models import admin_items
# Register your models here.
admin.site.register(admin_items),


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on')


