from django.contrib import admin


class CustomPublicationAdmin(admin.ModelAdmin):
    # The forms to add and change publication instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the Publication model.
    list_display = ("name", "category")
    list_filter = ("name", "category")

    # The fields to be used in updates on Publication model.
    fieldsets = (
        ("Informações básicas", {"fields": ("name", "category")}),
        ("Conteúdo", {"fields": ("document",)}),
        (
            "Monitoramento",
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )

    # Search and ordering
    search_fields = ("name", "category")
    ordering = ("name", "category")

    def save_model(self, request, publication, form, change):
        if not publication.created_by:
            publication.created_by = request.user
        else:
            publication.updated_by = request.user

        super().save_model(request, publication, form, change)
