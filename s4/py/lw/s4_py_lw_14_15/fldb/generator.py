import secrets
from random import randint
from datetime import datetime, timedelta
from random_name import generate_name


def __random_fullname():
    return generate_name().title().split('-')[:-1]


def __random_sex():
    return 'm' if randint(0, 1) else 'w'


def __random_date(start, end, format):
    return (start + timedelta(randint(0, (end - start).days))).strftime(format)

def __random_time():
    times = [
        '01:13',
        '02:58',
        '01:58',
        '03:28',
        '05:03',
        '02:18',
        '03:13',
        '06:23',
        '05:53',
        '02:48'
    ]
    return times[randint(0, 8)]

def __random_phone():
    return f'8{str(randint(9000000000, 9999999999))}'


def __random_email():
    domains = [
        'mail.ru', 'inbox.ru', 'bk.ru', 'list.ru', 'internet.ru', 'yandex.ru',
        'yahoo.com', 'gmail.com', 'hotmail.com', 'outlook.com'
    ]
    return f'{secrets.token_hex(8)}@{domains[randint(0, 9)]}'


def random_user(id):
    first_name, second_name = __random_fullname()
    sex = __random_sex()
    phone_number = __random_phone()
    email = __random_email()
    birth_day = __random_date(datetime(1970, 1, 1), datetime(2005, 1, 1), '%d.%m.%Y')
    return id, first_name, second_name, sex, phone_number, email, birth_day


def random_client(user_id):
    id = user_id
    registration_date = __random_date(datetime(2012, 6, 1), datetime.now(), '%d.%m.%Y')
    trust_status_id = randint(1, 4)
    return id, registration_date, user_id, trust_status_id


def random_librarian(user_id):
    id = user_id
    speciality_id = randint(1, 4)
    work_schedule_id = randint(1, 8)
    return id, user_id, speciality_id, work_schedule_id


def random_movie(id):
    title = ": ".join(__random_fullname())
    description = 'NULL'
    running_time = __random_time()
    release_date = __random_date(datetime(1990, 1, 1), datetime(2022, 1, 1), '%Y-%m-%d')
    genre_id = randint(1, 9)
    age_rating_id = randint(1, 5)
    country_id = randint(1, 7)
    film_company_id = randint(1, 19)
    distributor_id = randint(1, 15)
    cinematographer_id = randint(1, 19)
    director_id = randint(1, 18)
    producer_id = randint(1, 17)
    musician_id = randint(1, 16)
    editor_id = randint(1, 19)
    return id, title, description, running_time, release_date, genre_id, age_rating_id, country_id, film_company_id, \
        distributor_id, cinematographer_id, director_id, producer_id, musician_id, editor_id