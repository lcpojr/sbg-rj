from django.contrib.auth.admin import UserAdmin

from apps.core.forms.user import UserCreateForm, UserUpdateForm


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreateForm
    form = UserUpdateForm

    readonly_fields = ["created_at", "updated_at"]

    # The fields to be used in displaying the User model.
    list_display = ("first_name", "email", "last_login", "is_active")
    list_filter = ("first_name", "email", "last_login", "is_active")

    # The filds to be used in updates on User model.
    fieldsets = (
        ("Identidade", {"fields": ("first_name", "last_name", "email", "password")}),
        ("Permissões", {"fields": ("is_superuser",)}),
        ("Status", {"fields": ("is_active",)}),
    )

    # The fields to be used in inserts on User model.
    add_fieldsets = (
        (
            "Login",
            {"classes": ("wide",), "fields": ("email", "password1", "password2")},
        ),
    )
    # Search and ordering
    search_fields = ("first_name", "email")
    ordering = ("first_name", "created_at")
    filter_horizontal = ()

