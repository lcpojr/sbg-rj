from django.contrib import admin

from .custom_admins.user import CustomUserAdmin
from .custom_admins.director import CustomDirectorAdmin

from .models.user import User
from .models.director import Director

admin.site.register(User, CustomUserAdmin)
admin.site.register(Director, CustomDirectorAdmin)
