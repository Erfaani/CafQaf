from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "type")
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "type",
                ),
            },
        ),
    )
    


admin.site.register(User, CustomUserAdmin)
