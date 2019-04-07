from django.contrib import admin
from apps.core.forms.news import NewsCreateForm, NewsUpdateForm


class CustomNewsAdmin(admin.ModelAdmin):
    # The forms to add and change news instances
    add_form = NewsCreateForm
    form = NewsUpdateForm

    readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

    # The fields to be used in displaying the News model.
    list_display = ("title", "publish_date")
    list_filter = ("title", "publish_date")

    # The fields to be used in updates on News model.
    fieldsets = (
        (
            "Informações básicas",
            {"fields": ("title", "resume", "descriptrion", "publish_date")},
        ),
        ("Conteúdo", {"fields": ("image", "icon")}),
        (
            "Monitoramento",
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )

    # Search and ordering
    search_fields = ("title", "publish_date")
    ordering = ("title", "publish_date")

    def save_model(self, request, news, form, change):
        if not news.created_by:
            news.created_by = request.user
        else:
            news.updated_by = request.user

        super().save_model(request, news, form, change)
