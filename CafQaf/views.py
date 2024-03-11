from django.shortcuts import render, redirect

from product.models import Category, Product

def home_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'home.html', {'categories': categories, 'products': products})