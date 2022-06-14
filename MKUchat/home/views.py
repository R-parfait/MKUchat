from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def welcomepage(request):
    return render(request, "home/Welcomepage.html")

def loginpage(request):
    return HttpResponse("Login Form")

def createaccount(request):
    return HttpResponse("we shoud have the form to create an account here")

def logoutpage(request):
    return HttpResponse("You have succesfully logged out")