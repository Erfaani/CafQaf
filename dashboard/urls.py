from django.urls import path
from .views import dashboard_view, users_view, add_user, change_user, delete_user

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("users/", users_view, name="user_management"),
    path("users/add/", add_user, name="add_user"),
    path("users/change/<int:user_id>", change_user, name="change_user"),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
]