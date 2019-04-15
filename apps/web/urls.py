from django.urls import path

<<<<<<< HEAD
from .views import Contact, Events, Gallery, Home, News, Products
=======
from .views import Contact, Events, Home, News, Products, About
>>>>>>> feat: add about-page template and conifgures urls and view

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
<<<<<<< HEAD
    # Gallery uris
    path("galeria", Gallery.as_view(), name="gallery"),
    path("galeria/<slug:slug>/", Gallery.as_view(), name="gallery-show"),
=======
    # About uris
    path("sobre", About.as_view(), name="about")
>>>>>>> feat: add about-page template and conifgures urls and view
]
