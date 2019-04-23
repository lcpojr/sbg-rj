import uuid

from django.contrib.sitemaps import ping_google
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.db import models

from tinymce.models import HTMLField

from .user import User


class Event(models.Model):
    """
    This model contains the events data.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Identity
    title = models.CharField(max_length=100, verbose_name="Título")
    resume = models.CharField(max_length=250, verbose_name="Resumo")
    description = HTMLField(verbose_name="Descrição")

    slug = models.SlugField(
        max_length=500,
        unique=True,
        verbose_name="Slogan da página",
        help_text="Utilizado para que o link da página torne-se fácil de ler por um humano",
    )

    slideshow = models.BooleanField(
        default=False,
        verbose_name="Slideshow",
        help_text="Selecione essa opção se deseja que o evento apareça na HomePage.",
    )

    # Content
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to="events/%Y-%m-%d/",
        validators=[
            FileExtensionValidator(
                ["png", "jpg", "jpeg"], "Formato de imagem inválido (.png, .jpg, jpeg)"
            )
        ],
    )

    icon = models.ImageField(
        verbose_name="Ícone",
        upload_to="events/%Y-%m-%d/",
        validators=[
            FileExtensionValidator(
                ["png", "jpg", "jpeg"], "Formato de ícone inválido (.png, .jpg, jpeg)"
            )
        ],
    )

    apresentation = models.FileField(
        verbose_name="Apresentação",
        upload_to="events/%Y-%m-%d/",
        validators=[
            FileExtensionValidator(
                ["pdf", "ppt", "pptx"],
                "Formato de apresentação inválido (.pdf, .ppt, .pptx)",
            )
        ],
    )

    # Activity period
    starts_at = models.DateTimeField(verbose_name="Data de início")
    ends_at = models.DateTimeField(verbose_name="Data de término")

    # Monitoring
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima atualização")

    # Associations
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela criação do registro (evento).",
        related_name="event_creator_set",
        verbose_name="Criador",
        on_delete=models.SET_NULL,
    )

    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela ultima atualização do registro (evento).",
        related_name="event_updater_set",
        verbose_name="Atualizador",
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

        try:
            ping_google()
        except Exception:
            pass
