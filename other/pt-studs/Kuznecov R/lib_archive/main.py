import os
import sys
from PySide6 import QtWidgets as qtw

from db.base import db_path
from db import Subscriber, Book, Genre, BorrowRecord
from qt import LibArchiveControl


def init_tables() -> None:
    from db import tables
    os.remove(db_path)
    for table in tables:
        table.create_table()


def populate_database():
    fiction = Genre.create('Художественная литература')
    scientific = Genre.create('Научная литература')
    fantasy = Genre.create('Фэнтези')

    book1 = Book.create('Война и мир', 'Лев Толстой', '1-е', [fiction], 'A1')
    book2 = Book.create('1984', 'Джордж Оруэлл', '1-е', [fiction, scientific], 'A2')
    book3 = Book.create('Гарри Поттер и философский камень', 'Дж.К. Роулинг', '1-е', [fantasy], 'A3')

    subscriber1 = Subscriber.create('Иван', 'Иванов', 'Иванович', 'ivanov@example.com', 'Улица 1, дом 1', '1234567890')
    subscriber2 = Subscriber.create('Мария', 'Петрова', 'Сергеевна', 'petrova@example.com', 'Улица 2, дом 2', '0987654321')

    BorrowRecord.create(subscriber1, book1, 14)
    BorrowRecord.create(subscriber2, book3, 7)


def main() -> None:
    app = qtw.QApplication(sys.argv)
    control = LibArchiveControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    init_tables()
    populate_database()
    main()
