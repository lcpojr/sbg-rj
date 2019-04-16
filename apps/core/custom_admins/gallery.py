from django.contrib import admin
from django.db import models

from froala_editor.widgets import FroalaEditor


class CustomGalleryAdmin(admin.ModelAdmin):
    # The forms to add and change gallery instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    formfield_overrides = {models.TextField: {"widget": FroalaEditor}}

    # The fields to be used in displaying the Gallery model.
    list_display = ("title", "category", "image", "created_at", "updated_at")
    list_filter = ("title", "category", "image", "created_at", "updated_at")

    # The filds to be used in updates on Gallery model.
    fieldsets = (
        (
            "Informações básicas",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("title", "description", "category", "image"),
            },
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
    search_fields = ("title", "category", "image", "created_at", "updated_at")
    ordering = ("title", "created_at")

    def save_model(self, request, gallery, form, change):
        if not gallery.created_by:
            gallery.created_by = request.user
        else:
            gallery.updated_by = request.user

        super().save_model(request, gallery, form, change)
