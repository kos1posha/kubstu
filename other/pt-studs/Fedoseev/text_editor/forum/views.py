from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView

from forum.forms import CreatePostForm
from forum.models import Post


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IndexView(FormView):
    form_class = CreatePostForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'posts': reversed(Post.objects.all()),
        })
        return context

    def form_valid(self, form):
        post = form.save(False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)
