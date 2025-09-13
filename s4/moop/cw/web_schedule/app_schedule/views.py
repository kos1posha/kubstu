from datetime import datetime

from django.shortcuts import render

from app_schedule.proxies import ApiStruct, ApiTimetable


def schedule_group(request):
    def week_days():
        return ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    if request.method == 'GET':
        study_form = bool(request.GET.get('study-form')) if request.GET.get('study-form') != '-' else None
        try: department = int(request.GET.get('department'))
        except: department = None
        try: course = int(request.GET.get('course'))
        except: course = None
        group = request.GET.get('group')

    departments = ApiStruct.get_departments()
    groups = ApiStruct.get_groups(study_form=study_form, department=department, course=course)

    timetable = ApiTimetable.group(group)
    week_day = week_days()[datetime.weekday(datetime.now())]

    context = {'departments': departments, 'courses': [1, 2, 3, 4, 5, 6], 'groups': groups, 'week_day': week_day}
    if study_form is not None: context['selected_study_form'] = study_form
    if department is not None: context['selected_department'] = department
    if course is not None: context['selected_course'] = course
    if group is not None: context['selected_group'] = group
    try: int(timetable)
    except: context['timetable'] = timetable

    return render(request, 'schedule/schedule.html', context)
