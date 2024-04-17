from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from sklad_app import views
from storager import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('', include('sklad_app.urls')),
]

if settings.DEBUG:
    for prefix, root in settings.STATICFILES_DIRS:
        static(f'{settings.STATIC_URL}{prefix}/', document_root=root)
