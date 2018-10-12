from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('customer_names', 'customer_email', 'customer_phone', 'message_subject', 'message')
