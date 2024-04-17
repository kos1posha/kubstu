from django.urls import reverse_lazy
from django.views.generic import UpdateView

from sklad_app.forms import EditStorageForm
from sklad_app.models import Storage


class EditStorageView(UpdateView):
    form_class = EditStorageForm
    success_url = reverse_lazy('index')
    http_method_names = ['post', 'options']

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        self.request.session['init_storage_id'] = pk
        return Storage.objects.get(id=pk)
