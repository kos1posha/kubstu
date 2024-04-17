from django.contrib import admin

from calculator import models


admin.site.register(models.Position)
admin.site.register(models.Employee)
admin.site.register(models.Bonus)
admin.site.register(models.DefaultTaxes)
