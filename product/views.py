from django.shortcuts import render
from .models import Product, Category


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products, "categories": categories})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    print(product)
    return render(request, "product_detail.html", {"product": product})
