from typing import Optional

import numpy as np
from PySide6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc

from neural.perceptron import Perceptron, Neuron
from qt.py.main import Ui_PerceptronWindow


class PreviewLabel(qtw.QLabel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.letter_pixmap: qtg.QPixmap = None
        self.setFixedSize(300, 300)
        self.setFrameShape(qtw.QFrame.Shape.Box)
        self.setFrameShadow(qtw.QFrame.Shadow.Sunken)
        self.setScaledContents(True)
        self.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

    def get_signals(self) -> np.ndarray:
        if self.letter_pixmap is None:
            return np.array([])

        img = self.letter_pixmap.toImage()
        signals = []
        for y in range(30):
            for x in range(30):
                color = img.pixelColor(x, y)
                signals.append(0 if color.toTuple() == (255, 255, 255, 255) else 1)
        return np.array(signals)

    def mouseDoubleClickEvent(self, event: qtg.QMouseEvent) -> None:
        file_name, _ = qtw.QFileDialog.getOpenFileName(self, 'Выберите изображение', 'letters/', 'Images (*.png *.jpg *.jpeg *.bmp *.gif)')
        if not file_name:
            return

        self.letter_pixmap = qtg.QPixmap(file_name)
        if self.letter_pixmap.width() != 30:
            self.letter_pixmap.scaledToWidth(30, qtc.Qt.TransformationMode.FastTransformation)
        if self.letter_pixmap.height() != 30:
            self.letter_pixmap.scaledToHeight(30, qtc.Qt.TransformationMode.FastTransformation)
        self.setPixmap(self.letter_pixmap)
        self.setText('')


class PerceptronControl(Ui_PerceptronWindow, qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.perceptron = Perceptron([Neuron(letter, 0.2) for letter in self.alphabet])
        self.perceptron.randomize()
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self) -> None:
        super().setupUi(self)
        del self.l_preview
        self.l_preview = PreviewLabel('Нажмите дважды, чтобы загрузить изображение')
        self.gl_main.addWidget(self.l_preview, 1, 1, 1, 1)
        self.setFixedSize(self.sizeHint().width(), self.sizeHint().height())

        letter_validator = qtg.QRegularExpressionValidator('[а-яё ]+')
        self.le_letter.setValidator(letter_validator)

        self.tw_neurons.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.tw_neurons.setRowCount(len(self.perceptron.neurons))
        for row, neuron in enumerate(self.perceptron.neurons):
            for i, s in [(0, neuron.letter), (2, '-')]:
                item = qtw.QTableWidgetItem(s)
                item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
                self.tw_neurons.setItem(row, i, item)
            pb = qtw.QToolButton()
            pb.setText('👁')
            pb.setStyleSheet('background-color:transparent;border:none')
            pb.clicked.connect(neuron.visualize)
            self.tw_neurons.setCellWidget(row, 1, pb)

        self.l_neurons.setFocus()

    def connect_ui(self) -> None:
        self.pb_train_one.clicked.connect(self.train_one)
        self.pb_train_all.clicked.connect(self.train_all)
        self.pb_predict.clicked.connect(self.predict)

    def validate_letter(self) -> bool:
        if self.le_letter.text() == '':
            self.l_letter.setStyleSheet('color:rgba(255,0,0,214)')
            self.le_letter.setStyleSheet('background-color:rgba(255,0,0,31)')
            return False
        return True

    def validate_preview(self) -> bool:
        if self.l_preview.letter_pixmap is None:
            qtw.QMessageBox.warning(self, 'Ошибка', 'Не выбрано изображение буквы')
            return False
        return True

    def validate_inputs(self) -> Optional[tuple[str, float, int]]:
        if not self.validate_letter() and self.validate_preview():
            return None

        self.l_letter.setStyleSheet('')
        self.le_letter.setStyleSheet('')
        return self.le_letter.text(), self.dsb_alpha.value(), self.sb_epochs.value()

    def _train(self, entity: Neuron | Perceptron) -> None:
        validated_inputs = self.validate_inputs()
        if validated_inputs is None:
            return
        letter, alpha, epochs = validated_inputs

        signals = self.l_preview.get_signals()
        try:
            entity.train(signals, letter, alpha, epochs)
        except:
            qtw.QMessageBox.warning(self, 'Ошибка', 'Во время обучения произошла ошибка...')
        else:
            qtw.QMessageBox.information(self, 'Успешно', 'Обучение прошло успешно')

    def train_one(self) -> None:
        n_i = self.tw_neurons.currentRow()
        if n_i == -1:
            qtw.QMessageBox.warning(self, 'Ошибка', 'Выберите нейрон из списка')
            return

        self._train(self.perceptron.neurons[n_i])

    def train_all(self) -> None:
        self._train(self.perceptron)

    def predict(self) -> None:
        if not self.validate_preview():
            return

        for i, prediction in enumerate(self.perceptron.predict(self.l_preview.get_signals())):
            self.tw_neurons.item(i, 2).setText(str(prediction))
