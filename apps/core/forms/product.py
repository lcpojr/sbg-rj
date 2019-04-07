from django import forms

from apps.core.models.product import Product


class ProductCreateForm(forms.ModelForm):
    """
    A form for creating new products. Includes all the required
    fields.
    """

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "image",
            "icon",
            "price_associated",
            "price_non_associated",
        )


class ProductUpdateForm(forms.ModelForm):
    """
    A form for updating products. Includes all the fields on
    the product, but replaces the users fields to be only readable.
    """

    class Meta:
        model = Product
        fields = "__all__"

