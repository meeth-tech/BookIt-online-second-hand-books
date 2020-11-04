from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def home(request):
    print(request.user)
    # context = {'variable1': 'this is sent',
    # 'variable2': 'this is not sent'}
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')  # args= (request, template_file, variable vlue to be passed in


# templates where context is a dictionary


def about(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'about.html')


def buy(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'buy.html')


def contacts(request):
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact.html')


def advertise(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'advertise.html')


def sell(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'sell.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Username and Password do not match. Check credentials and try again')
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/login')
