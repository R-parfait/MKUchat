from django.urls import path
from . import views

urlpatterns=[
    path("", views.homepage, name="home"),
    path("welcome", views.welcomepage, name="welcomepage"),
    path("login", views.loginpage, name="loginpage"),
    path("createaccount", views.createaccount, name="createaccount"),
    path("logout", views.logoutpage, name="logoutpage"),
]