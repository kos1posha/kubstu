from django import template


register = template.Library()


@register.filter
def area_n(some_list, current_index):
    try:
        return some_list[int(current_index) + 1][1]
    except:
        return some_list[int(current_index)][1]


@register.filter
def pie_p(some_list, current_index):
    try:
        if (ind := int(current_index)) == 0:
            raise IndexError
        return some_list[ind - 1][1][1]
    except:
        return 0
