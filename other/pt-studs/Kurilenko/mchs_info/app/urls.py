from django.urls import path

from app import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('writer/', views.WriterView.as_view(), name='writer'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('article/<slug:slug>/', views.ArticleView.as_view(), name='article'),
    path('article/<slug:slug>/views/', views.ArticleViewsAnalyticView.as_view(), name='article_views'),
    path('article/<int:pk>/delete/', views.DeleteArticleView.as_view(), name='delete'),
    path('auth/', views.AuthView.as_view(), name='auth'),
    path('analytics/', views.GlobalAnalyticView.as_view(), name='analytics'),
]
