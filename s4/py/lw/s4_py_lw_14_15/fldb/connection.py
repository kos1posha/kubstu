from sqlite3 import connect, Connection, Cursor, Error

from logs import loger


# connection class for filmlibrary database
class FLDBConnection:
    __connection: Connection
    __cursor: Cursor
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            loger.write(200, 'Connection established')
        return cls.__instance

    def __init__(self):
        db_path = r'C:\Users\admin\source\repos\kubstu\s4\py\lw\s4_py_lw_14_15\fldb\filmlibrary.db'
        self.__connection = connect(db_path)
        self.__cursor = self.__connection.cursor()

    def __del__(self):
        self.__connection.close()

    def rich_execute(self, query, write_log=True, return_error=False):
        code, title, error = 0, 'Unknown', None
        try:
            self.__cursor.execute(query)
            self.__connection.commit()
            code, title = 200, 'Query completed successfully'
        except Error as e:
            code, title, error = 500, 'SQL error', e
        finally:
            if write_log: loger.write(code, title, query, error)
            if return_error: return code == 200
            return self.__cursor.fetchall()

    def insert_rows(self, table, values):
        values = [values] if values.__class__ is tuple else values
        query = f'INSERT INTO {table} VALUES {", ".join([str(value) for value in values])}'
        return True if self.rich_execute(query, return_error=True) else False

    def delete_rows(self, table, where=None):
        query = f'DELETE FROM {table} '
        if where: query += f'WHERE {where}'
        return self.rich_execute(query)

    def select_rows(self, table, where=None):
        query = f'SELECT * FROM {table} '
        if where: query += f'WHERE {where}'
        return self.rich_execute(query)

    def get_table_signature(self, table, only_headers=True):
        query = (f"SELECT pti.name, pti.type, pti.dflt_value\n"
                 f"FROM sqlite_master AS sm, pragma_table_info(sm.name) AS pti\n"
                 f"WHERE sm.type = 'table' and sm.name = '{table}'")
        result = self.rich_execute(query)
        return [row[0] for row in result] if only_headers else result
