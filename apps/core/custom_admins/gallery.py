from django.contrib import admin
from apps.core.forms.gallery import GalleryCreateForm, GalleryUpdateForm


class CustomGalleryAdmin(admin.ModelAdmin):
    # The forms to add and change gallery instances
    add_form = GalleryCreateForm
    form = GalleryUpdateForm

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the Gallery model.
    list_display = ("title", "description", "category")
    list_filter = ("title", "description", "category")

    # The filds to be used in updates on Gallery model.
    fieldsets = (
        ("Conteúdo", {"fields": ("photos",)}),
        (
            "Monitoramento",
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )

    # Search and ordering
    search_fields = ("title", "description", "category")
    ordering = ("title", "created_at")

    def save_model(self, request, gallery, form, change):
        if not gallery.created_by:
            gallery.created_by = request.user
        else:
            gallery.updated_by = request.user

        super().save_model(request, gallery, form, change)
