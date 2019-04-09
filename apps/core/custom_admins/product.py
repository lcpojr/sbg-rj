from django.contrib import admin
from django.db import models

from froala_editor.widgets import FroalaEditor


class CustomProductAdmin(admin.ModelAdmin):
    # The forms to add and change products instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    formfield_overrides = {models.TextField: {"widget": FroalaEditor}}

    # The fields to be used in displaying the Product model.
    list_display = (
        "name",
        "price_associated",
        "price_non_associated",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
        "price_associated",
        "price_non_associated",
        "created_at",
        "updated_at",
    )

    # The filds to be used in updates on Product model.
    fieldsets = (
        (
            "Identidade",
            {"classes": ("grp-collapse grp-open",), "fields": ("name", "description")},
        ),
        (
            "Preços",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("price_associated", "price_non_associated"),
            },
        ),
        (
            "Propaganda",
            {"classes": ("grp-collapse grp-open",), "fields": ("image", "icon")},
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
    search_fields = (
        "name",
        "price_associated",
        "price_non_associated",
        "created_at",
        "updated_at",
    )

    ordering = ("name", "created_at")

    def save_model(self, request, product, form, change):
        if not product.created_by:
            product.created_by = request.user
        else:
            product.updated_by = request.user

        super().save_model(request, product, form, change)
