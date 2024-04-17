from django.views.generic import TemplateView

from sklad_app.utils import get_index_forms


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(get_index_forms(self.request))
        return context
