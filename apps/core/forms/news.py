from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from apps.core.models.news import News


class NewsCreateForm(forms.ModelForm):
    """
    A form for creating new News. Includes all the required
    fields.
    """

    class Meta:
        model = News
        fields = ("title", "resume", "description", 
                  "publish_date", "image", "icon")


class NewsUpdateForm(forms.ModelForm):
    """
    A form for updating News. Includes all the fields on
    the news, but replaces the users fields to be only readable.
    """

    class Meta:
        model = News
        fields = "__all__"

