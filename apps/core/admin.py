from django.contrib import admin
from django.contrib.admin import AdminSite

from .custom_admins.user import CustomUserAdmin
from .custom_admins.director import CustomDirectorAdmin
from .custom_admins.event import CustomEventAdmin
from .custom_admins.news import CustomNewsAdmin

from .models.user import User
from .models.director import Director
from .models.event import Event
from .models.news import News


class CustomAdminSite(AdminSite):
    site_header = "SBG-RJ (Administração)"
    site_header = "Sociedade brasileira de geologia"
    site_title = "SBG-RJ"
    index_title = "Administração"


admin_site = CustomAdminSite(name="custom_admin")

# Registering admin endpoints

admin_site.register(User, CustomUserAdmin)
admin_site.register(Director, CustomDirectorAdmin)
admin_site.register(Event, CustomEventAdmin)
admin_site.register(News, CustomNewsAdmin)
