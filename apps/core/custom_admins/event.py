from django.contrib import admin
from django.db import models

from froala_editor.widgets import FroalaEditor


class CustomEventAdmin(admin.ModelAdmin):
    # The forms to add and change events instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    formfield_overrides = {models.TextField: {"widget": FroalaEditor}}

    # The fields to be used in displaying the Event model.
    list_display = ("title", "starts_at", "ends_at", "created_at", "updated_at")
    list_filter = ("title", "starts_at", "ends_at", "created_at", "updated_at")

    # The filds to be used in updates on Event model.
    fieldsets = (
        (
            "Informações básicas",
            {"classes": ("grp-collapse grp-open",), "fields": ("title", "description","slideshow")},
        ),
        (
            "Periodo de atividade",
            {"classes": ("grp-collapse grp-open",), "fields": ("starts_at", "ends_at")},
        ),
        (
            "Conteúdo",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("image", "icon", "apresentation"),
            },
        ),
        (
            "Monitoramento",
            {
                "classes": ("grp-collapse grp-closed",),
                "fields": ("created_at", "updated_at", "created_by", "updated_by"),
            },
        ),
    )

    # Search and ordering
    search_fields = ("title", "starts_at", "ends_at", "created_at", "updated_at")
    ordering = ("title", "created_at")

    def save_model(self, request, event, form, change):
        if not event.created_by:
            event.created_by = request.user
        else:
            event.updated_by = request.user

        super().save_model(request, event, form, change)
