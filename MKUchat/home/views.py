from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def welcomepage(request):
    return HttpResponse("Welcome to MKUchat!")

def loginpage(request):
    return HttpResponse("Login Form")

def logoutpage(request):
    return HttpResponse("You have succesfully logged out")