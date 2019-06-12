import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from .user import User


class Slideshow(models.Model):
    """
    This model contains the slideshow data.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Content
    title = models.CharField(max_length=100, verbose_name="Título", unique=True)
    resume = models.CharField(max_length=500, verbose_name="Resumo")
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to="slideshow/%Y-%m-%d/",
        validators=[
            FileExtensionValidator(
                ["png", "jpg", "jpeg"], "Formato de imagem inválido (.png, .jpg, jpeg)"
            )
        ],
    )

    # Monitoring
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima atualização")

    # Associations
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela criação do registro (slide).",
        related_name="slide_creator_set",
        verbose_name="Criador",
        on_delete=models.SET_NULL,
    )

    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela ultima atualização do registro (slide).",
        related_name="slide_updater_set",
        verbose_name="Atualizador",
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Slideshow"
        verbose_name_plural = "Slideshow"

    def __str__(self):
        return self.title
