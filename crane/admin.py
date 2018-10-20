from django.contrib import admin
from .models import ContactMessage, Carousel


# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('names', 'email')
    list_display = (
        'name', 'email', 'phone_number', 'subject', 'read_message', 'sent_at', 'read')
    exclude = ('names', 'email', 'phone_number', 'subject', 'message', 'sent_at', 'read')


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'position')
    radio_fields = {"position": admin.HORIZONTAL}

    def has_add_permission(self, request):
        if Carousel.objects.count() > 4:
            return False
        return True


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Carousel, CarouselAdmin)


admin.site.site_title = 'CCV Admin'
admin.site.site_header = 'CCV Admin'
