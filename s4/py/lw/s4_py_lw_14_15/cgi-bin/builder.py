from fldb.initializer import translate_table, translate_field


# content builder for cgi content
def concat(strings):
    return ''.join(strings)


def tabs(string, count, tab='  '):
    return '\n'.join([tab * count + line for line in string.split('\n')])

def draw_inserted_table(table, cols, updated_row=None, with_caption=True):
    headers = [col[0] for col in cols]
    types = [col[1] for col in cols]

    def tr(data):
        return f'        <tr>\n{data}        </tr>\n'

    def th(data, scope):
        if data == 'NULL': data = '-'
        return f'          <th scope="{scope}" class="align-top justify-content-evenly">{translate_field(data) if scope == "col" else data}</th>\n'

    def td(row_name, type, ind, row=None):
        value = "" if (row is None or row == "None" or row == "NULL") else row
        data = '<h4 class="text-center">Что-то пошло не так...<\h4>'
        if row_name == 'ID':
            type = 'ID'
        elif row_name == 'Title' or row_name == 'RusTitle' or row_name == 'FirstName' or row_name == 'LastName' or row_name == 'Name':
            type = 'TITLE'
        elif row_name == 'RunningTime':
            type = 'MOV_TIME'
        elif row_name == 'ReleaseDate' or row_name == 'DateTime' or row_name == 'Duration' or row_name == 'BirthDay':
            type = 'MOV_DATE'
        elif row_name == 'PhoneNumber':
            type = 'PHONE'
        elif row_name == 'Email':
            type = 'EMAIL'
        elif row_name == 'BirthDay' or row_name == 'DateTime' or row_name == 'Duration':
            type = 'USER_DATE'
        elif row_name == 'Active' or row_name == 'Monday' or row_name == 'Tuesday' or row_name == 'Wednesday' or row_name == 'Thursday' or row_name == 'Friday' or row_name == 'Saturday' or row_name == 'Sunday':
            type = 'BOOL'
        elif row_name == 'Sex':
            type = 'SEX'

        if type == 'ID':
            data = f'<input required {"readonly" if value != "" else ""} name="input{ind}" value="{value}" type="number" class="input-group-text mw-90px" min="1" maxlength="5" step="1">'
        elif type == 'PHONE':
            data = f'<input required name="input{ind}" value="{value}" class="input-group-text text-wrap align-content-start text-start textarea-title" size="11" type="tel" ' + 'pattern="8(9[0-9]{2})[0-9]{3}-[0-9]{2}-[0-9]{2}">'
        elif type == 'SEX':
            data = f'<select required name="input{ind}" class="form-select">' \
                   f'<option hidden="hidden"></option>' \
                   f'<option value="m">Мужской</option>' \
                   f'<option value="w">Женский</option>'
        elif type == 'EMAIL':
            data = f'<input required name="input{ind}" value="{value}" class="input-group-text text-wrap align-content-start text-start textarea-title" type="email">'
        elif type == 'TITLE':
            data = f'<textarea required name="input{ind}" maxlength="40" class="input-group-text text-wrap align-content-start text-start textarea-title">{value}</textarea>'
        elif type == 'TEXT':
            data = f'<textarea required name="input{ind}" maxlength="300" class="input-group-text text-wrap align-content-start text-start textarea-title">{value}</textarea>'
        elif type == 'MOV_TIME':
            data = f'<input required name="input{ind}" value="{value}" type="time" min="00:08:00" max="06:30:00" class="input-group-text">'
        elif type == 'MOV_DATE':
            data = f'<input required name="input{ind}" value="{value}" type="date" min="1895-03-22" class="input-group-text align-content-start text-start">'
        elif type == 'USER_TIME':
            data = f'<input required name="input{ind}" value="{value}" type="time" class="input-group-text">'
        elif type == 'USER_DATE':
            data = f'<input required name="input{ind}" value="{value}" type="date" class="input-group-text align-content-start text-start">'
        elif type == 'INTEGER':
            data = f'<input required name="input{ind}" value="{value}" type="number" class="input-group-text mw-90px" min="1" maxlength="5" step="1">'
        elif type == 'BOOL':
            data = f'<input name="input{ind}" value="Да" type="checkbox" class="form-check-input mw-90px" >'


        return f'          <td class="align-top justify-content-evenly">\n' \
               f'            {data}\n' \
               f'          </td>\n'

    caption = f'<h2 class="h2 text-center text-dark">{translate_table(table)}</h2>' if with_caption else ""
    head = tr(concat([th(col, "col") for col in headers]))
    body = tr(concat([td(headers[i], types[i], i, updated_row[0][i]) for i in range(len(cols))])) \
           if updated_row is not None else \
           tr(concat([td(headers[i], types[i], i) for i in range(len(cols))]))

    return \
       f'{caption}' \
        '<div class="container-sm table-responsive-sm">\n' \
        '  <div class="overflow-auto">\n' \
        '    <table class="table table-sm table-hover table-primary border align-middle">\n' \
       f'      <thead class="table-primary">\n' \
       f'{head}' \
       f'      </thead>\n' \
       f'      <tbody>\n' \
       f'{body}' \
       f'      </tbody>\n' \
        '    </table>\n' \
        '  </div>\n' \
        '</div>\n'



def draw_table(table, cols, rows, with_caption=True):
    def tr(data):
        return f'        <tr>\n{data}        </tr>\n'

    def th(data, scope):
        if data == 'NULL' or data is None: data = '-'
        return f'          <th scope="{scope}" class="align-top justify-content-evenly">{translate_field(data) if scope == "col" else data}</th>\n'

    caption = f'<h2 class="h2 text-center text-dark">{translate_table(table)}</h2>' if with_caption else ""
    head = tr(concat([th(col, "col") for col in cols]))
    body = concat([tr(concat([th(field, "row") for field in row])) for row in rows])

    return \
       f'{caption}' \
        '<div class="container-sm table-responsive-sm">\n' \
        '  <div class="overflow-auto">\n' \
        '    <table class="table table-sm table-hover table-primary border align-middle">\n' \
       f'      <thead class="table-primary">\n' \
       f'{head}' \
       f'      </thead>\n' \
       f'      <tbody>\n' \
       f'{body}' \
       f'      </tbody>\n' \
        '    </table>\n' \
        '  </div>\n' \
        '</div>\n'
