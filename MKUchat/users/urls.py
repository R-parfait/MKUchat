from django.urls import path

from . import views

app_name="users"
urlpatterns=[
    path("", views.registrationpage, name="index"),
     path("login", views.login_views, name="loginpage"),
     path("logout", views.logout_views, name="logoutpage"),

]