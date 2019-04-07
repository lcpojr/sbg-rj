from django import forms

from apps.core.models.publication import Publication


class PublicationCreateForm(forms.ModelForm):
    """
    A form for creating new publications. Includes all the required
    fields.
    """

    class Meta:
        model = Publication
        fields = ("name", "document", "category")


class PublicationUpdateForm(forms.ModelForm):
    """
    A form for updating publications. Includes all the fields on
    the publication, but replaces the users fields to be only readable.
    """

    class Meta:
        model = Publication
        fields = "__all__"

