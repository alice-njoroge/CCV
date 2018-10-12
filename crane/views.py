from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def home(request):
    return render(request, 'crane/index.html')


def about(request):
    return render(request, 'crane/about.html')


def gallery(request):
    return render(request, 'gallery.html')


def typo(request):
    return render(request, 'typo.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'we have received your message.'
                                      ' We will get back to you.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'crane/contact.html', {'form': form})

# def projects(request):
#     return redirect('projects.html')
