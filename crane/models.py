from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ContactMessage(models.Model):
    customer_names = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=100, blank=True, null=True)
    message_subject = models.TextField()
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def read_message(self):
        return "<a href='/contact-message/%s/read'>Read Message</a>" % self.id

    read_message.allow_tags = True

    def __str__(self):
        return self.message_subject


# Create your models here.
