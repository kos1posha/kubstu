from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import FormView, TemplateView

from main.forms import FiltersForm
from main.models import BusStation, Trip


class IndexView(FormView):
    template_name = 'index.html'
    form_class = FiltersForm
    success_url = reverse_lazy('trips')
    extra_context = {
        'stations': BusStation.objects.all()
    }


class FindTripsView(TemplateView):
    template_name = 'find.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to = self.request.GET.get('to')
        date = self.request.GET.get('date')
        filters = {
            'start_dt__gte': timezone.now()
        }
        if to:
            filters['to_id'] = to
        if date and date != 'Когда угодно':
            y, m, d = [int(v) for v in date.split('-')]
            filters['start_dt__year'] = y
            filters['start_dt__month'] = m
            filters['start_dt__day'] = d
        context.update({
            'to': to or 'Куда угодно',
            'date': date or 'Когда угодно',
            'form': FiltersForm(to=to, date=date),
            'trips': Trip.objects.filter(**filters)
        })
        return context
