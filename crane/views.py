from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from .models import Carousel, HomeRight


def home(request):
    carousel = Carousel.objects.all()
    home_right_images = HomeRight.objects.all()
    return render(request, 'crane/index.html', {
        'carousel': carousel,
        'home_right_images': home_right_images
    })


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
            message = form.save()
            send_mail(
                subject=message.subject,
                recipient_list=['alice.njoroge@ccvkenya.org'],
                message=f'You have received a message from {message.name}, {message.email} saying {message.message}',
                from_email='website@ccv.org'
            )
            messages.success(request, 'we have received your message.'
                                      ' We will get back to you.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'crane/contact.html', {'form': form})

# def projects(request):
#     return redirect('projects.html')
