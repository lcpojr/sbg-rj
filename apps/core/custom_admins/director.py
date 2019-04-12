from django.contrib import admin


class CustomDirectorAdmin(admin.ModelAdmin):
    # The forms to add and change director instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the Director model.
    list_display = (
        "first_name",
        "last_name",
        "email",
        "role",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "first_name",
        "last_name",
        "email",
        "role",
        "created_at",
        "updated_at",
    )

    # The filds to be used in updates on Director model.
    fieldsets = (
        (
            "Informações básicas",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (("first_name", "last_name"), "email", "role"),
            },
        ),
        (
            "Periodo de atividade",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("started_at", "ends_at"),
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
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "role",
        "created_at",
        "updated_at",
    )

    ordering = ("first_name", "created_at")

    def save_model(self, request, director, form, change):
        if not director.created_by:
            director.created_by = request.user
        else:
            director.updated_by = request.user

        super().save_model(request, director, form, change)
