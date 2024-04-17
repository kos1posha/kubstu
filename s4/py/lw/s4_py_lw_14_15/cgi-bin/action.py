#!/usr/bin/env python3

from cgi import FieldStorage
from html import escape
from handler import *

form = FieldStorage()
table = escape(form.getfirst('table'))
action = escape(form.getfirst('action'))

content = '<h2 class="h2 text-center">Что-то пошло не так...</h2>'

if action == 'Delete slice':
    start = escape(form.getfirst('start'))
    end = escape(form.getfirst('end'))
    if start > end:
        content = f'<h2 class="h2 text-center">Начальное значение среза не может превышать конечное</h2>'
    else:
        content = delete_slice(table, start, end)
if action == 'Delete id':
    id = escape(form.getfirst('id'))
    content = delete_id(table, id)
if action == 'View all':
    content = view_all(table)
if action == 'View slice':
    start = escape(form.getfirst('start'))
    end = escape(form.getfirst('end'))
    if start > end:
        content = f'<h2 class="h2 text-center">Начальное значение среза не может превышать конечное</h2>'
    else:
        content = view_slice(table, start, end)
if action == 'View id':
    id = escape(form.getfirst('id'))
    content = view_id(table, id)
if action == 'Add':
    content = pre_add(table)
if action == 'Update':
    id = escape(form.getfirst('id'))
    content = pre_update(table, id)


print('Content-type: text/html\n')
print(f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Фильмотека</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="../templates/styles.css" rel="stylesheet">
  <link href="../images/favicon.png" type="image/png" rel="shortcut-icon">
  <link href="../images/favicon.png" type="image/png" rel="icon">
  <script src="../templates/scripts.js" type="text/javascript"></script>
</head>


<body style="background: url('../images/bg-default.jpg'); background-size: contain">
<div class="bg-white">
  <h1 class="h1 text-center caption-top">Фильмотека</h1>
  <h6 class="h6 text-center text-black-50">Контроль содержимого локальной базы данных</h6>
  <hr>
</div>


<div class="container-sm pad-bottom bg-dark">
  <div class="container-sm pad-bottom bg-danger">
    <div class="container-sm pad-bottom bg-warning">
      <div class="container-sm pad-bottom bg-success">
        
        <form class="container-sm pad-bottom bg-white" action="/cgi-bin/action.py" method="post">

          <br/>

          <div class="row justify-content-around">
            <div class="col text-center">
              <label class="form-label h4" for="table">Выберите таблицу</label>
              <select class="form-select" id="table" name="table" required>
                <option {"" if table != "Issuances" else "selected"} value="Issuances">Журнал выдач</option>
                <optgroup label="О фильмах">
                  <option {"" if table != "Movies" else "selected"} value="Movies">Фильмы</option>
                  <option {"" if table != "Genres" else "selected"} value="Genres">Жанры</option>
                  <option {"" if table != "AgeRatings" else "selected"} value="AgeRatings">Возрастные рейтинги</option>
                  <option {"" if table != "Countries" else "selected"} value="Countries">Страны</option>
                  <option {"" if table != "FilmCompanies" else "selected"} value="FilmCompanies">Кинокомпании</option>
                  <option {"" if table != "Distributors" else "selected"} value="Distributors">Дистрибьюторы</option>
                  <option {"" if table != "Cinematographers" else "selected"} value="Cinematographers">Операторы</option>
                  <option {"" if table != "Directors" else "selected"} value="Directors">Режиссеры</option>
                  <option {"" if table != "Producers" else "selected"} value="Producers">Продюсеры</option>
                  <option {"" if table != "Musicians" else "selected"} value="Musicians">Композиторы</option>
                  <option {"" if table != "Editors" else "selected"} value="Editors">Редакторы</option>
                </optgroup>
                <optgroup label="О дисках">
                  <option {"" if table != "MovieInstances" else "selected"} value="MovieInstances">Имеющиеся диски</option>
                  <option {"" if table != "DubbingStudios" else "selected"} value="DubbingStudios">Студии дубляжа</option>
                  <option {"" if table != "Adapters" else "selected"} value="Adapters">Носители</option>
                  <option {"" if table != "Languages" else "selected"} value="Languages">Языки</option>
                </optgroup>
                <optgroup label="О людях">
                  <option {"" if table != "Users" else "selected"} value="Users">Пользователи</option>
                  <option {"" if table != "Clients" else "selected"} value="Clients">Клиенты</option>
                  <option {"" if table != "Librarians" else "selected"} value="Librarians">Библиотекари</option>
                </optgroup>
                <optgroup label="О прочем">
                  <option {"" if table != "TrustStatuses" else "selected"} value="TrustStatuses">Статусы доверия</option>
                  <option {"" if table != "WorkSchedules" else "selected"} value="WorkSchedules">Рабочие расписания</option>
                  <option {"" if table != "Specialities" else "selected"} value="Specialities">Специальности</option>
                </optgroup>
              </select>
            </div>

            <div class="col text-center">
              <label class="form-label h4" for="action">Выберите действие</label>
              <select class="form-select" id="action" name="action" onchange="showHide(this.value)" required>
                <option hidden="hidden"></option>
                <option value="Add">Добавить</option>
                <option value="Update">Обновить</option>
                <optgroup label="Удалить">
                  <option value="Delete slice">Удалить срез</option>
                  <option value="Delete id">Удалить одно</option>
                </optgroup>
                <optgroup label="Просмотреть">
                  <option value="View all">Просмотреть все</option>
                  <option value="View slice">Просмотреть срез</option>
                  <option value="View id">Просмотреть одно</option>
                </optgroup>
              </select>

              <div class="row justify-content-center">
                <div class="col-4" style="display: none" id="start_block">
                  <label class="small text-black" for="start">Начало</label>
                  <input class="input-group-text" id="start" name="start" min="1" max="10000000" step="1" type="number">
                </div>
                <div class="col-4" style="display: none" id="id_block">
                  <label class="small text-black" for="id">ID</label>
                  <input class="input-group-text" id="id" name="id" min="1" max="10000000" step="1" type="number">
                </div>
                <div class="col-4" style="display: none" id="end_block">
                  <label class="small text-black" for="end">Конец</label>
                  <input class="input-group-text" id="end" name="end" min="1" max="10000000" step="1" type="number">
                </div>
              </div>
            </div>
          </div>

          <br/>

          <div class="text-center">
            <button class="text-center btn btn-primary w-auto">Отправить запрос</button>
          </div>

          <br/>

        </form>
        
        <form class="container-sm pad-bottom bg-white" action="/cgi-bin/update.py" method="post">
        <input name="table" value="{table}" hidden>
        <input name="action" value="{action}" hidden>
        
{content}
           
        </form>
        
      </div>
    </div>
  </div>
</div>

</body>
</html>""")
