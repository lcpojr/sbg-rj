from django.contrib import admin


class CustomPublicationAdmin(admin.ModelAdmin):
    # The forms to add and change publication instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the Publication model.
    list_display = ("name", "category", "document", "created_at", "updated_at")
    list_filter = ("name", "category", "created_at", "updated_at")

    # The fields to be used in updates on Publication model.
    fieldsets = (
        (
            "Informações básicas",
            {"classes": ("grp-collapse grp-open",), "fields": ("name", "category")},
        ),
        ("Conteúdo", {"classes": ("grp-collapse grp-open",), "fields": ("document",)}),
        (
            "Monitoramento",
            {
                "classes": ("grp-collapse grp-closed",),
                "fields": ("created_at", "updated_at", "created_by", "updated_by"),
            },
        ),
    )

    # Search and ordering
    search_fields = ("name", "category", "created_at", "updated_at")
    ordering = ("name", "category")

    def save_model(self, request, publication, form, change):
        if not publication.created_by:
            publication.created_by = request.user
        else:
            publication.updated_by = request.user

        super().save_model(request, publication, form, change)
