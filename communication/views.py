from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import pandas as pd
from users.models import CustomUser


# Create your views here.
def mailme(request, user_to):
    # get the slogan, so we can use it for the subject
    df = pd.DataFrame([u.id, u.slogan, u.email] for u in CustomUser.objects.raw('SELECT id, slogan, email FROM users_customuser where id='+ user_to) )
    
    subject = "Re: " + df.iloc[0,1]
    recipient = df.iloc[0, 2]    
    from_email = 'gollnick.bert@gmail.com' #request.user
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [recipient])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'pages/home.html', {'mailstatus': 'Thank you. Your mail has been sent.'})
    context = {'form': form, 'subject': subject, 'sender': from_email, 'recipient': from_email}
    return render(request, "communication/mailme.html", context)

def successView(request):
    return HttpResponse('Success! Thank you for your message.')