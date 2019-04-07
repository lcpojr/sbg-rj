from django.contrib import admin
from django.db import models

from froala_editor.widgets import FroalaEditor


class CustomEventAdmin(admin.ModelAdmin):
    # The forms to add and change events instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    formfield_overrides = {models.TextField: {"widget": FroalaEditor}}

    # The fields to be used in displaying the Event model.
    list_display = ("title", "description")
    list_filter = ("title", "description")

    # The filds to be used in updates on Event model.
    fieldsets = (
        ("Identidade", {"fields": ("title", "description")}),
        ("Periodo de atividade", {"fields": ("starts_at", "ends_at")}),
        ("Conteúdo", {"fields": ("image", "icon", "apresentation")}),
        (
            "Monitoramento",
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )

    # Search and ordering
    search_fields = ("title", "description")
    ordering = ("title", "created_at")

    def save_model(self, request, event, form, change):
        if not event.created_by:
            event.created_by = request.user
        else:
            event.updated_by = request.user

        super().save_model(request, event, form, change)
