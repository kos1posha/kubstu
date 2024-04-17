from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from text_editor import settings


urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),
    path('admin/', admin.site.urls),
    path('', include('forum.urls'))
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
