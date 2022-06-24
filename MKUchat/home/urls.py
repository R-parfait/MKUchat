from django.urls import path
from . import views

app_name = "home"
urlpatterns=[
    path("", views.homepage, name="home"),
    path("welcome", views.welcomepage, name="welcomepage"),
    path("createaccount", views.createaccount, name="createaccount"),
]