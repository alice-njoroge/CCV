from django.shortcuts import render
from .forms import ContactForm


def home (request):
	return render (request, 'index.html')


def  about (request):
	return render (request, 'about.html')

def   gallery (request):
	return render (request, 'gallery.html')


def  typo (request):
	return render (request, 'typo.html')


def   contact (request):

	if request.method  == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():

			newMessage = Message (

			username = form.cleaned_data['username'],
			email = form.cleaned_data['email'],
			message = form.cleaned_data['message'],)
			newMessage.save()
			



			return render (request, 'index')
	else:
		form = ContactForm
	return render (request, 'contact.html')

def   projects (request):
	return redirect ( 'projects.html')



