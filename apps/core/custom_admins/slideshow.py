from django.contrib import admin
from django.db import models


class CustomSlideshowAdmin(admin.ModelAdmin):
    # The forms to add and change events instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the Slideshow model.
    list_display = ("title", "image", "created_at", "updated_at")
    list_filter = ("title", "image", "created_at", "updated_at")

    # The fields to be used in updates on Slideshow model.
    fieldsets = (
        (
            "Informações básicas",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("title", "resume", "image"),
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
    search_fields = ("title", "image", "created_at", "updated_at")
    ordering = ("title", "image", "created_at")

    def save_model(self, request, slideshow, form, change):
        if not slideshow.created_by:
            slideshow.created_by = request.user
        else:
            slideshow.updated_by = request.user

        super().save_model(request, slideshow, form, change)
