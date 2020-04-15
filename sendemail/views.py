from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            recipient = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'info@dogooddeed.com', [recipient])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'pages/home.html', {'mailstatus': 'Thank you. Your mail has been sent.'})
    return render(request, "contact.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
