import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from .user import User


class Product(models.Model):
    """
    This model contains the products data.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Identity
    name = models.CharField(max_length=50, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")

    # Content
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to="products/%Y-%m-%d/",
        validators=[
            FileExtensionValidator(
                ["png", "jpg", "jpeg"], "Formato de imagem inválido (.png, .jpg, jpeg)"
            )
        ],
    )

    icon = models.ImageField(
        verbose_name="Ícone",
        upload_to="products/%Y-%m-%d/",
        validators=[
            FileExtensionValidator(
                ["png", "jpg", "jpeg"], "Formato de ícone inválido (.png, .jpg, jpeg)"
            )
        ],
    )

    # Princing
    price_associated = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Preço de associado"
    )

    price_non_associated = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Preço de não associado"
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
        related_name="product_creator_set",
        verbose_name="Criador",
        on_delete=models.SET_NULL,
    )

    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        help_text="Usuário responsável pela ultima atualização do registro (produto).",
        related_name="product_updater_set",
        verbose_name="Atualizador",
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return "{} - R$ {}".format(self.name, self.price_non_associated)
