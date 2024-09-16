import peewee as pw

db_path = 'db.sqlite3'
db = pw.SqliteDatabase(db_path)


class BaseModel(pw.Model):
    class Meta:
        database = db
