import sys

from PySide6 import QtWidgets as qtw

from qt import MedicalDiagnosticsControl


def main():
    app = qtw.QApplication(sys.argv + ['-platform', 'windows:darkmode=1'])
    app.setStyle('windows')
    control = MedicalDiagnosticsControl()
    control.run_file('diagnosis_system.py')
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
