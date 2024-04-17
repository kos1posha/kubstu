from django.urls import reverse_lazy
from django.views.generic import DeleteView

from sklad_app.models import Storage


class DeleteStorageView(DeleteView):
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        self.request.session['init_storage_id'] = pk
        return Storage.objects.filter(id=pk).first()
