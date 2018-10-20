from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from django.core.files.images import get_image_dimensions


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def read_message(self):
        return "<a href='/contact-message/%s/read'>Read Message</a>" % self.id

    read_message.allow_tags = True

    def __str__(self):
        return self.subject


class Carousel(models.Model):
    """
    Store carousel image for the front page and stores 5 images with a position
    """
    POSITIONS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    image = models.ImageField(upload_to='carousels/',
                              help_text='This is one of the images on the carousel slider',
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    position = models.PositiveSmallIntegerField(choices=POSITIONS, unique=True)

    def image_url(self):
        """allow image to be displayed in the admin as a thumbnail"""
        url = self.image.url
        return format_html(
            '<a href="{}"><img style="height:70px;width:70px;" alt="25" src="{}"/></a>',
            url,
            url
        )

    image_url.allow_tags = True

    def __str__(self):
        return str(self.image.url)

    class Meta:
        ordering = ('position',)

    def clean(self):
        w, h = get_image_dimensions(self.image)
        if w < 676 or h < 507:
            raise ValidationError({'image': 'The image needs to be 676 * 507 pixels'})
