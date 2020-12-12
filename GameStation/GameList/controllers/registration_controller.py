from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings

def index(request):
    msg = ''
    if request.method == 'POST':
        req = request.POST.dict()
        username = req['username']
        password = req['password']
        email = req['email']  
        try: 
            user = User.objects.get(username=username)
            error_message = 'Username is already registered, please input another username'
        except User.DoesNotExist: 
            user = User.objects.create_user(username, email, password) 
            user.save()
            send_mail(
                'Registration Successful',
                'Welcome Gamers to GameStation!',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )
            return HttpResponseRedirect('account/login')
    data = {
        'error_message': error_message,
    }
    return render(request, 'registration.html', data)

