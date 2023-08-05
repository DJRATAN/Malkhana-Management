from django.http import HttpResponse
from django.shortcuts import render 
def Home(request):
    return render(request,"manage/home.html")

def about(request):
   return render(request,"about.html")

def services(request):
    return render(request,"services.html",{})