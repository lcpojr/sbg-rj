from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.core.models.event import Event
from apps.core.models.gallery import Gallery
from apps.core.models.news import News
from apps.core.models.product import Product


class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = "never"

    def items(self):
        return [
            "home",
            "events",
            "gallery",
            "news",
            "products",
            "publications",
            "contact",
            "about",
            "regionals",
        ]

    def location(self, namespace):
        return reverse("web:{}".format(namespace))


class EventSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Event.objects.all()

    def location(self, obj):
        return reverse("web:events-show", kwargs={"slug": obj.slug})

    def lastmod(self, obj):
        return obj.updated_at


class GallerySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Gallery.objects.all()

    def location(self, obj):
        return reverse("web:gallery-show", kwargs={"slug": obj.slug})

    def lastmod(self, obj):
        return obj.updated_at


class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return News.objects.all()

    def location(self, obj):
        return reverse("web:news-show", kwargs={"slug": obj.slug})

    def lastmod(self, obj):
        return obj.updated_at


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return reverse("web:products-show", kwargs={"slug": obj.slug})

    def lastmod(self, obj):
        return obj.updated_at
