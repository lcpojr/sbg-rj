from django.urls import path

from .views import Contact, Events, Gallery, Home, News, Products

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
    path("fale-conosco", Contact.as_view(), name="contact"),
    # Gallery uris
    path("galeria", Gallery.as_view(), name="gallery"),
    path("galeria/<slug:slug>/", Gallery.as_view(), name="gallery-show"),
]
