from datetime import timedelta

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

    def __get_last_months(self, m, y):
        months = [*range(1, 13)]
        return [(m, y) for m in months[m - 1::-1]] + [(m, y - 1) for m in months[12:m - 1:-1]]

    def __transform_to_pie_data(self, data):
        total_sum = sum(data)
        result = []
        cumulative_sum = 0
        for num in data:
            ratio = num / total_sum
            cumulative_sum += ratio
            result.append((round(ratio, 2), round(cumulative_sum, 2)))
        return [[str(r).replace(',', '.') for r in rs] for rs in result]

    def __cities_trips_pie(self, cities):
        cities_by_trips_count = [(c, c.trips.count()) for c in sorted(cities, key=lambda c: c.trips.count(), reverse=True)]
        cities_by_trips_count = cities_by_trips_count[:7] + [('Другие', sum([c[1] for c in cities_by_trips_count[7:]]))]
        cities_by_trips_count = list(zip([c[0] for c in cities_by_trips_count], self.__transform_to_pie_data([c[1] for c in cities_by_trips_count])))
        return cities_by_trips_count

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = timezone.now()

        trips = Trip.objects.all()
        tickets = Ticket.objects.all()
        cities_to = To.objects.all()

        active_trips = trips.filter(end_dt__gt=now)
        owned_tickets = tickets.filter(owned=True)

        city_to_popularity_list = sorted(cities_to, key=lambda to: len(to.owned_tickets), reverse=True)

        months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
        kppm = sorted([(months[m], trips.filter(start_dt__month=m, start_dt__year=y).count()) for m, y in self.__get_last_months(now.month, now.year)], key=lambda x: x[1], reverse=True)
        kkbpm = sorted([(months[m], owned_tickets.filter(trip__start_dt__month=m, trip__start_dt__year=y).count()) for m, y in self.__get_last_months(now.month, now.year)], key=lambda x: x[1], reverse=True)

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
                'name': 'Статистика по городам',
                'metric_rows': [{
                    'Самый посещаемый город': city_to_popularity_list[0],
                    'Самый непосещаемый город': city_to_popularity_list[-1],
                }],
                'charts': [{
                    'name': 'Количество купленных билетов по городам',
                    'type': 'column',
                    'classes': 'show-heading show-labels data-spacing-4 data-outside',
                    'data': [(to, to.owned_tickets.count()) for to in city_to_popularity_list[:7]],
                    'max_data': city_to_popularity_list[0].owned_tickets.count() + 25,
                    'color': 'rgba(90,165,255,0.5)',
                    'size': '6',
                }, {
                    'name': 'Количество поездок по городам',
                    'type': 'pie',
                    'classes': 'show-labels show-heading',
                    'data': self.__cities_trips_pie(cities_to),
                    'max_data': 1,
                    'size': '6',
                }, {
                    'name': 'Количество активных поездок по городам',
                    'type': 'column',
                    'classes': 'show-heading show-labels data-spacing-4 data-outside',
                    'data': sorted([(to, to.trips.filter(end_dt__gt=now).count()) for to in city_to_popularity_list], key=lambda x: x[1], reverse=True)[:7],
                    'max_data': city_to_popularity_list[0].trips.filter(end_dt__gt=now).count() + 2,
                    'color': 'rgba(90,255,165,0.5)',
                    'size': '6',
                }, {
                    'name': 'Соотношение купленных билетов к общему количеству по городам',
                    'type': 'area',
                    'classes': 'show-heading show-labels data-spacing-4 data-outside',
                    'data': sorted([(to, str(round((owned_tickets.filter(trip__to=to).count() / tickets.filter(trip__to=to).count()) if tickets.filter(trip__to=to).count() != 0 else 0, 2)).replace(',', '.')) for to in city_to_popularity_list], key=lambda x: x[1], reverse=True)[:7],
                    'max_data': 1,
                    'color': 'rgba(255,45,90,0.5)',
                    'size': '6',
                }]}, {
                'name': 'Статистика по времени',
                'metric_rows': [{
                    'Поездок за последний месяц': trips.filter(start_dt__lt=now, start_dt__gt=now - timedelta(days=28)).count(),
                    'Поездок за последний квартал': trips.filter(start_dt__lt=now, start_dt__gt=now - timedelta(days=112)).count(),
                    'Поездок за последний год': trips.filter(start_dt__lt=now, start_dt__gt=now - timedelta(days=365)).count(),
                }],
                'charts': [{
                    'name': 'Количество поездок по месяцам',
                    'type': 'bar',
                    'classes': 'show-labels show-heading data-start data-spacing-2',
                    'data': kppm,
                    'max_data': max(kppm, key=lambda k: k[1])[1] + 10,
                    'color': 'rgba(165,60,60,0.5)',
                    'size': '6',
                }, {
                    'name': 'Количество купленных билетов по месяцам',
                    'type': 'bar',
                    'classes': 'show-labels show-heading data-start data-spacing-2',
                    'data': kkbpm,
                    'max_data': max(kkbpm, key=lambda k: k[1])[1] + 10,
                    'color': 'rgba(60,165,60,0.5)',
                    'size': '6',
                }]}
            ]
        })
        return context
