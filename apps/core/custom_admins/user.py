from django.contrib.auth.admin import UserAdmin

from apps.core.forms.user import UserCreateForm, UserUpdateForm


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreateForm
    form = UserUpdateForm
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at"]

    # The fields to be used in displaying the User model.
    list_display = (
        "first_name",
        "last_name",
        "email",
        "last_login",
        "is_active",
        "is_superuser",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "first_name",
        "last_name",
        "email",
        "last_login",
        "is_active",
        "is_superuser",
        "created_at",
        "updated_at",
    )

    # The fields to be used in updates on User model.
    fieldsets = (
        (
            "Informações básicas",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (("first_name", "last_name"), "email", "password"),
            },
        ),
        (
            "Permissões",
            {"classes": ("grp-collapse grp-open",), "fields": ("is_superuser",)},
        ),
        ("Status", {"classes": ("grp-collapse grp-open",), "fields": ("is_active",)}),
    )

    # The fields to be used in inserts on User model.
    add_fieldsets = (
        (
            "Login",
            {
                "classes": ("grp-collapse grp-open", "wide"),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    # Search and ordering
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "last_login",
        "is_active",
        "is_superuser",
        "created_at",
        "updated_at",
    )

    ordering = ("first_name", "created_at")
    filter_horizontal = ()

