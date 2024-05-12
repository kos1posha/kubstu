from datetime import date, timedelta

from django import template
from django.template.defaultfilters import date as _
from django.utils import timezone

from app.models import HallPlace, Ticket


register = template.Library()


@register.filter
def date_format(value):
    now = timezone.now()
    if isinstance(value, date):
        if value == now.date():
            return 'сегодня'
        if value == now.date() + timedelta(days=1):
            return 'завтра'
        elif value == now.date() + timedelta(days=2):
            return 'послезавтра'
        elif value == now.date() + timedelta(days=2):
            return 'через 2 дня'
    if value.year == now.year:
        return _(value, 'j E')
    return value


@register.filter
def places_owned_by(value, user_id):
    tickets = Ticket.objects.filter(filmshow=value, owner_id=user_id)
    return HallPlace.objects.filter(hall=value.hall, ticket__in=tickets)
