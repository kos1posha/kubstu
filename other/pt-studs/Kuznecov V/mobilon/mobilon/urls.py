from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from mobilon import settings
from salon import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('history/', views.HistoryView.as_view(), name='history'),
    path('', views.CatalogView.as_view(), name='catalog'),

    path('add_product/<int:id>/', views.AddProductToBasketView.as_view(), name='add_product'),
    path('remove_product/<int:id>/', views.RemoveProductFromBasketView.as_view(), name='remove_product'),
    path('done_purchase/', views.DonePurchaseView.as_view(), name='done_purchase'),
    path('clear_backet/', views.ClearBasketView.as_view(), name='clear_basket'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
