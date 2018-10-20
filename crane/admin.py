from django.contrib import admin
from .models import ContactMessage


# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('names', 'email')
    list_display = (
        'name', 'email', 'phone_number', 'subject', 'read_message', 'sent_at', 'read')
    exclude = ('names', 'email', 'phone_number', 'subject', 'message', 'sent_at', 'read')


admin.site.register(ContactMessage, ContactMessageAdmin)
