import uuid

from django.contrib.sitemaps import ping_google
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.db import models

from .user import User


class Gallery(models.Model):
    """
    This model contains the gallery data.
    """

    CATEGORY_CHOICES = []

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Identity
    title = models.CharField(max_length=100, unique=True, verbose_name="Title")
    description = models.TextField(verbose_name="Descrição")
    category = models.CharField(
        max_length=50, verbose_name="Categoria", blank=True, choices=CATEGORY_CHOICES
    )

    slug = models.SlugField(
        max_length=500,
        unique=True,
        verbose_name="Slogan da página",
        help_text="Utilizado para que o link da página torne-se fácil de ler por um humano",
    )

    # Content
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to="gallery/%Y-%m-%d",
        validators=[
            FileExtensionValidator(
                ["png", "jpg", "jpeg"], "Formato de imagem inválido (.png, .jpg, .jpeg)"
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
        help_text="Usuário responsável pela criação do registro (produto).",
        related_name="gallery_creator_set",
        verbose_name="Criador",
        on_delete=models.SET_NULL,
    )

    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela ultima atualização do registro (produto).",
        related_name="gallery_updater_set",
        verbose_name="Atualizador",
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"

    def __str__(self):
        return "{} ({})".format(self.title, self.category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)

        try:
            ping_google()
        except Exception:
            pass

