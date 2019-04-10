from django.shortcuts import render
from django.views.generic import View

from apps.core.models.event import Event
from apps.core.models.news import News


class Home(View):
    """
    Its the Home Page view.
    It should contain the last events and news to be render on website.
    """

    def get(self, request):
        # Getting objects
        events = Event.objects.all().order_by("starts_at")[:8]
        news = News.objects.all().order_by("publish_date")[:9]

        # Creating context
        context = {"events": events, "news": news}

        return render(request, "home.html", context)
