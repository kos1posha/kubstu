from PySide6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc

import languages
from qt.py.language_expert import Ui_LanguageExpertWindow


class LanguageExpertControl(Ui_LanguageExpertWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.current_options = []
        self.user_input = []
        self.answers = iter([])
        self.setup_ui()
        self.connect_ui()

    def refresh_answers(self):
        self.answers = iter([
            (languages.paradigms, 'Парадигмы программирования', 250, True),
            (languages.run_types, 'Механизм выполнения кода', 172, False),
            (languages.typing_strengths, 'Типизация', 172, False),
            (languages.typing_statics, 'Типизация', 172, False),
            (languages.use_cases, 'Необходимые вам области', 431, True)
        ])

    def setup_ui(self):
        super().setupUi(self)
        self.l_title.setVisible(False)
        self.setFixedHeight(self.height())

    def connect_ui(self):
        self.pb_choose.clicked.connect(self.start)

    def start(self):
        self.l_title.setVisible(True)
        self.pb_choose.setText('Выбрать')
        self.pb_choose.clicked.disconnect(self.start)
        self.pb_choose.clicked.connect(self.choose)
        self.refresh_answers()
        self.new_question(*next(self.answers))

    def choose(self):
        for cb in self.current_options:
            if cb.isChecked():
                self.user_input.append(cb.text())
        try:
            self.new_question(*next(self.answers))
        except StopIteration:
            self.result()

    def result(self):
        possible_languages = languages.analyze(self.user_input)
        self.user_input.clear()
        self.clear_question_layout()
        self.l_title.setVisible(False)
        l1_text = 'Подходящие языки' if possible_languages else 'Я не нашел подходящего вам языка :('
        l2_text = ', '.join(possible_languages) if possible_languages else 'Похоже, наша база знаний требует доработки...'
        for text, font_args, alignment in zip([l1_text, l2_text], [('Microsoft YaHei UI', 16, 2), ('Microsoft YaHei UI Light', 9)], [qtc.Qt.AlignmentFlag.AlignBottom, qtc.Qt.AlignmentFlag.AlignTop]):
            label = qtw.QLabel(text)
            font = qtg.QFont(*font_args)
            label.setFont(font)
            label.setAlignment(alignment | qtc.Qt.AlignmentFlag.AlignHCenter)
            label.setWordWrap(True)
            self.vl_question.addWidget(label)
        self.setFixedHeight(250)
        self.pb_choose.setText('Перезапуск')
        self.pb_choose.clicked.disconnect(self.choose)
        self.pb_choose.clicked.connect(self.start)

    def new_question(self, options, title, height, multiple_choose):
        self.l_title.setText(title)
        self.clear_question_layout()
        self.current_options.clear()
        for option in options:
            w_option = qtw.QCheckBox(option) if multiple_choose else qtw.QRadioButton(option)
            self.current_options.append(w_option)
            self.vl_question.addWidget(w_option)
        self.setFixedHeight(height)

    def clear_question_layout(self):
        while self.vl_question.count():
            item = self.vl_question.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_question_layout()
