from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem

from .forms import AddToCartForm

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user

    # Check if the user has an existing cart or create one
    order, created = Order.objects.get_or_create(user=user, total_price=0)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            # Check if the product is already in the cart
            order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product, item_price=product.price)

            if not item_created:
                order_item.quantity += quantity
                order_item.save()

            order.total_price += product.price * quantity
            order.save()

            return redirect('cart')

    else:
        form = AddToCartForm()

    return render(request, 'add_to_cart.html', {'form': form, 'product': product})

def view_cart(request):
    user = request.user
    order = Order.objects.filter(user=user).last()

    return render(request, 'cart.html', {'order': order}



