from django.contrib import admin
from django.contrib import messages

from .models import (ContactMessage,
                     Carousel, HomeRight,
                     Welcome, DonationPledge,
                     Service, Team, Testimonial,
                     AboutUs, WhatWeDo, Activities,
                     Project)


# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('names', 'email')
    list_display = (
        'name', 'email', 'phone_number', 'subject', 'read_message', 'sent_at', 'read')
    exclude = ('names', 'email', 'phone_number', 'subject', 'message', 'sent_at', 'read')


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('caption', 'sub_caption', 'image_url', 'position')
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


class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        if Welcome.objects.count() > 4:
            return False
        return True


class DonationPledgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'amount', 'pledged_on', 'action')
    list_display_links = ('action',)
    fields = ('name', ('email', 'phone'), 'amount', ('pledged_on', 'when'), 'extra')

    def action(self, obj):
        return 'edit'


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'name', 'image_url', 'added_on')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'avatar_url', 'created_at', 'action')
    list_display_links = ('action',)

    def action(self, obj):
        return 'edit'


class WhatWeDoInlineAdmin(admin.TabularInline):
    model = WhatWeDo
    verbose_name_plural = 'what we do'
    fields = ('title',)
    extra = 1


class ActivitiesInlineAdmin(admin.TabularInline):
    model = Activities
    verbose_name_plural = 'Activities'
    fields = ('title',)
    extra = 1


class AboutUsAdmin(admin.ModelAdmin):
    inlines = [WhatWeDoInlineAdmin, ActivitiesInlineAdmin]
    list_display = ('title', 'image_url', 'action')
    list_display_links = ('action',)

    def action(self, obj):
        return 'edit'

    def has_add_permission(self, request):
        if AboutUs.objects.exists():
            return False
        return True


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url', 'action')
    list_display_links = ('action',)

    def action(self, obj):
        return 'edit'


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(HomeRight, HomeRightAdmin)
admin.site.register(Welcome, WelcomeAdmin)
admin.site.register(DonationPledge, DonationPledgeAdmin)
admin.site.register(Service, ServicesAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Project, ProjectAdmin)

admin.site.site_title = 'CCV Admin'
admin.site.site_header = 'CCV Admin'
