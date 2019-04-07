from django import forms

from apps.core.models.gallery import Gallery


class GalleryCreateForm(forms.ModelForm):
    """
    A form for creating new photos. Includes all the required
    fields.
    """

    class Meta:
        model = Gallery
        fields = ("title", "description", "category", "photos")


class GalleryUpdateForm(forms.ModelForm):
    """
    A form for updating gallery. Includes all the fields on
    the gallery, but replaces the users fields to be only readable.
    """

    class Meta:
        model = Gallery
        fields = "__all__"

