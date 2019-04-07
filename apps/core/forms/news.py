from django import forms

from apps.core.models.news import News


class NewsCreateForm(forms.ModelForm):
    """
    A form for creating new news. Includes all the required
    fields.
    """

    class Meta:
        model = News
        fields = ("title", "resume", "description", "publish_date", "image", "icon")


class NewsUpdateForm(forms.ModelForm):
    """
    A form for updating news. Includes all the fields on
    the news, but replaces the users fields to be only readable.
    """

    class Meta:
        model = News
        fields = "__all__"

