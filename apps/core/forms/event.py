from django import forms

from apps.core.models.event import Event


class EventCreateForm(forms.ModelForm):
    """
    A form for creating new events. Includes all the required
    fields.
    """

    class Meta:
        model = Event
        fields = (
            "title",
            "description",
            "starts_at",
            "ends_at",
            "image",
            "icon",
            "apresentation",
        )


class EventUpdateForm(forms.ModelForm):
    """
    A form for updating events. Includes all the fields on
    the event, but replaces the users fields to be only readable.
    """

    class Meta:
        model = Event
        fields = "__all__"

