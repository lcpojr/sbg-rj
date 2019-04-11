import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from .user import User


class News(models.Model):
    """
    This model contains the news data.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Identity
    title = models.CharField(max_length=50, verbose_name="Título da Notícia")
    resume = models.TextField(verbose_name="Resumo da Notícia")
    description = models.TextField(verbose_name="Descrição")
    publish_date = models.DateTimeField(verbose_name="Data da Notícia")

    # Content
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to="news/%Y-%m-%d",
        validators=[
            FileExtensionValidator(
                ["png", "jpg", "jpeg"], "Formato de imagem inválido (.png, .jpg, .jpeg)"
            )
        ],
    )

    icon = models.ImageField(
        verbose_name="Ícone",
        upload_to="news/%Y-%m-%d",
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
        help_text="Usuário responsável pela criação do registro (notícia).",
        related_name="news_creator_set",
        verbose_name="Criador",
        on_delete=models.SET_NULL,
    )

    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela ultima atualização do registro (notícia).",
        related_name="news_updater_set",
        verbose_name="Atualizador",
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    def __str__(self):
        return "{} ()".format(self.title, self.resume)
