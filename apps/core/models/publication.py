import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from .user import User


class Publication(models.Model):
    """
    This model contains the publications data.
    """

    PUBLICATION_CHOICES = []

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Identity
    name = models.CharField(max_length=100, verbose_name="Nome")
    category = models.CharField(
        max_length=50, null=True, verbose_name="Categoria", choices=PUBLICATION_CHOICES
    )

    # Content
    document = models.FileField(
        verbose_name="Documento",
        upload_to="publications/%Y-%m-%d/",
        validators=[
            FileExtensionValidator(["pdf"], "Formato de publicação inválido (.pdf)")
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
        help_text="Usuário responsável pela criação do registro (publicação).",
        related_name="publication_creator_set",
        verbose_name="Criador",
        on_delete=models.SET_NULL,
    )

    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela ultima atualização do registro (publicação).",
        related_name="publication_updater_set",
        verbose_name="Atualizador",
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"

    def __str__(self):
        return "{} {}".format(self.name, self.category)
