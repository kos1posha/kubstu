from datetime import date, datetime



def write(code, title, query=None, error=None):
    date_format = '%d.%m.%Y'
    file = open(fr'C:\Users\admin\source\repos\kubstu\s4\py\lw\s4_py_lw_14_15\logs\{date.today().strftime(date_format)}.log', mode='a', encoding='utf-8')
    log = f'[{datetime.now()}] {code}: {title}'
    log += f'\n{error.__class__.__name__}: {error}' if error else ''
    log += f'\n{query}' if query else ''
    log += '\n\n'
    file.write(log)


