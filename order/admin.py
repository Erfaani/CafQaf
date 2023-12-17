from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'table', 'is_active', 'created_at')


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'product','total_price', 'quantity')
    readonly_fields = ('total_price',)