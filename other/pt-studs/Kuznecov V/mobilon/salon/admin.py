from django.contrib import admin

from salon import models


admin.site.register(models.Category)
admin.site.register(models.Product)
