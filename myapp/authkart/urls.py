from django.contrib import admin
from django.urls import path
from .views import* 

urlpatterns = [
    path("signup/",signup),
    path("login/",handlelogin),
    path("logout/",handlelogout),
]
