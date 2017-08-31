from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext


# Create your views here.

#def index(request):
#    return render(request, 'keti/home.html', {})


def index(request):
    return HttpResponse('<h1>keti>keti home</h1>')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        user = authenticate(username = username)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('check your name, try again')
    else:
        form = Loginform()
        return render(request, 'keti/login.html', {'form': form})
