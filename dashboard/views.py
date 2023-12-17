from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from account.models import User
from product.models import Category, Product, Table


@login_required
@user_passes_test(lambda u: u.is_manager or u.is_employee)
def dashboard_view(request):
    return render(request, "index.html")


@login_required
@user_passes_test(lambda u: u.is_manager or u.is_employee)
def users_view(request):
    managers = User.objects.filter(type="manager")
    employees = User.objects.filter(type="employee")
    normals = User.objects.filter(type="normal")
    return render(
        request,
        "users.html",
        {"managers": managers, "employees": employees, "normals": normals},
    )


@login_required
@user_passes_test(lambda u: u.is_manager)
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
                password=password,
            )
            return redirect("user_management")
        else:
            return render(
                request,
                "users/add_change.html",
                {"error": "رمز عبور و تکرار آن یکسان نیستند"},
            )
    return render(request, "users/add_change.html")


@login_required
@user_passes_test(lambda u: u.is_manager)
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
            return render(
                request,
                "users/add_change.html",
                {"error": "رمز عبور و تکرار آن یکسان نیستند"},
            )

        user.save()
        return redirect("user_management")

    return render(request, "users/add_change.html", {"this": user})


@login_required
@user_passes_test(lambda u: u.is_manager)
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect("user_management")


def products_view(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    category = None
    if category_id:
        category = categories.get(id=category_id)
        products = products.filter(category_id=category_id)

    tables = Table.objects.all()
    return render(
        request,
        "products.html",
        {
            "category": category,
            "categories": categories,
            "products": products,
            "tables": tables,
        },
    )


def add_change_category(request, category_id=None):
    category = None
    if category_id:
        category = Category.objects.get(id=category_id)

    if request.method == "POST":
        name = request.POST["name"]
        icon = None
        if request.FILES:
            icon = request.FILES.get("image")
        if category:
            category.name = name
            category.icon = icon
            category.save()
        else:
            Category.objects.create(name=name, icon=icon)
        return redirect("product_management")
    return render(request, "add_change_category.html", {"category": category})


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect("product_management")


def add_change_table(request, table_id=None):
    table = None
    if table_id:
        table = Table.objects.get(id=table_id)

    if request.method == "POST":
        name = request.POST["name"]
        capacity = request.POST["capacity"]
        if table:
            table.name = name
            table.capacity = capacity
            table.save()
        else:
            Table.objects.create(name=name, capacity=capacity)
        return redirect("product_management")
    return render(request, "add_change_table.html", {"table": table})

def delete_table(request, table_id):
    table = Table.objects.get(id=table_id)
    table.delete()
    return redirect("product_management")


def add_change_product(request, product_id=None):
    product = None
    if product_id:
        product = Product.objects.get(id=product_id)

    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        category = Category.objects.get(id=request.POST["category"])
        image = None
        if request.FILES:
            image = request.FILES.get("image")
        if product:
            product.name = name
            product.price = price
            product.category = category
            if image:
                product.image = image
            product.save()
        else:
            Product.objects.create(
                name=name, price=price, category=category, image=image
            )
        return redirect("product_management")
    categories = Category.objects.all()
    return render(
        request, "add_change_product.html", {"product": product, "categories": categories}
    )
    
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect("product_management")
