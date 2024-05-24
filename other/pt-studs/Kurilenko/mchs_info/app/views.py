import datetime
import datetime as dt

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView

from app.models import Article, ArticleDateViews


class MainPageView(ListView):
    template_name = 'main.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return reversed(Article.objects.all())


class AboutView(TemplateView):
    template_name = 'about.html'


class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increment_date_views()
        return response


class ArticleViewsAnalyticView(DetailView):
    model = Article
    template_name = 'article_views.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_views = ArticleDateViews.objects.filter(article=self.object, date__gt=dt.date.today() - dt.timedelta(days=14))
        max_views = max(article_views.values_list('views', flat=True))
        context['views_last_two_weeks'] = {article.date.strftime('%d.%m'): (article.views, max_views)
                                           for article in ArticleDateViews.objects.filter(article=self.object)}
        return context


class WriterView(CreateView):
    model = Article
    fields = ['main_photo', 'slug', 'title', 'preview', 'content']
    template_name = 'writer.html'
    extra_context = {
        'auth_form': AuthenticationForm(),
    }

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'slug': self.object.get_absolute_url()})


class DeleteArticleView(DeleteView):
    model = Article
    http_method_names = ['post']
    success_url = reverse_lazy('main')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Article.objects.get(pk=pk)


class AuthView(LoginView):
    http_method_names = ['post']
    template_name = 'writer.html'

    def form_invalid(self, form):
        return redirect('writer')


class GlobalAnalyticView(TemplateView):
    template_name = 'analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['articles_count'] = Article.objects.all().count()
        context['today_articles_count'] = Article.objects.filter(create__day=today.day, create__month=today.month, create__year=today.year).count()
        date_views = [sum(ArticleDateViews.objects.filter(date=dt.date.today() - dt.timedelta(days=i)).values_list('views', flat=True)) for i in range(14)]
        max_views = max(date_views)
        context['views_last_two_weeks'] = {(dt.date.today() - dt.timedelta(days=i)).strftime('%d.%m'): (dw, max_views) for i, dw in enumerate(date_views)}
        most_viewed_articles = sorted(Article.objects.all()[:7], key=lambda a: a.views(), reverse=True)
        max_viewed = most_viewed_articles[0].views()
        context['most_viewed_articles'] = {a.slug: (a.views(), max_viewed) for a in most_viewed_articles}
        return context
