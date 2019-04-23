from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView as Robots
from django.views.decorators.cache import cache_page

from .views import (
    About,
    Contact,
    Events,
    Gallery,
    Home,
    News,
    Products,
    Publication,
    Regionals,
)

from .sitemaps import (
    StaticSitemap,
    EventSitemap,
    GallerySitemap,
    NewsSitemap,
    ProductSitemap,
)

sitemaps = {
    "static": StaticSitemap,
    "events": EventSitemap,
    "galleries": GallerySitemap,
    "news": NewsSitemap,
    "products": ProductSitemap,
}

app_name = "web"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    # Events uris
    path("eventos", Events.as_view(), name="events"),
    path("eventos/<slug:slug>/", Events.as_view(), name="events-show"),
    # News uris
    path("noticias", News.as_view(), name="news"),
    path("noticias/<slug:slug>/", News.as_view(), name="news-show"),
    # Products uris
    path("produtos", Products.as_view(), name="products"),
    path("produtos/<slug:slug>/", Products.as_view(), name="products-show"),
    # Contact uris
    path("fale-conosco", cache_page(60 * 10)(Contact.as_view()), name="contact"),
    # Gallery uris
    path("galeria", Gallery.as_view(), name="gallery"),
    path("galeria/<slug:slug>/", Gallery.as_view(), name="gallery-show"),
    # About uris
    path("sobre", cache_page(60 * 10)(About.as_view()), name="about"),
    # Publications uirs
    path("publicacoes", Publication.as_view(), name="publications"),
    # Regionals uri
    path("regionais", cache_page(60 * 10)(Regionals.as_view()), name="regionals"),
    # Extras
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path(
        "robots.txt",
        Robots.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
