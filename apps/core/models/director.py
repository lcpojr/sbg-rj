import uuid

from django.db import models
from .user import User


class Director(models.Model):
    """
    This model contains the director data.
    The director should only stay active for maximum 2 years.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Identity
    first_name = models.CharField(max_length=50, verbose_name="Nome")
    last_name = models.CharField(max_length=50, null=True, verbose_name="Sobrenome")
    role = models.CharField(max_length=50, verbose_name="Cargo")
    email = models.EmailField(unique=True, verbose_name="Email")

    # Activity period (biennium)
    started_at = models.DateTimeField(verbose_name="Data de início")
    ends_at = models.DateTimeField(verbose_name="Data de término")

    # Monitoring
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima atualização")

    # Associations
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela criação do registro (diretor).",
        related_name="director_creator_set",
        verbose_name="Criador",
        on_delete=models.SET_NULL,
    )

    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela ultima atualização do registro (diretor).",
        related_name="director_updater_set",
        verbose_name="Atualizador",
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Diretor"
        verbose_name_plural = "Diretores"

    def __str__(self):
        return "{} ()".format(self.first_name, self.email)

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
