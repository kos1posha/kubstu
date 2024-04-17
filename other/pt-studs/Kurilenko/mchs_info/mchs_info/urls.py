from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from mchs_info import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    for prefix, root in settings.STATICFILES_DIRS:
        static(f'{settings.STATIC_URL}{prefix}/', document_root=root)
