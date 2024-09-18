from db import BorrowRecord, Subscriber, Book
from qt.py.main import Ui_LibArchiveWindow
from PySide6 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg

date_format = '%d.%m.%Y'


class LibArchiveControl(Ui_LibArchiveWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:
        super().setupUi(self)
        self.setup_tables()
        self.update_all()
        self.showMaximized()

    def setup_tables(self) -> None:
        tables = self.tw_borrowers, self.tw_subscribers, self.tw_books
        for table in tables:
            table.horizontalHeader().setSectionResizeMode(
                qtw.QHeaderView.ResizeMode.ResizeToContents)

        def set_cols_resize_mode(t, indexes, resize_mode=qtw.QHeaderView.ResizeMode.Stretch):
            for index in indexes:
                t.horizontalHeader().setSectionResizeMode(index, resize_mode)

        set_cols_resize_mode(self.tw_subscribers, (1,))
        set_cols_resize_mode(self.tw_borrowers, (2,))
        set_cols_resize_mode(self.tw_books, (1, 2))

    def update_all(self) -> None:
        self.update_borrowers()
        self.update_subscribers()
        self.update_books()

    def get_table_item(self, data) -> qtw.QTableWidgetItem:
        str_d = str(data)
        item = qtw.QTableWidgetItem(str_d)
        item.setToolTip(str_d)
        item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        return item

    def update_borrowers(self) -> None:
        borrow_records = BorrowRecord.select()
        self.tw_borrowers.setRowCount(0)
        self.tw_borrowers.setRowCount(borrow_records.count())
        for row, b in enumerate(borrow_records):
            data = (
                b.id, b.subscriber.short_name, b.book.full_name,
                b.borrowing_date.strftime(date_format),
                b.expected_date.strftime(date_format)
            )
            for col, d in enumerate(data):
                item = self.get_table_item(d)
                self.tw_borrowers.setItem(row, col, item)

    def update_subscribers(self) -> None:
        subscribers = Subscriber.select()
        self.tw_subscribers.setRowCount(0)
        self.tw_subscribers.setRowCount(subscribers.count())
        for row, s in enumerate(subscribers):
            data = (s.id, s.full_name, s.rating, s.registration_datetime.strftime(date_format))
            for col, d in enumerate(data):
                item = self.get_table_item(d)
                self.tw_subscribers.setItem(row, col, item)
            qtb = self.get_contacts_qtb_for_subscriber(s)
            self.tw_subscribers.setCellWidget(row, len(data), qtb)

    def get_contacts_qtb_for_subscriber(self, subscriber: Subscriber) -> qtw.QToolButton:
        qtb = qtw.QToolButton()
        qtb.setText('Открыть')
        msgbox = qtw.QMessageBox(
            qtw.QMessageBox.Icon.Information, subscriber.full_name,
            f'Номер телефона: {subscriber.phone_number_f}\n'
            f'Почта: {subscriber.email}\n'
            f'Домашний адрес: {subscriber.home_address}',
            qtw.QMessageBox.StandardButton.NoButton
        )
        qtb.clicked.connect(lambda: msgbox.exec())
        return qtb

    def update_books(self) -> None:
        books = Book.select()
        self.tw_books.setRowCount(0)
        self.tw_books.setRowCount(books.count())
        for row, b in enumerate(books):
            data = (b.id, b.name, b.author, b.edition, b.position)
            for col, d in enumerate(data):
                item = self.get_table_item(d)
                self.tw_books.setItem(row, col, item)
            qtb = self.get_genres_qtb_for_book(b)
            self.tw_books.setCellWidget(row, len(data), qtb)

    def get_genres_qtb_for_book(self, book: Book) -> qtw.QToolButton:
        qtb = qtw.QToolButton()
        qtb.setText('Открыть')
        genres = '\n'.join(g.name for g in book.genres)
        msgbox = qtw.QMessageBox(
            qtw.QMessageBox.Icon.Information, book.name,
            f'Жанры:\n{genres}',
            qtw.QMessageBox.StandardButton.NoButton
        )
        qtb.clicked.connect(lambda: msgbox.exec())
        return qtb
