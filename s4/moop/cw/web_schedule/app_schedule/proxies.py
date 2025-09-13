from datetime import datetime

from requests import api

import variables as VAR
from app_schedule.models import TimetablePair, TimetableDay, TimetableWeek


class ApiTimetable:
    @staticmethod
    def group(group_code, week_even=None, week_day=None, pair_number=None, pair_type=None):
        params = {'key': VAR.API_MASTER_KEY, 'group': group_code}
        if week_even is not None: params['week_even'] = week_even
        if week_day is not None: params['day'] = week_day
        if pair_number is not None: params['pair_number'] = pair_number
        if pair_type is not None: params['pair_type'] = pair_type
        response = api.get(url=VAR.API_URL + VAR.API_TIMETABLE_GROUP, params=params)
        if response.status_code != 200:
            return response.status_code
        else:
            timetable = []
            for week in response.json().get('response'):
                days = []
                for day in week.get('schedules'):
                    pairs = []
                    for pair in day.get('pairs'):
                        pairs.append(TimetablePair(
                            title = pair.get('pair_title'),
                            teacher_first_name = pair.get('teacher_name'),
                            teacher_last_name = pair.get('teacher_surname'),
                            teacher_patronymic = pair.get('teacher_patronymic'),
                            number = pair.get('pair_number'),
                            type = pair.get('pair_type'),
                            classroom = pair.get('classroom'),
                            period_start = pair.get('period_start'),
                            period_end = pair.get('period_end'),
                        ))
                    days.append(TimetableDay(day=day.get('day'), pairs=pairs))
                timetable.append(TimetableWeek(even=week.get('week_even'), days=days))
            return timetable

    @staticmethod
    def teacher(first_name, last_name, patronymic, format_raw=None, week_even=None, week_day=None, pair_number=None, pair_type=None):
        params = {'key': VAR.API_MASTER_KEY, 'first': first_name, 'second': last_name, 'third': patronymic}
        if format_raw is not None: params['raw'] = format_raw
        if week_even is not None: params['week_even'] = week_even
        if week_day is not None: params['day'] = week_day
        if pair_number is not None: params['pair_number'] = pair_number
        if pair_type is not None: params['pair_type'] = pair_type
        response = api.get(url=VAR.API_URL + VAR.API_TIMETABLE_TEACHER, params=params)
        if response.status_code != 200:
            return response.status_code
        else:
            teacher_timetable = response.json().get('response')
            return teacher_timetable

class ApiStruct:
    @staticmethod
    def get_all():
        params = {'key': VAR.API_MASTER_KEY}
        response = api.get(url=VAR.API_URL + VAR.API_STRUCT_ALL, params=params)
        if response.status_code != 200:
            return response.status_code
        else:
            university = response.json().get('response')
            return university

    @staticmethod
    def get_departments():
        params = {'key': VAR.API_MASTER_KEY}
        response = api.get(url=VAR.API_URL + VAR.API_STRUCT_DEPARTMENTS, params=params)
        if response.status_code != 200:
            return response.status_code
        else:
            departments = response.json().get('response').get('departments')
            return departments

    @staticmethod
    def get_groups(study_form=None, department=None, course=None):
        params = {'key': VAR.API_MASTER_KEY}
        if type(study_form) is bool: params['study_form'] = study_form
        if type(department) is int: params['department'] = department
        response = api.get(url=VAR.API_URL + VAR.API_STRUCT_GROUPS, params=params)
        if response.status_code != 200:
            return response.status_code
        else:
            departments: list = response.json().get('response').get('groups')
            if course is None or type(course) is str:
                return departments
            else:
                course_code = str(datetime.now().year % 100 - int(course))
                return list(filter(lambda d: d.startswith(course_code), departments))

    @staticmethod
    def get_group_info(group):
        params = {'key': VAR.API_MASTER_KEY, 'group': group}
        response = api.get(url=VAR.API_URL + VAR.API_STRUCT_GROUP_INFO, params=params)
        if response.status_code != 200:
            return response.status_code
        else:
            group_info = response.json().get('response')
            return group_info
