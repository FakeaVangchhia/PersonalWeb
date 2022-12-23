from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Send email
        send_mail(
            name, # subject
            message, # message
            email, # sender email
            ['fakeavangchhia@gmail.com'], # receiver email
            fail_silently=False,
        )

        return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})




