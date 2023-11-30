from django.contrib import admin

from .models import TableType, Table, Order, OrderItem

admin.site.register(TableType)
admin.site.register(Table)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'table', 'canceled', 'created_at')


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'product','total_price', 'quantity')
    readonly_fields = ('total_price',)