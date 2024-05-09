from datetime import date, timedelta

from django import template
from django.template.defaultfilters import date as _
from django.utils import timezone


register = template.Library()


@register.filter
def date_format(value):
    now = timezone.now()
    if isinstance(value, date):
        if value == now.date() + timedelta(days=1):
            return f'завтра'
        elif value == now.date() + timedelta(days=2):
            return f'послезавтра'
        elif value == now.date() + timedelta(days=2):
            return f'через 2 дня'
    if value.year == now.year:
        return _(value, 'j E')
    return value


@register.filter
def owned(value):
    pass
