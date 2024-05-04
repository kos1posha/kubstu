import os.path
from sqlite3 import Error, connect

from db.tables import tables


class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None and not issubclass(type(cls._instance), cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        db_path = os.path.abspath('db.sqlite3')
        self._connection = connect(db_path)
        self._cursor = self._connection.cursor()

    def __del__(self):
        self._connection.close()

    def execute(self, query):
        try:
            self._cursor.execute(query)
            self._connection.commit()
            return self._cursor.fetchall()
        except Error as e:
            print(e, query, sep='\n')
            return False

    def insert_rows(self, table, values):
        values = [values] if values.__class__ is tuple else values
        columns = ', '.join(c.split()[0][1:-1] for c in tables[table])
        query = f'INSERT INTO {table} ({columns}) VALUES {", ".join([str(value) for value in values])}'
        return True if self.execute(query) is not False else False

    def delete_rows(self, table, where=None):
        query = f'DELETE FROM {table} '
        if where: query += f'WHERE {where}'
        return self.execute(query)

    def select_rows(self, table, where=None):
        query = f'SELECT * FROM {table} '
        if where: query += f'WHERE {where}'
        return self.execute(query)

    def get_table_signature(self, table, only_headers=True):
        query = (f"SELECT pti.name, pti.type, pti.dflt_value\n"
                 f"FROM sqlite_master AS sm, pragma_table_info(sm.name) AS pti\n"
                 f"WHERE sm.type = 'table' and sm.name = '{table}'")
        result = self.execute(query)
        return [row[0] for row in result] if only_headers else result
