import sys

from PySide6 import QtWidgets as qtw

from db.initializer import DBInitializer
from qt.controls.main import MainControl


def db_reinit(clear=False):
    initializer = DBInitializer()
    initializer.reinit()
    if clear:
        initializer.clear_tables()


def main():
    app = qtw.QApplication(sys.argv)
    app.setStyle('windows')
    control = MainControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    db_reinit()
    main()
