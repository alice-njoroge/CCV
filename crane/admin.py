from django.contrib import admin
from .models import ContactMessage


# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('customer_names', 'customer_email')
    list_display = (
        'customer_names', 'customer_email', 'customer_phone', 'message_subject', 'read_message', 'sent_at', 'read')
    exclude = ('customer_names', 'customer_email', 'customer_phone', 'message_subject', 'message', 'sent_at', 'read')


admin.site.register(ContactMessage, ContactMessageAdmin)
