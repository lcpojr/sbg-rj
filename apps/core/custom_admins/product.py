from django.contrib import admin


class CustomProductAdmin(admin.ModelAdmin):
    # The forms to add and change products instances
    empty_value_display = "----"

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the Product model.
    list_display = ("name", "price_associated", "price_non_associated")
    list_filter = ("name", "price_associated", "price_non_associated")

    # The filds to be used in updates on Product model.
    fieldsets = (
        ("Identidade", {"fields": ("name", "description")}),
        ("Preços", {"fields": ("price_associated", "price_non_associated")}),
        ("Propaganda", {"fields": ("image", "icon")}),
        (
            "Monitoramento",
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )

    # Search and ordering
    search_fields = ("name", "price_associated", "price_non_associated")
    ordering = ("name", "created_at")

    def save_model(self, request, product, form, change):
        if not product.created_by:
            product.created_by = request.user
        else:
            product.updated_by = request.user

        super().save_model(request, product, form, change)
