from django.contrib import admin

from .custom_admins.user import CustomUserAdmin
from .models.user import User

admin.site.register(User, CustomUserAdmin)
