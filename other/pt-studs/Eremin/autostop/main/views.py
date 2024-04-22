from babel.dates import format_timedelta
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import FormView, TemplateView

from main.forms import FiltersForm
from main.models import BusStation, Ticket, To, Trip


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


class AnalyticsView(TemplateView):
    template_name = 'analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = timezone.now()

        trips = Trip.objects.all()
        tickets = Ticket.objects.all()
        cities_to = To.objects.all()

        active_trips = trips.filter(end_dt__gt=now)
        owned_tickets = tickets.filter(owned=True)

        city_to_popularity_list = sorted(cities_to, key=lambda to: len(to.owned_tickets), reverse=True)

        context.update({
            'metrics_groups': [{
                'name': 'Статистика сервиса',
                'metric_rows': [{
                    'Время работы сервиса': format_timedelta(now - trips.first().start_dt, locale='ru_RU'),
                    'Всего поездок': [trips.count()],
                    'Активных поездок': [active_trips.count()],
                }, {
                    'Всего билетов': [tickets.count()],
                    'Процент купленных билетов': [int(round(owned_tickets.count() / tickets.count(), 2) * 100), '%'],
                    'Общая прибыль': [int(sum(ot.price for ot in owned_tickets)), '₽'],
                }]}, {
                'name': 'Города',
                'metric_rows': [{
                    'Самый посещаемый город': city_to_popularity_list[0],
                    'Самый непосещаемый город': city_to_popularity_list[-1],
                }],
                'charts': [{
                    'name': 'Количество купленных билетов по городам',
                    'classes': 'column show-heading show-labels data-spacing-4 data-outside',
                    'data': zip(city_to_popularity_list[:7], [to.owned_tickets.count() for to in city_to_popularity_list[:7]]),
                    'max_data': city_to_popularity_list[0].owned_tickets.count() + 25,
                    'color': 'rgba(90,165,255,0.5)',
                    'size': '6',
                }, {
                    'name': 'Количество поездок по городам',
                    'classes': 'column show-heading show-labels data-spacing-4 data-outside',
                    'data': zip(city_to_popularity_list[:7], [to.trips.count() for to in city_to_popularity_list[:7]]),
                    'max_data': city_to_popularity_list[0].trips.count() + 2,
                    'color': 'rgba(90,255,165,0.5)',
                    'size': '6',
                }]
            }]
        })
        return context
