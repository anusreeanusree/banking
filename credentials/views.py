from django.contrib import auth, messages
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
# Create your views here.


def register(request):
    if request.POST:
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cfpassword = request.POST.get('cfpassword')

        user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
        return render(request,'login.html',{'user': user})
    return  render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'submit.html')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
