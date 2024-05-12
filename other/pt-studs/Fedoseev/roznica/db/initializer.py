from db import defaults
from db.connection import DBConnection
import db.models as dbm
from db.tables import tables


dt_format = f'%Y.%m.%d %H:%M:%S.%f'
short_dt_format = f'%H:%M %d.%m.%Y '


class DBInitializer:
    def __init__(self):
        self._connection = DBConnection()

    def reinit(self):
        self.drop_tables()
        self.create_tables()
        self.put_defaults()

    def put_defaults(self):
        for category in defaults.categories:
            dbm.categories.insert(**category)
        for product in defaults.products:
            dbm.products.insert(**product)

    def create_tables(self):
        sep = ',\n\t'
        id_column = ['"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT']
        for table, columns in tables.items():
            query = (f'CREATE TABLE "{table}" '
                     f'(\n\t{sep.join(id_column + columns)}\n)')
            self._connection.execute(query)

    def drop_tables(self):
        for table in tables:
            query = f'DROP TABLE {table}'
            self._connection.execute(query)

    def clear_tables(self):
        for table in tables.keys():
            query = f'DELETE FROM {table}'
            self._connection.execute(query)
