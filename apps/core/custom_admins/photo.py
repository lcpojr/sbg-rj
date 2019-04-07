from django.contrib import admin


class CustomPhotoAdmin(admin.ModelAdmin):
    # The forms to add and change photos instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the Photo model.
    list_display = ("image")
    list_filter = ("image")

    # The filds to be used in updates on Photo model.
    fieldsets = (
        ("Conteúdo", {"fields": ("image")}),
        (
            "Monitoramento",
            {"fields": ("created_at", "updated_at",
                        "created_by", "updated_by")},
        ),
    )

    # Search and ordering
    search_fields = ("image")
    ordering = ("image", "created_at")

    def save_model(self, request, photo, form, change):
        if not photo.created_by:
            photo.created_by = request.user
        else:
            photo.updated_by = request.user

        super().save_model(request, photo, form, change)
