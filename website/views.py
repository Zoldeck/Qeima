from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    if request.method == "POST":
        fname = request.POST.get('fname', '');
        lname = request.POST.get('lname', '');
        email = request.POST.get('email', '');
        subject = request.POST.get('subject', '');
        message = request.POST.get('message', '');

        send_mail(
            'Website message - ' + fname + " " + lname + ' - Phone Number: ' + subject + " - " + email,
            message,
            email,
            ['hamada_1418@hotmail.com'],
            fail_silently=False,

        )

        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})
