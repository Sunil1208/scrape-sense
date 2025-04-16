from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import CustomUser
from apps.users.forms import CustomUserChangeForm, CustomUsercreationFrom


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    add_form = CustomUsercreationFrom
    form = CustomUserChangeForm
    list_display = (
        "id",
        "user_id",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    list_display_links = ["id", "email", "user_id"]
    list_filter = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    ordering = ("email",)

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Login Credentials", {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "username")}),
        (
            "Permissions and Groups",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    search_fields = ("email", "first_name", "last_name", "username", "user_id")


admin.site.register(CustomUser, CustomUserAdmin)
