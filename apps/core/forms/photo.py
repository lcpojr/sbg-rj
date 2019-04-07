from django import forms

from apps.core.models.photo import Photo


class PhotoCreateForm(forms.ModelForm):
    """
    A form for creating new photos. Includes all the required
    fields.
    """

    class Meta:
        model = Photo
        fields = ("image",)


class PhotoUpdateForm(forms.ModelForm):
    """
    A form for updating photos. Includes all the fields on
    the photos, but replaces the users fields to be only readable.
    """

    class Meta:
        model = Photo
        fields = "__all__"

