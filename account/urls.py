from django.urls import path
from .views import logout_view, login_view, signup_view

urlpatterns = [
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
]
