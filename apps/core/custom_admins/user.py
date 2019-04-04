from django.contrib.auth.admin import UserAdmin

from apps.core.forms.user import UserCreateForm, UserUpdateForm


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreateForm
    form = UserUpdateForm

    # The fields to be used in displaying the User model.
    list_display = ("email", "first_name", "last_login", "is_active")
    list_filter = ("email", "first_name", "last_login", "is_active")

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
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()

