import sys
from PySide6 import QtWidgets as qtw

from qt import LibArchiveControl


def main() -> None:
    app = qtw.QApplication(sys.argv)
    control = LibArchiveControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
