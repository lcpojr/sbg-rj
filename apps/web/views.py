from django.shortcuts import render
from django.views.generic import View

from apps.core.models.event import Event as EventModel
from apps.core.models.news import News as NewsModel


class Home(View):
    """
    Its the Home Page view.
    It should contain the last events and news to be render on website.
    """

    def get(self, request):
        # Getting objects
        events = EventModel.objects.all().order_by("starts_at")[:8]
        news = NewsModel.objects.all().order_by("publish_date")[:9]

        # Creating context
        context = {"events": events, "news": news}

        return render(request, "home.html", context)


class Events(View):
    """
    Its the Events view.
    It should contain show the list of events and the details of it.
    """

    def get(self, request, slug=None):
        if slug:
            event = EventModel.objects.get(slug=slug)
            return render(request, "events-show.html", {"event": event})
        else:
            events = EventModel.objects.all().order_by("starts_at")
            return render(request, "events.html", {"events": events})


class News(View):
    """
    Its the News view.
    It should contain show the list of news and the details of it.
    """

    def get(self, request, slug=None):
        if slug:
            news = NewsModel.objects.get(slug=slug)
            return render(request, "news-show.html", {"news": news})
        else:
            news = NewsModel.objects.all().order_by("publish_date")
            return render(request, "news.html", {"news": news})
