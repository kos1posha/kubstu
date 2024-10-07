import os.path
import re

from PySide6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc

import nn
from image_helper import ImageHelper
from qt.py.perceptron import Ui_PerceptronWindow


class PerceptronControl(Ui_PerceptronWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.alpha = 0.1
        self.perceptron = nn.Perceptron([nn.Neuron(letter, 0.21) for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
        self.perceptron.randomize()
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.le_neurons.setValidator(qtg.QRegularExpressionValidator(qtc.QRegularExpression(r'^([A-Z](\s|$))*$'), self.le_neurons))
        self.tw_train_data.horizontalHeader().setSectionResizeMode(0, qtw.QHeaderView.ResizeMode.ResizeToContents)

    def connect_ui(self):
        self.pb_choose_file.clicked.connect(self.file_dialog_for_predict)
        self.pb_add_td.clicked.connect(self.file_dialog_for_train)
        self.pb_remove_td.clicked.connect(self.remove_selected_td)
        self.pb_train_selectively.clicked.connect(self.train_selectively)
        self.pb_train_all.clicked.connect(self.train_all)
        self.pb_predict.clicked.connect(self.predict)

    def file_dialog_for_predict(self):
        file_path, _ = qtw.QFileDialog.getOpenFileName(self, 'Выберите файл PNG', '', 'PNG файл (*.png)')
        if file_path:
            if not self.check_image_size(file_path):
                return
            self.le_file_path.setText('📂 ' + file_path)
            self.le_file_path.setToolTip(file_path)
            self.le_file_path.setCursorPosition(0)

    def file_dialog_for_train(self):
        file_paths, _ = qtw.QFileDialog.getOpenFileNames(self, 'Выберите файлы PNG', '', 'PNG файлы (*.png)')
        letter_validator = qtg.QRegularExpressionValidator(qtc.QRegularExpression(r'^[A-Z]+$'))
        for row, file_path in enumerate(file_paths, start=self.tw_train_data.rowCount()):
            self.tw_train_data.insertRow(row)
            if self.check_image_size(file_path, False):
                dirname = os.path.basename(os.path.dirname(file_path))
                le_letter = qtw.QLineEdit(dirname if bool(re.fullmatch(r'[A-Z]', dirname)) else '')
                le_letter.setStyleSheet('border:none;background:transparent')
                le_letter.setMaxLength(1)
                le_letter.setValidator(letter_validator)
                le_letter.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
                path_item = qtw.QTableWidgetItem(file_path)
                path_item.setFlags(path_item.flags() & ~qtc.Qt.ItemFlag.ItemIsEditable)
                path_item.setToolTip(file_path)
                self.tw_train_data.setCellWidget(row, 0, le_letter)
                self.tw_train_data.setItem(row, 1, path_item)

    def remove_selected_td(self):
        selected_rows = self.tw_train_data.selectionModel().selectedRows()
        for row in reversed(selected_rows):
            self.tw_train_data.removeRow(row.row())

    def check_image_size(self, file_path, msg=True):
        pixmap = qtg.QPixmap(file_path)
        if pixmap.size() != qtc.QSize(30, 30):
            if msg:
                qtw.QMessageBox.critical(self, 'Ошибка', f'Файл {file_path} должен быть размером 30x30 пикселей.')
            return False
        return True

    def _train(self, letters):
        selected_rows = self.tw_train_data.selectionModel().selectedRows()
        for row in selected_rows:
            letter = self.tw_train_data.cellWidget(row.row(), 0).text()
            if not letter:
                continue
            file_path = self.tw_train_data.item(row.row(), 1).text()
            signals = ImageHelper.image_to_array(file_path)
            self.perceptron.train(signals, letter, self.alpha, 20, letters)

        img = ImageHelper.perceptron_to_image(self.perceptron)
        img.save('perceptron.png')

    def train_selectively(self):
        letters = set(self.le_neurons.text().replace(' ', ''))
        self._train(letters)
        qtw.QMessageBox.information(self, 'Успешно', 'Следующие нейроны были успешно обучены:\n' +
                                    '\n'.join([str(n) for n in self.perceptron.neurons if n.letter in letters]))

    def train_all(self):
        self._train(set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        qtw.QMessageBox.information(self, 'Успешно', 'Следующие нейроны были успешно обучены:\n' + '\n'.join([str(n) for n in self.perceptron.neurons]))

    def predict(self):
        if '📁' in self.le_file_path.text():
            qtw.QMessageBox.warning(self, 'Внимание', 'Вы не выбрали файл')
            return

        file_path = self.le_file_path.text()[2:]
        signals = ImageHelper.image_to_array(file_path)
        result = self.perceptron.predict(signals, 0.17)

        output = [f'<span style="color:green">{file_path}</span>']
        for n, r in zip(self.perceptron.neurons, result):
            if self.cb_only_1.isChecked():
                if r == 1:
                    output.append(f'{n} -> <span style="color:blue">1</span>')
            else:
                color = 'blue' if r else 'red'
                output.append(f'{n} -> <span style="color:{color}">{r}</span>')
        self.te_perceptron_output.setHtml('<br>'.join(output))
        self.te_perceptron_output.moveCursor(qtg.QTextCursor.MoveOperation.End)
