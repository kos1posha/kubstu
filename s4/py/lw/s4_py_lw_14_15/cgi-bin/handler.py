from builder import *
from fldb.connection import FLDBConnection


# handler for cgi-script action.py


def delete_slice(table_name, start, end):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name)
    table_data = connection.select_rows(table_name, f'ID BETWEEN {start} AND {end}')
    connection.delete_rows(table_name, f'ID BETWEEN {start} AND {end}')
    head = f'<h2 class="h2 text-center">В таблице "{translate_table(table_name)}" нет записей</h2>'
    return head if len(table_data) == 0 else \
        f'<h2 class="h2 text-center">Следующие записи были удалены из таблицы</h2>' + \
        tabs(draw_table(table_name, table_signature, table_data), 5)


def delete_id(table_name, id):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name)
    table_data = connection.select_rows(table_name, f'ID = {id}')
    connection.delete_rows(table_name, f'ID = {id}')
    head = f'<h2 class="h2 text-center">В таблице "{translate_table(table_name)}" нет записи с индексом {id}</h2>'
    return head if len(table_data) == 0 else \
        f'<h2 class="h2 text-center">Следующая запись была удалена из таблицы "{translate_table(table_name)}"</h2>' + \
        tabs(draw_table(table_name, table_signature, table_data), 5)


def view_all(table_name):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name)
    table_data = connection.select_rows(table_name)
    head = f'<h2 class="h2 text-center">В таблице "{translate_table(table_name)}" нет записей</h2>'
    return head if len(table_data) == 0 else tabs(draw_table(table_name, table_signature, table_data), 5)


def view_slice(table_name, start, end):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name)
    table_data = connection.select_rows(table_name, f'ID BETWEEN {start} AND {end}')
    head = f'<h2 class="h2 text-center">В таблице "{translate_table(table_name)}" нет записей c {start} по {end} индексы</h2>'
    return head if len(table_data) == 0 else tabs(draw_table(table_name, table_signature, table_data), 5)


def view_id(table_name, id):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name)
    table_data = connection.select_rows(table_name, f'ID = {id}')
    head = f'<h2 class="h2 text-center">В таблице "{translate_table(table_name)}" нет записи с индексом {id}</h2>'
    return head if len(table_data) == 0 else tabs(draw_table(table_name, table_signature, table_data), 5)


def view(table_name, table_data):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name)
    return tabs(draw_table(table_name, table_signature, table_data), 5)


def pre_add(table_name):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name, only_headers=False)
    button = '\n<div class="text-center">' \
             '\n  <button class="text-center btn btn-primary w-25">Добавить</button>' \
             '\n</div>'
    return tabs(draw_inserted_table(table_name, table_signature) + button, 5)


def add(table_name, new_data):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name)
    head = '<h2 class="h2 text-center">Следующая строк была добавлена в таблицу</h2>'
    if not connection.insert_rows(table_name, new_data):
        head = f'<h2 class="h2 text-center">Что-то пошло не так...</h2>' \
                f'<h3 class="h3 text-center">Следующая строка не была добавлена в таблицу</h3>'
    return tabs(head + draw_table(table_name, table_signature, new_data), 5)

def pre_update(table_name, id):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name, only_headers=False)
    table_data = connection.select_rows(table_name, f'ID = {id}')
    head = f'<h2 class="h2 text-center">В таблице "{translate_table(table_name)}" нет записи с индексом {id}</h2>'
    button = '\n<div class="text-center">' \
             '\n  <button class="text-center btn btn-primary w-25">Изменить</button>' \
             '\n</div>'
    return head if table_data == 0 else tabs(draw_inserted_table(table_name, table_signature, table_data) + button, 5)

def update(table_name, new_data):
    connection = FLDBConnection()
    table_signature = connection.get_table_signature(table_name)
    old_data = connection.select_rows(table_name, f'ID = {new_data[0][0]}')
    connection.delete_rows(table_name, f'ID = {new_data[0][0]}')
    connection.insert_rows(table_name, new_data)
    head = '<h2 class="h2 text-center">Следующая строк была изменена</h2>'
    between =  '<h2 class="h2 text-center">на</h2>'
    return tabs(head + draw_table(table_name, table_signature, old_data, False) +
                between + draw_table(table_name, table_signature, new_data, False), 5)