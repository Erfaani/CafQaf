from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account.models import User


@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")

@login_required
def users_view(request):
    managers = User.objects.filter(type='manager')
    employees = User.objects.filter(type='employee')
    normals = User.objects.filter(type='normal')
    return render(
        request,
         "users.html",
          {"managers": managers,
           "employees": employees,
           "normals": normals
           })

@login_required
def add_user(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        type = request.POST["type"]
        username = request.POST["username"]
        password = request.POST["password1"]
        password2 = request.POST["password2"]
        if password == password2:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                type=type,
                username=username,
                password=password
            )
            return redirect("user_management")
        else:
            return render(request, 'users/add.html', {"error": "رمز عبور و تکرار آن یکسان نیستند"})
    return render(request, 'users/add.html')

@login_required
def change_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.type = request.POST["type"]
        user.username = request.POST["username"]
        password = request.POST["password1"]
        password2 = request.POST["password2"]
        if password == password2:
            if password != "":
                user.set_password(password)  
        else:
            return render(request, 'users/change.html', {"error": "رمز عبور و تکرار آن یکسان نیستند"})

        user.save()
        return redirect("user_management")
    
    return render(request, 'users/change.html', {"user": user})

@login_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('user_management')
