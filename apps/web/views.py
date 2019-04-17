from datetime import datetime

from django.shortcuts import render
from django.views.generic import View

from apps.core.models.event import Event as EventModel
from apps.core.models.news import News as NewsModel
from apps.core.models.product import Product as ProductModel
<<<<<<< HEAD
from apps.core.models.gallery import Gallery as GalleryModel
from apps.core.models.photo import Photo as PhotoModel
=======
>>>>>>> 35b0673bd9459387b37ae012f54898ba2d631181
from apps.core.models.director import Director as DirectorModel

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

            """
            send_mail(
                "Você recebeu um novo pedido pelo seu WEBSITE",
                "Cliente: {} \n Telefone: {} \n Email: {} \n {}".format(
                    contact["nome"],
                    contact["telefone"],
                    contact["email"],
                    contact["descricao"],
                ),
                settings.DEFAULT_FROM_EMAIL,
                settings.CONTACT_EMAILS,
            )
            """
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

            """
            send_mail(
                "Uma pessoa entrou em contato pelo seu WEBSITE",
                "Cliente: {} \n Telefone: {} \n Email: {} \n {}".format(
                    contact["nome"],
                    contact["telefone"],
                    contact["email"],
                    contact["descricao"],
                ),
                settings.DEFAULT_FROM_EMAIL,
                settings.CONTACT_EMAILS,
            )
            """
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


def group_directors(directors):
    """
    This function will group all directors by year
    It will be used inside the about View
    """
    history = []
    for director in directors:
        if history == []:
            history.append({"year": director.started_at.year, "directors": [director]})
            check = False

        for value in history:
            if value['year'] == director.started_at.year:
                value['directors'].append(director)
                check = True
            else:
                check = False

        if not check:
            history.append({"year": director.started_at.year, "directors": [director]})
    
    return history



class About(View):
    """
    Its the About Page view.
    It should contain all the directors to be rendered in the website.
    """    

    def get(self, request):
        # Getting objects
        directors = DirectorModel.objects.all().order_by("-started_at")
        directors_history = group_directors(directors)
        current_year = datetime.now().year

        # Creating context
        context = {"directors": directors, "directors_history": directors_history, "current_year": current_year}

        return render(request, "about.html", context)
