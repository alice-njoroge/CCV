from django import forms
from .models import ContactMessage, DonationPledge


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone_number', 'subject', 'message')


class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationPledge
        fields = ('name', 'email', 'phone', 'amount', 'when')
