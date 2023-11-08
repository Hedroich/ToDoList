from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "name",
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "name",
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("name", "email", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
