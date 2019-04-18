from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from apps.core.models.event import Event as EventModel
from apps.core.models.news import News as NewsModel
from apps.core.models.product import Product as ProductModel
from apps.core.models.gallery import Gallery as GalleryModel
from apps.core.models.photo import Photo as PhotoModel

from .forms import ContactCreateForm, OrderCreateForm


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


class Products(View):
    """
    Its the Products view.
    It should contain show the list of products and the details of it.
    It will also send a email notification.
    """

    def get(self, request, slug=None):
        form = OrderCreateForm()

        if slug:
            product = ProductModel.objects.get(slug=slug)
            context = {"form": form, "product": product, "message": None}
            return render(request, "products-show.html", context)
        else:
            products = ProductModel.objects.all().order_by("created_at")
            context = {"form": form, "products": products, "message": None}
            return render(request, "products.html", context)

    def post(self, request, slug=None):
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            message = True

            # Build admin message context
            message_context = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "description": form.cleaned_data["description"],
                "is_admin": True,
            }

            text_content = render_to_string("emails/order.txt", message_context)
            html_content = render_to_string("emails/order.html", message_context)

            # Build message data
            email_message = EmailMultiAlternatives(
                "Pedido recebido SBG-RJ",
                text_content,
                settings.DEFAULT_FROM_EMAIL,
                settings.CONTACT_EMAILS,
            )

            # Attach HTML content and sends the message
            email_message.attach_alternative(html_content, "text/html")
            email_message.content_subtype = "html"
            email_message.send()

            # Build client message context
            message_context["is_admin"] = False

            text_content = render_to_string("emails/order.txt", message_context)
            html_content = render_to_string("emails/order.html", message_context)

            # Build message data
            email_message = EmailMultiAlternatives(
                "Pedido recebido SBG-RJ",
                text_content,
                settings.DEFAULT_FROM_EMAIL,
                settings.CONTACT_EMAILS,
            )

            # Attach HTML content and sends the message
            email_message.attach_alternative(html_content, "text/html")
            email_message.content_subtype = "html"
            email_message.send()

        else:
            message = False

        if slug:
            product = ProductModel.objects.get(slug=slug)
            context = {"form": form, "product": product, "message": message}
            return render(request, "products-show.html", context)
        else:
            products = ProductModel.objects.all().order_by("created_at")
            context = {"form": form, "products": products, "message": message}
            return render(request, "products.html", context)


class Contact(View):
    """
    Its the Contact view.
    It should contain all contact information and send email functions.
    """

    def get(self, request):
        form = ContactCreateForm()
        return render(request, "contact.html", {"form": form})

    def post(self, request):
        form = ContactCreateForm(request.POST)

        if form.is_valid():
            message = True

            # Build admin message context
            message_context = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "subject": form.cleaned_data["subject"],
                "description": form.cleaned_data["description"],
                "is_admin": True,
            }

            text_content = render_to_string("emails/contact.txt", message_context)
            html_content = render_to_string("emails/contact.html", message_context)

            # Build message data
            email_message = EmailMultiAlternatives(
                "Contato recebido SBG-RJ",
                text_content,
                settings.DEFAULT_FROM_EMAIL,
                settings.CONTACT_EMAILS,
            )

            # Attach HTML content and sends the message
            email_message.attach_alternative(html_content, "text/html")
            email_message.content_subtype = "html"
            email_message.send()

            # Build client message context
            message_context["is_admin"] = False

            text_content = render_to_string("emails/contact.txt", message_context)
            html_content = render_to_string("emails/contact.html", message_context)

            # Build message data
            email_message = EmailMultiAlternatives(
                "Contato recebido SBG-RJ",
                text_content,
                settings.DEFAULT_FROM_EMAIL,
                settings.CONTACT_EMAILS,
            )

            # Attach HTML content and sends the message
            email_message.attach_alternative(html_content, "text/html")
            email_message.content_subtype = "html"
            email_message.send()

        else:
            message = False

        return render(request, "contact.html", {"form": form, "message": message})


class Gallery(View):
    """
    Its the Gallery view.
    It should contain all photos organized in albums.
    """

    def get(self, request, slug=None):
        if slug:
            gallery = GalleryModel.objects.get(slug=slug)
            photos = PhotoModel.objects.filter(gallery=gallery)

            context = {"gallery": gallery, "photos": photos}

            return render(request, "gallery-show.html", context)
        else:
            galleries = GalleryModel.objects.all().order_by("created_at")
            return render(request, "gallery.html", {"galleries": galleries})
