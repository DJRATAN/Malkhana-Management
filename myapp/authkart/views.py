from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass1"]
        confirm_password = request.POST["pass2"]
        if password != confirm_password:
            messages.warning(request, "Password is not Matching")
            return render(request, "manage/signup.html")
        try:
            if User.objects.get(username=email):
                messages.info(request, "Email Already is Taken")
                return render(request, "manage/signup.html")
        except Exception as identifier:
            pass
        user = User.objects.create_user(email, email, password)
        user.save()
        messages.success(request,"Your Account activated You can Login ")
        return redirect('/manage/signup/')
    return render(request, "manage/signup.html")

def handlelogin(request):
    if request.method=="POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/authkart/login')
    return render(request, "manage/login.html")


def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect("manage/index")


