from django.urls import path
from .views import (
    dashboard_view,
    users_view,
    add_user,
    change_user,
    delete_user,
    products_view,
    add_change_category,
    delete_category,
    add_change_table,
    delete_table,
    add_change_product,
    delete_product,
    orders_view, done_order,
    select_item,
)

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("users/", users_view, name="user_management"),
    path("users/add/", add_user, name="add_user"),
    path("users/change/<int:user_id>", change_user, name="change_user"),
    path("delete_user/<int:user_id>/", delete_user, name="delete_user"),
    path("products/", products_view, name="product_management"),
    path("products/<int:category_id>", products_view, name="product_management"),
    path("products/add_change_category/", add_change_category, name="add_category"),
    path(
        "products/add_change_category/<int:category_id>",
        add_change_category,
        name="change_category",
    ),
    path(
        "products/delete_category/<int:category_id>",
        delete_category,
        name="delete_category",
    ),
    path("products/add_change_table/", add_change_table, name="add_table"),
    path(
        "products/add_change_table/<int:table_id>",
        add_change_table,
        name="change_table",
    ),
    path("products/delete_table/<int:table_id>", delete_table, name="delete_table"),
    path("products/add_change_product/", add_change_product, name="add_product"),
    path(
        "products/add_change_product/<int:product_id>",
        add_change_product,
        name="change_product",
    ),
    path(
        "products/delete_product/<int:product_id>",
        delete_product,
        name="delete_product",
    ),
    path("orders/", orders_view, name="order_management"),
    path('orders/done/<int:order_id>/', done_order, name='done_order'),
    path("select_item/", select_item, name="select_item"),
]
