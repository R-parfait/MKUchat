from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def welcomepage(request):
    return render(request, "home/Welcomepage.html")

def loginpage(request):
    return render(request, "home/login.html")

def createaccount(request):
    return HttpResponse("we shoud have the form to create an account here")

def logoutpage(request):
    return HttpResponse("You have succesfully logged out")

def homepage(request):
    return render(request,"home/home.html")