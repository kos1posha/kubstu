import datetime

from PySide6 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw

from db import dt_format, models as dbm, short_dt_format


class IntegerLineEdit(qtw.QLineEdit):
    def __init__(self, parent=None):
        super(IntegerLineEdit, self).__init__(parent)
        self.setValidator(qtg.QIntValidator(bottom=1))
        self.textChanged.connect(self.text_changed)

    def text_changed(self):
        self.setText(self.text().lstrip('0'))


class AddCategoryDialog(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.gl = qtw.QGridLayout()
        self.le_title = qtw.QLineEdit()
        self.pte_description = qtw.QPlainTextEdit()
        self.pb_add = qtw.QPushButton('Добавить')
        self.pb_cancel = qtw.QPushButton('Отмена')
        self.l_status = qtw.QLabel('')
        self.exec_return = None
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        self.setWindowTitle('Добавить категорию')
        self.setLayout(self.gl)
        self.le_title.setPlaceholderText('Название*')
        self.pte_description.setPlaceholderText('Описание')
        self.gl.addWidget(self.le_title, 0, 0, 1, 2)
        self.gl.addWidget(self.pte_description, 1, 0, 1, 2)
        self.gl.addWidget(self.pb_cancel, 2, 0)
        self.gl.addWidget(self.pb_add, 2, 1)
        self.gl.addWidget(self.l_status, 3, 0, 1, 2)

    def connect_ui(self):
        self.le_title.textChanged.connect(lambda: self.le_title.setStyleSheet(''))
        self.pb_add.clicked.connect(self.add)
        self.pb_cancel.clicked.connect(self.close)

    def fetch_data(self):
        return [
            self.le_title.text().strip(),
            self.pte_description.toPlainText().strip()
        ]

    def validate(self, title):
        if not title:
            self.le_title.setStyleSheet('color:red')
            self.l_status.setText('Заполните обязательные поля')
            return False
        if dbm.categories.get(title):
            self.le_title.setStyleSheet('color:red')
            self.l_status.setText('Категория с таким названием уже существует')
            return False
        return True

    def add(self):
        title, description = self.fetch_data()
        if self.validate(title):
            dbm.categories.insert(title, description)
            self.close()


class AddProductDialog(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.gl = qtw.QGridLayout()
        self.cmb_categories = qtw.QComboBox()
        self.le_code = qtw.QLineEdit()
        self.le_title = qtw.QLineEdit()
        self.le_weight = IntegerLineEdit()
        self.le_price = IntegerLineEdit()
        self.pte_description = qtw.QPlainTextEdit()
        self.pb_add = qtw.QPushButton('Добавить')
        self.pb_cancel = qtw.QPushButton('Отмена')
        self.l_status = qtw.QLabel('')
        self.exec_return = None
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        self.setWindowTitle('Добавить продукт')
        self.setLayout(self.gl)
        self.le_code.setPlaceholderText('Код*')
        self.le_title.setPlaceholderText('Название*')
        self.cmb_categories.addItems([c[1] for c in dbm.categories.all()])
        self.le_weight.setPlaceholderText('Вес*')
        self.le_price.setPlaceholderText('Цена*')
        self.pte_description.setPlaceholderText('Описание')
        self.gl.addWidget(self.cmb_categories, 0, 0, 1, 2)
        self.gl.addWidget(self.le_code, 1, 0, 1, 2)
        self.gl.addWidget(self.le_title, 2, 0, 1, 2)
        self.gl.addWidget(self.le_weight, 3, 0)
        self.gl.addWidget(self.le_price, 3, 1)
        self.gl.addWidget(self.pte_description, 4, 0, 1, 2)
        self.gl.addWidget(self.pb_cancel, 6, 0)
        self.gl.addWidget(self.pb_add, 6, 1)
        self.gl.addWidget(self.l_status, 7, 0, 1, 2)

    def connect_ui(self):
        self.le_code.textChanged.connect(lambda: self.le_code.setStyleSheet(''))
        self.le_title.textChanged.connect(lambda: self.le_title.setStyleSheet(''))
        self.le_weight.textChanged.connect(lambda: self.le_weight.setStyleSheet(''))
        self.le_price.textChanged.connect(lambda: self.le_price.setStyleSheet(''))
        self.pb_add.clicked.connect(self.add)
        self.pb_cancel.clicked.connect(self.close)

    def fetch_data(self):
        return [
            self.le_code.text().strip(),
            self.le_title.text().strip(),
            self.cmb_categories.currentText(),
            self.le_weight.text(),
            self.le_price.text(),
            self.pte_description.toPlainText().strip(),
        ]

    def validate(self, code, title, weight, price):
        if not all([code, title, weight, price]):
            for le, text in [(self.le_code, code), (self.le_title, title), (self.le_weight, weight), (self.le_price, price)]:
                if not text: le.setStyleSheet('color:red')
            self.l_status.setText('Заполните обязательные поля')
            return False
        if dbm.products.get(code):
            self.le_code.setStyleSheet('color:red')
            self.l_status.setText('Продукт с таким кодом уже существует')
            return False
        return True

    def add(self):
        code, title, category, weight, price, description = self.fetch_data()
        if self.validate(code, title, weight, price):
            dbm.products.insert(code, title, category, 0, weight, price, description)
            self.close()


class Add__comeDialog(qtw.QDialog):
    def __init__(self, dbm, window_title):
        super().__init__()
        self.dbm = dbm
        self.window_title = window_title
        self.gl = qtw.QGridLayout()
        self.cmb_products = qtw.QComboBox()
        self.le_count = IntegerLineEdit()
        self.de_datetime = qtw.QDateTimeEdit()
        self.pb_add = qtw.QPushButton('Подтвердить')
        self.pb_cancel = qtw.QPushButton('Отмена')
        self.l_status = qtw.QLabel('')
        self.exec_return = None
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        self.setWindowTitle(self.window_title)
        self.setLayout(self.gl)
        self.cmb_products.addItems([f'[{p[1]}] {p[2]}, количество: {p[4]}' for p in dbm.products.all()])
        self.le_count.setPlaceholderText('Количество*')
        self.de_datetime.setDateTime(qtc.QDateTime.currentDateTime())
        self.de_datetime.setCalendarPopup(True)
        self.gl.addWidget(self.cmb_products, 0, 0, 1, 2)
        self.gl.addWidget(self.le_count, 1, 0, 1, 2)
        self.gl.addWidget(self.de_datetime, 2, 0, 1, 2)
        self.gl.addWidget(self.pb_cancel, 3, 0)
        self.gl.addWidget(self.pb_add, 3, 1)
        self.gl.addWidget(self.l_status, 4, 0, 1, 2)

    def connect_ui(self):
        self.le_count.textChanged.connect(lambda: self.le_count.setStyleSheet(''))
        self.pb_add.clicked.connect(self.add)
        self.pb_cancel.clicked.connect(self.close)

    def fetch_data(self):
        return [
            self.cmb_products.currentText().split()[0].strip('[]'),
            self.le_count.text().strip(),
            self.de_datetime.dateTime().toPython().strftime(dt_format),
        ]

    def validate(self, count):
        if not count:
            self.le_count.setStyleSheet('color:red')
            self.l_status.setText('Заполните обязательные поля')
            return False
        return True

    def old_count(self):
        return int(self.cmb_products.currentText().split('количество:')[1])

    def calc_new_count(self, count):
        raise NotImplementedError()

    def add(self):
        product_code, count, dt = self.fetch_data()
        if self.validate(count):
            dbm.products.update_count(product_code, self.calc_new_count(count))
            self.dbm.insert(product_code, count, dt)
            self.close()


class AddIncomeDialog(Add__comeDialog):
    def __init__(self):
        super().__init__(dbm.income_history, 'Ввоз продукции')

    def calc_new_count(self, count):
        return self.old_count() + int(count)


class AddOutcomeDialog(Add__comeDialog):
    def __init__(self):
        super().__init__(dbm.outcome_history, 'Вывоз продукции')

    def calc_new_count(self, count):
        return self.old_count() - int(count)

    def validate(self, count):
        if not super().validate(count):
            return False
        if self.old_count() < int(count):
            self.le_count.setStyleSheet('color:red')
            self.l_status.setText('Вывоз не может превышать количество продукции на складе')
            return False
        return True


class IncomeOutcomeHistoryDialog(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.vl = qtw.QVBoxLayout()
        self.tw_comes = qtw.QTableWidget()
        self.setup_ui()
        self.put_data()

    def setup_ui(self):
        self.setWindowTitle('Ввоз и вывоз')
        self.resize(600, 400)
        self.setLayout(self.vl)
        self.tw_comes.setColumnCount(6)
        self.tw_comes.setHorizontalHeaderLabels(['Тип', 'Название продукта', 'Категория', 'Цена (₽)', 'Количество', 'Общая цена (₽)'])
        self.tw_comes.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.ResizeToContents)
        for column in [1, 2]:
            self.tw_comes.horizontalHeader().setSectionResizeMode(column, qtw.QHeaderView.ResizeMode.Stretch)
        self.tw_comes.setEditTriggers(qtw.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.vl.addWidget(self.tw_comes)

    def put_data(self):
        def dt(string):
            dt = datetime.datetime.strptime(string, dt_format)
            return (dt.strftime(short_dt_format),)

        incomes, outcomes = dbm.income_history.all(), dbm.outcome_history.all()
        incomes, outcomes = list(map(lambda i: dt(i[1]) + ('Ввоз',) + i[3:] + (int(i[5]) * int(i[6]),), incomes)), list(map(lambda o: dt(o[1]) + ('Вывоз',) + o[3:] + (int(o[5]) * int(o[6]),), outcomes)),
        comes = sorted(incomes + outcomes, key=lambda c: c[-1])
        for row, come in enumerate(comes):
            self.tw_comes.insertRow(row)
            self.tw_comes.setVerticalHeaderItem(row, qtw.QTableWidgetItem(come[0]))
            for column, data in enumerate(come[1:]):
                item = qtw.QTableWidgetItem(str(data))
                item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
                self.tw_comes.setItem(row, column, item)
