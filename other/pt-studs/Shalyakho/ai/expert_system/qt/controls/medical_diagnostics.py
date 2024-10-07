import sys

from qt.py.medical_diagnostics import Ui_MedicalDiagnosticsWindow
from PySide6 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg


class MedicalDiagnosticsControl(Ui_MedicalDiagnosticsWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.process = qtc.QProcess(self)
        self.process.setProgram(sys.executable)
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)

    def connect_ui(self):
        self.pb_clear.clicked.connect(self.clear_output)
        self.process.readyReadStandardOutput.connect(self.ready_read_standard_output)
        self.process.readyReadStandardError.connect(self.ready_read_standard_error)
        self.le_input.editingFinished.connect(self.editing_finished)

    def run_file(self, url):
        self.process.setArguments([url])
        self.process.start()

    def ready_read_standard_output(self):
        out = self.process.readAllStandardOutput().data().decode()
        self.pte_output.setPlainText(self.pte_output.toPlainText() + out)
        self.pte_output.moveCursor(qtg.QTextCursor.MoveOperation.End)

    def ready_read_standard_error(self):
        err = self.process.readAllStandardError().data().decode()
        self.pte_output.setPlainText(self.pte_output.toPlainText() + '\n' + err)
        self.pte_output.moveCursor(qtg.QTextCursor.MoveOperation.End)

    def editing_finished(self):
        self.process.write(self.le_input.text().encode() + b'\n')
        self.pte_output.setPlainText(self.pte_output.toPlainText() + f'\n>>> {self.le_input.text()}\n')
        self.pte_output.moveCursor(qtg.QTextCursor.MoveOperation.End)
        self.le_input.clear()

    def clear_output(self):
        yes = qtw.QPushButton('Да')
        cancel = qtw.QPushButton('Отмена')
        msgbox = qtw.QMessageBox(qtw.QMessageBox.Icon.Warning, 'Вы уверены?', 'Выведенная информация может быть полезна.')
        msgbox.addButton(yes, qtw.QMessageBox.ButtonRole.YesRole)
        msgbox.addButton(cancel, qtw.QMessageBox.ButtonRole.NoRole)
        msgbox.exec()

        if msgbox.clickedButton() == cancel:
            self.pte_output.setPlainText('')
