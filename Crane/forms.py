from django import forms
from .models import *
from validate_email import validate_email


class ContactForm(forms.Form):
	name =  forms.CharField()
	email = forms.CharField()
	phone = forms.CharField()
	message =  forms.CharField(widget=forms.Textarea)


	def clean_phone(self):
		cd = self.cleaned_datas
		phone = cd.get('phone')

		if (phone.isdigit() and phone < 10 ):
			"""raise.forms.ValidationError ("Invalid Phone details")"""
			raise(forms.ValidationError ("Invalid Phone details"))

		return phone


	def clean_email(self):
		cd = self.cleaned_data
		email = cd.get('email')

		if (validate_email(email)) :
			raise(forms.ValidationError ("Invalid email"))

		return email


	def clean_message(self):
		cd = self.cleaned_data
		message = cd.get('message')

		if (len( message )) < 160:
			raise(forms.ValidationError ("Message too long"))

		return message




	def clean_username(self):
		cd = self.cleaned_data
		username = cd.get('username')

		if (len( username)) < 20:
			raise(forms.ValidationError ("Error"))

		return message
