from django.contrib import admin
from django.db import models


class CustomNewsAdmin(admin.ModelAdmin):
    # The forms to add and change news instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the News model.
    list_display = ("title", "publish_date", "created_at", "updated_at")
    list_filter = ("title", "publish_date", "created_at", "updated_at")

    # The fields to be used in updates on News model.
    fieldsets = (
        (
            "Informações básicas",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("title", "resume", "description", "publish_date"),
            },
        ),
        (
            "Conteúdo",
            {"classes": ("grp-collapse grp-open",), "fields": ("image", "icon")},
        ),
        (
            "Monitoramento",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("created_at", "updated_at", "created_by", "updated_by"),
            },
        ),
    )

    # Search and ordering
    search_fields = ("title", "publish_date", "created_at", "updated_at")
    ordering = ("title", "publish_date")

    def save_model(self, request, news, form, change):
        if not news.created_by:
            news.created_by = request.user
        else:
            news.updated_by = request.user

        super().save_model(request, news, form, change)
