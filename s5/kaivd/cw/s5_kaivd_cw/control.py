import os.path

import clf
import translate as tr

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QIntValidator
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractScrollArea
from ui.view import Ui_ClfWindow
from sklearn.datasets import load_iris, load_breast_cancer, load_digits, load_wine


class ClfControl(Ui_ClfWindow, QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.digits_key = 'Изображения 8х8'
        self.datasets = {'Цветы Ириса': load_iris(), 'Больные раком желудочной железы': load_breast_cancer(), self.digits_key: load_digits(), 'Вина': load_wine()}
        self.criterions = {'Индекс Джини': 'gini', 'Энтропийный критерий': 'entropy'}
        self.splitters = {'Лучшее': 'best', 'Случайное': 'random'}
        self.setupUi(widget)
        self.connectUi()

    def setupUi(self, widget):
        super().setupUi(widget)
        self.widget.setWindowIcon(QIcon(os.path.abspath('ui/clf.ico')))
        self.tw_dataset.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tw_dataset.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tw_dataset.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cb_dataset.addItems(self.datasets.keys())
        self.cb_dataset.setCurrentIndex(-1)
        self.cb_criterion.addItems(self.criterions.keys())
        self.cb_criterion.setCurrentIndex(0)
        self.cb_splitter.addItems(self.splitters.keys())
        self.cb_splitter.setCurrentIndex(0)
        zero_inf_validator = QIntValidator(0, 2147483647)
        for line_edit in [self.le_max_depth, self.le_min_samples_leaf, self.le_min_samples_split, self.le_max_features, self.le_max_leaf_nodes, self.le_random_state]:
            line_edit.setValidator(zero_inf_validator)

    def connectUi(self):
        self.cb_dataset.currentIndexChanged.connect(self.dataset_changed)
        self.tw_dataset.currentItemChanged.connect(self.toggle_pb_show_digits_image)
        self.pb_fit_and_plot_tree.clicked.connect(self.fit_and_plot_tree)
        self.pb_show_digits_image.clicked.connect(self.show_digits_image)
        self.le_max_depth.textChanged.connect(lambda: self.validate_int_field(1, self.le_max_depth))
        self.le_min_samples_leaf.textChanged.connect(lambda: self.validate_int_field(1, self.le_min_samples_leaf))
        self.le_min_samples_split.textChanged.connect(lambda: self.validate_int_field(2, self.le_min_samples_split))
        self.le_max_features.textChanged.connect(lambda: self.validate_int_field(1, self.le_max_features))
        self.le_max_leaf_nodes.textChanged.connect(lambda: self.validate_int_field(2, self.le_max_leaf_nodes))
        self.le_random_state.textChanged.connect(lambda: self.validate_int_field(0, self.le_random_state))

    def fetch_data(self):
        if not (dataset_key := self.cb_dataset.currentText()): return
        dataset = self.datasets[dataset_key]
        criterion = self.criterions[self.cb_criterion.currentText()]
        splitter = self.splitters[self.cb_splitter.currentText()]
        max_depth = int(self.le_max_depth.text()) if self.le_max_depth.text() != '' else None
        min_samples_split = int(self.le_min_samples_split.text()) if self.le_min_samples_split.text() != '' else 2
        min_samples_leaf = int(self.le_min_samples_leaf.text()) if self.le_min_samples_leaf.text() != '' else 1
        max_features = int(self.le_max_features.text()) if self.le_max_features.text() != '' else None
        max_leaf_nodes = int(self.le_max_leaf_nodes.text()) if self.le_max_leaf_nodes.text() != '' else None
        random_state = int(self.le_random_state.text()) if self.le_random_state.text() != '' else None
        return dataset, criterion, splitter, max_depth, min_samples_split, min_samples_leaf, max_features, max_leaf_nodes, random_state

    def fit_and_plot_tree(self):
        dataset, criterion, splitter, max_depth, min_samples_split, min_samples_leaf, max_features, max_leaf_nodes, random_state = self.fetch_data()
        tree, accuracy = clf.fit_clf(
            dataset=dataset,
            criterion=criterion,
            splitter=splitter,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_features=max_features,
            max_leaf_nodes=max_leaf_nodes,
            random_state=random_state
        )
        clf.plot_clf(tree, f'Дерево классификации: {self.cb_dataset.currentText()} (точность: {accuracy})', dataset.feature_names)

    def show_digits_image(self):
        clf.plot_digits(self.tw_dataset.currentRow())

    def dataset_changed(self):
        current = self.datasets[self.cb_dataset.currentText()]
        columns, rows, description = clf.split_dataset(current)
        translate = tr.dictionary.setdefault(self.cb_dataset.currentText(), {column: column.replace('_', ' ').capitalize() for column in columns})
        self.tw_dataset.setColumnCount(len(columns))
        self.tw_dataset.setRowCount(len(rows))
        self.tw_dataset.setHorizontalHeaderLabels([translate[column] for column in columns])
        for row, items in enumerate(rows):
            for column, item in enumerate(items):
                self.tw_dataset.setItem(row, column, QTableWidgetItem(item))
        self.adjust_dataset_table()
        self.toggle_pb_show_digits_image()

    def toggle_pb_show_digits_image(self):
        self.pb_show_digits_image.setEnabled(self.tw_dataset.currentRow() != -1 and self.cb_dataset.currentText() == self.digits_key)

    def validate_int_field(self, bottom, line_edit):
        if line_edit.text() == '': return
        if int(line_edit.text()) < bottom: line_edit.setText(str(bottom))

    def adjust_dataset_table(self):
        self.tw_dataset.setVisible(False)
        self.tw_dataset.resizeColumnsToContents()
        self.tw_dataset.resizeRowsToContents()
        self.tw_dataset.setVisible(True)
