from django.urls import path

from sklad_app import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('create-storage/', views.CreateStorageView.as_view(), name='create-storage'),
    path('edit-storage/<int:pk>/', views.EditStorageView.as_view(), name='edit-storage'),
    path('delete-storage/<int:pk>/', views.DeleteStorageView.as_view(), name='delete-storage'),
    path('create-product/<int:storage_id>/', views.CreateProductView.as_view(), name='create-product'),
    path('product-count/<int:pk>/', views.ProductCountView.as_view(), name='product-count'),
    path('delete-product/<int:pk>/', views.DeleteProductView.as_view(), name='delete-product'),
    path('edit-product/<int:pk>/', views.EditProductView.as_view(), name='edit-product'),
]
