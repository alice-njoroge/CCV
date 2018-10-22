from django.contrib import admin
from .models import ContactMessage, Carousel, HomeRight
from django.contrib import messages


# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('names', 'email')
    list_display = (
        'name', 'email', 'phone_number', 'subject', 'read_message', 'sent_at', 'read')
    exclude = ('names', 'email', 'phone_number', 'subject', 'message', 'sent_at', 'read')


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'caption', 'position')
    radio_fields = {"position": admin.HORIZONTAL}

    def has_add_permission(self, request):
        if Carousel.objects.count() > 4:
            return False
        return True


class HomeRightAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'title', 'subtitle')

    def has_add_permission(self, request):
        if HomeRight.objects.count() > 3:
            return False
        return True

    def save_model(self, request, obj, form, change):
        object = super(HomeRightAdmin, self).save_model(request=request, obj=obj, form=form, change=change)
        count = HomeRight.objects.count()
        if count <= 3:
            remaining = 4 - count
            self.message_user(request, f'{remaining} more images to go! please keep adding!', level=messages.WARNING)
            return object


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(HomeRight, HomeRightAdmin)

admin.site.site_title = 'CCV Admin'
admin.site.site_header = 'CCV Admin'
