from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings

from .models import Info

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        
        send_mail(
            subject,
            message,
            # from 
            settings.EMAIL_HOST_USER,
            # to
            [email],
            
            fail_silently=False,
        )
        print('Email sent: ', email)
        return redirect('email-sent')

    return render(request, 'contact.html')


def email_sent(request):
    return render(request, 'email_sent.html', {})