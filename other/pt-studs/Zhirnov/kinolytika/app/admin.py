from django.apps import apps
from django.contrib import admin
from django.contrib.auth.models import Group


admin.site.unregister(Group)
models = apps.get_app_config('app').get_models()
for model in models:
    admin.site.register(model)
