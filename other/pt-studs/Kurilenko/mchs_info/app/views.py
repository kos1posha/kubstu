from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView

from app.models import Article


class MainPageView(ListView):
    template_name = 'main.html'
    queryset = Article.objects.all()
    context_object_name = 'articles'

    def get_queryset(self):
        return reversed(self.queryset)


class AboutView(TemplateView):
    template_name = 'about.html'


class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'article'


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
