from django.contrib import admin

from main import models


admin.site.register(models.BusStation)
admin.site.register(models.Contact)
admin.site.register(models.To)
admin.site.register(models.Trip)
admin.site.register(models.Ticket)
