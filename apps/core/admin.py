from django.contrib import admin

from .custom_admins.user import CustomUserAdmin
from .custom_admins.director import CustomDirectorAdmin
from .custom_admins.event import CustomEventAdmin

from .models.user import User
from .models.director import Director
from .models.event import Event

admin.site.register(User, CustomUserAdmin)
admin.site.register(Director, CustomDirectorAdmin)
admin.site.register(Event, CustomEventAdmin)
