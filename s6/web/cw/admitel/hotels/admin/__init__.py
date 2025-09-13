from .user_admin import UserAdmin
from hotels import models

from django.contrib import admin
from django.contrib.auth import models as djmodels

admin.site.unregister(djmodels.Group)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Administrator)
admin.site.register(models.Branch)
admin.site.register(models.Hotel)
admin.site.register(models.Room)
