import datetime
from zoneinfo import ZoneInfo

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

from account.models import User
from product.models import Category, Product, Table
from order.models import Order, OrderItem

from utils import jalali


@login_required
@user_passes_test(lambda u: u.is_manager or u.is_employee)
def dashboard_view(request):
    return render(request, "dashboard/index/index.html")


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
        description = request.POST["description"]
        category = Category.objects.get(id=request.POST["category"])
        image = None
        if request.FILES:
            image = request.FILES.get("image")
        if product:
            product.name = name
            product.price = price
            product.category = category
            product.description = description
            if image:
                product.image = image
            product.save()
        else:
            Product.objects.create(
                name=name, price=price, category=category, description=description, image=image
            )
        return redirect("product_management")
    categories = Category.objects.all()
    return render(
        request,
        "add_change_product.html",
        {"product": product, "categories": categories},
    )


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect("product_management")


def orders_view(request):
    current_orders = Order.objects.filter(is_active=True)
    past_orders = Order.objects.filter(is_active=False)
    return render(
        request,
        "dashboard/orders/orders.html",
        {"current_orders": current_orders, "past_orders": past_orders},
    )


def done_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_active = False
    order.save()
    return redirect("order_management")

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect("order_management")


@login_required(login_url="login")
def select_item(request, order_id=None):

    if request.method == "POST":
        table_id = request.POST["table"]
        date, time = request.POST["date"].split(" ")
        table = Table.objects.get(id=table_id)
        order = Order.objects.get(id=order_id)
        order.table = table
        # https://github.com/mjnaderi/Jalali.py
        order.reserved_for = (
            datetime.datetime.strptime(
                jalali.Persian(date).gregorian_string(), "%Y-%m-%d"
            )
            + datetime.timedelta(
                hours=int(time.split(":")[0]), minutes=int(time.split(":")[1])
            )
        ).replace(tzinfo=ZoneInfo("Asia/Tehran"))
        order.save()
        return redirect("order_management")

    order = None
    if order_id:
        order = Order.objects.get(id=order_id)
    else:
        order = Order.objects.create(user=request.user)
        return redirect("select_item", order_id=order.id)
    order_items = OrderItem.objects.filter(order=order)

    categories = Category.objects.all()
    products = Product.objects.all()
    if category_id := request.GET.get("category"):
        products = products.filter(category_id=category_id)
    tables = Table.objects.all()

    context = {
        "categories": categories,
        "products": products,
        "tables": tables,
        "order": order,
        "order_items": order_items
    }
    return render(request, "dashboard/orders/select.html", context)


def add_item(request, product_id, order_id=None):
    product = Product.objects.get(id=product_id)
    
    order = None
    if order_id:
        order = Order.objects.get(id=order_id)
    else:
        order = Order.objects.create(user=request.user)
        order_id = order.id

    order_items = OrderItem.objects.filter(order=order)
    if order_items.filter(product=product).exists():
        order_item = order_items.get(product=product)
        order_item.quantity += 1
        order_item.save()
    else:
        OrderItem.objects.create(order=order, product=product, quantity=1)

    return redirect("select_item", order_id=order_id)


def remove_item(request, order_id, item_id):
    item = OrderItem.objects.get(id=item_id)
    item.delete()
    return redirect("select_item", order_id=order_id)


@require_GET
def change_item_quantity(request, order_id, item_id):
    item = OrderItem.objects.get(id=item_id)
    item.quantity = request.GET.get("quantity", 1)
    item.save()
    return redirect("select_item", order_id=order_id)


def checkout(request, order_id):
    return redirect("order_management")
