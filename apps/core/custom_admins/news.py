from django.contrib import admin
from django.db import models

from froala_editor.widgets import FroalaEditor


class CustomNewsAdmin(admin.ModelAdmin):
    # The forms to add and change news instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    formfield_overrides = {models.TextField: {"widget": FroalaEditor}}

    # The fields to be used in displaying the News model.
    list_display = ("title", "publish_date")
    list_filter = ("title", "publish_date")

    # The fields to be used in updates on News model.
    fieldsets = (
        (
            "Informações básicas",
            {"fields": ("title", "resume", "description", "publish_date")},
        ),
        ("Conteúdo", {"fields": ("image", "icon")}),
        (
            "Monitoramento",
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )

    # Search and ordering
    search_fields = ("title", "publish_date")
    ordering = ("title", "publish_date")

    def save_model(self, request, news, form, change):
        if not news.created_by:
            news.created_by = request.user
        else:
            news.updated_by = request.user

        super().save_model(request, news, form, change)
