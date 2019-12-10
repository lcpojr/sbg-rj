import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from .user import User
from .gallery import Gallery


class Photo(models.Model):
    """
    This model contains the photos data.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Content
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to="photos/%Y-%m-%d/",
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
    gallery = models.ForeignKey(
        Gallery,
        help_text="Galeria que contem o registro (foto)",
        related_name="gallery_photos",
        verbose_name="Galeria",
        on_delete=models.CASCADE,
    )

    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela criação do registro (produto).",
        related_name="photo_creator_set",
        verbose_name="Criador",
        on_delete=models.SET_NULL,
    )

    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela ultima atualização do registro (produto).",
        related_name="photo_updater_set",
        verbose_name="Atualizador",
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

    def __str__(self):
        return "{}".format(self.image)

