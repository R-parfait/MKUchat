from django.urls import path
from . import views

urlpatterns=[
    path("", views.welcomepage, name="welcomepage"),
    path("login", views.loginpage, name="loginpage"),
    path("logout", views.logoutpage, name="logoutpage"),
]