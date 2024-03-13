from django.shortcuts import render, redirect

from product.models import Category, Product

def home_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    current_category = None
    if category := request.GET.get('category'):
        products = Product.objects.filter(category=category)
        current_category = Category.objects.get(id=category)

    return render(
        request,
        "home.html",
        {"categories": categories, "products": products, "category": current_category},
    )
