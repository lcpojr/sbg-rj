from django.contrib import admin
from apps.core.forms.director import DirectorCreateForm, DirectorUpdateForm


class CustomDirectorAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    add_form = DirectorCreateForm
    form = DirectorUpdateForm

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the User model.
    list_display = ("first_name", "email", "role")
    list_filter = ("first_name", "email", "role")

    # The filds to be used in updates on User model.
    fieldsets = (
        ("Identidade", {"fields": ("first_name", "last_name", "email", "role")}),
        ("Periodo de atividade", {"fields": ("started_at", "ends_at")}),
        (
            "Monitoramento",
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )

    # Search and ordering
    search_fields = ("first_name", "email", "role")
    ordering = ("first_name", "email", "role")

    def save_model(self, request, director, form, change):
        if not director.created_by:
            director.created_by = request.user
        else:
            director.updated_by = request.user

        super().save_model(request, director, form, change)
