import email
from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from home import *
from django.contrib.auth.models import User, auth

# Create your views here.

def registrationpage(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                return render(request, "home/login.html", {
                    "message":"Username Already Used"
                })

            elif User.objects.filter(email=email).exists():
                return render(request, "home/login.html", {
                    "message":"Email has already been used"
                })
        
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                return render(request, "home/login.html", {
                    "message":"Acoount Created Succesfully! You can now log in"
                })

        else:
            return render(request, "home/login.html", {
            "message":"Password not matching"
            })

    else:
        return render(request, "home/login.html", {
            "message":"Failed. Kindly try again!"
        })

def login_views(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "home/home.html")
        else:
            return render(request, "home/login.html", {
                "message": "Invalid Credentials"
            })

    return render(request, "home/login.html")

def logout_views(request):
    logout(request)
    return render(request, "home/login.html", {
        "message": "Logged Out."
    })
