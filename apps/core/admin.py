from django.contrib.admin import AdminSite

from .custom_admins.user import CustomUserAdmin
from .custom_admins.director import CustomDirectorAdmin
from .custom_admins.event import CustomEventAdmin
from .custom_admins.news import CustomNewsAdmin
from .custom_admins.product import CustomProductAdmin
from .custom_admins.publication import CustomPublicationAdmin
from .custom_admins.photo import CustomPhotoAdmin
from .custom_admins.gallery import CustomGalleryAdmin

from .models.user import User
from .models.director import Director
from .models.event import Event
from .models.news import News
from .models.product import Product
from .models.publication import Publication
from .models.photo import Photo
from .models.gallery import Gallery


class CustomAdminSite(AdminSite):
    site_header = "SBG-RJ (Administração)"
    site_header = "Sociedade brasileira de geologia"
    site_title = "SBG-RJ"
    index_title = "Administração"


# Registering admin endpoints
admin_site = CustomAdminSite(name="custom_admin")
admin_site.register(User, CustomUserAdmin)
admin_site.register(Director, CustomDirectorAdmin)
admin_site.register(Event, CustomEventAdmin)
admin_site.register(News, CustomNewsAdmin)
admin_site.register(Product, CustomProductAdmin)
admin_site.register(Publication, CustomPublicationAdmin)
admin_site.register(Photo, CustomPhotoAdmin)
admin_site.register(Gallery, CustomGalleryAdmin)
