from django import forms

from apps.core.models.director import Director


class DirectorCreateForm(forms.ModelForm):
    """
    A form for creating new directors. Includes all the required
    fields.
    """

    class Meta:
        model = Director
        fields = ("first_name", "last_name", "role", "email")


class DirectorUpdateForm(forms.ModelForm):
    """
    A form for updating directors. Includes all the fields on
    the director, but replaces the users fields to be only readable.
    """

    class Meta:
        model = Director
        fields = "__all__"

