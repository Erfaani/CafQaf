from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Login successful.")
            return redirect("home") 
        else:
            return render(request, "login.html", {"error": "نام کاربری یا رمز عبور اشتباه است"})
    return render(request, "login.html") 

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password1"]
        password2 = request.POST["password2"]
        if password == password2:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            login(request, user)
            return redirect("home")
        else:
            return render(request, "signup.html", {"error": "رمز عبور و تکرار آن یکسان نیستند"})
    return render(request, "signup.html")

