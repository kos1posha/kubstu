from PySide6 import QtCore as qtc, QtWidgets as qtw
from PySide6.QtWidgets import QTreeWidgetItem

import analytics as plots
from db import models as dbm
from qt.controls.dialogs import AddCategoryDialog, AddIncomeDialog, AddOutcomeDialog, AddProductDialog, IncomeOutcomeHistoryDialog
from qt.views.main import Ui_MainWindow


class MainControl(Ui_MainWindow, qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        self.tw_products.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.ResizeToContents)
        for column in [2, 3, 4, 5, 6]:
            self.tw_products.horizontalHeader().setSectionResizeMode(column, qtw.QHeaderView.ResizeMode.Stretch)
        self.update_data()

    def connect_ui(self):
        self.tb_add_category.clicked.connect(self.add_category)
        self.tb_remove_category.clicked.connect(self.remove_category)
        self.tb_add_product.clicked.connect(self.add_product)
        self.tb_remove_product.clicked.connect(self.remove_product)
        self.pb_income.clicked.connect(self.add_income)
        self.pb_outcome.clicked.connect(self.add_outcome)
        self.pb_income_outcome.clicked.connect(self.show_income_outcome_history)
        self.pb_abc_average_price.clicked.connect(plots.average_price_by_category)
        self.pb_abc_product_count.clicked.connect(plots.product_count_by_category)
        self.pb_abc_total_weight.clicked.connect(plots.total_weight_by_category)
        self.pb_abp_product_distribution.clicked.connect(plots.product_price_distribution)

    def update_data(self):
        self.update_products_table()
        self.update_storage_tree()
        self.update_categories_list()
        self.update_metrics()

    def update_products_table(self):
        def center(el):
            widget = qtw.QWidget()
            layout = qtw.QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(el)
            widget.setLayout(layout)
            return widget

        def description_widget(el):
            if len(el) < 11:
                return el
            widget = qtw.QToolButton()
            widget.setMaximumSize(20, 20)
            widget.setText('...')
            widget.clicked.connect(lambda: qtw.QMessageBox(qtw.QMessageBox.Icon.Information, 'Описание', el, qtw.QMessageBox.StandardButton.NoButton).exec())
            return widget

        def complectation_widget(el):
            widget = qtw.QCheckBox()
            widget.setChecked(el == '1')
            widget.setAttribute(qtc.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
            return widget

        self.tw_products.setRowCount(0)
        products = map(list, dbm.products.all())
        for row, product in enumerate(products):
            self.tw_products.insertRow(row)
            for column, data in enumerate(product):
                item = qtw.QTableWidgetItem(str(data))
                item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
                self.tw_products.setItem(row, column, item)
        specials = [(7, description_widget), (8, complectation_widget)]
        for column, spec in specials:
            for row in range(self.tw_products.rowCount()):
                item = self.tw_products.item(row, column)
                spec_value = spec(item.text())
                if isinstance(spec_value, qtw.QWidget):
                    self.tw_products.setCellWidget(row, column, center(spec_value))
                    self.tw_products.item(row, column).setText('')
                else:
                    item.setText(spec_value)
        self.tw_products.resizeColumnsToContents()
        self.tw_products.resizeRowsToContents()

    def update_storage_tree(self):
        self.treew_storage.clear()
        storage_dict = dbm.products.by_categories()
        for category, products in storage_dict.items():
            self.put_category_to_storage_tree(category, products)

    def update_categories_list(self):
        self.lw_categories.clear()
        categories = dbm.categories.all()
        for category in categories:
            item = qtw.QListWidgetItem(str(category[1]))
            self.lw_categories.addItem(item)

    def update_metrics(self):
        products, income, outcome = dbm.products.all(), dbm.income_history.all(), dbm.outcome_history.all()
        self.l_products_count_value.setText(f'{len(products)} ед.')
        self.l_inventory_count_value.setText(f'{sum(int(p[4]) for p in products)} шт.')
        self.l_run_out_value.setText(f'{len([p for p in products if p[4] == "0"])} ед.')
        self.l_total_price_value.setText(f'{sum(int(p[4]) * int(p[6]) for p in products)} ₽')
        self.l_income_last_week_value.setText(f'{sum(int(i[5]) * int(i[6]) for i in income)} ₽')
        self.l_outcome_last_week_value.setText(f'{sum(int(o[5]) * int(o[6]) for o in outcome)} ₽')

    def put_category_to_storage_tree(self, category, products):
        category_item = QTreeWidgetItem()
        category_item.setText(0, f'[{category[0]}] {category[1]}, продуктов: {len(products)}')
        for product in products:
            product_item = QTreeWidgetItem(category_item)
            product_item.setText(0, f'[{product[1]}] {product[2]}, {product[6]} ₽, количество: {product[4]}')
        self.treew_storage.addTopLevelItem(category_item)

    def add_category(self):
        add_dialog = AddCategoryDialog()
        add_dialog.exec()
        self.update_data()

    def remove_category(self):
        category_row = self.lw_categories.currentRow()
        if category_row == -1:
            return self.statusbar.showMessage('Выберите категорию, которую хотите удалить', 2500)
        category = dbm.categories.get(self.lw_categories.currentItem().text())
        if len(dbm.products.of_category(category[1])) > 0:
            return self.statusbar.showMessage('Вы не можете удалить непустую категорию', 2500)

        mb_remove = qtw.QMessageBox(qtw.QMessageBox.Icon.Warning, 'Удалить категорию', 'Вы уверены, что хотите удалить категорию?\nДанное действие необратимо.', qtw.QMessageBox.StandardButton.NoButton)
        mb_remove.setInformativeText(f'Удаляемая категория:\n    {category[1]}')
        pb_yes, pb_no = qtw.QPushButton('Удалить'), qtw.QPushButton('Отмена')
        mb_remove.addButton(pb_yes, qtw.QMessageBox.ButtonRole.ApplyRole)
        mb_remove.addButton(pb_no, qtw.QMessageBox.ButtonRole.RejectRole)
        if mb_remove.exec() == 0: dbm.categories.remove(category[1])
        self.update_data()

    def add_product(self):
        if self.lw_categories.count() == 0:
            return self.statusbar.showMessage('Для создания продукта необходима хотя бы одна категория', 2500)

        add_dialog = AddProductDialog()
        add_dialog.exec()
        self.update_data()

    def remove_product(self):
        product_row = self.tw_products.currentRow()
        if product_row == -1:
            return self.statusbar.showMessage('Выберите продукт, который хотите удалить', 2500)
        product = dbm.products.get(self.tw_products.item(product_row, 1).text())
        if int(product[4]) > 0:
            return self.statusbar.showMessage('Вы не можете удалить продукт, который есть на складе', 2500)

        mb_remove = qtw.QMessageBox(qtw.QMessageBox.Icon.Warning, 'Удалить продукт', 'Вы уверены, что хотите удалить продукт?\nДанное действие необратимо.', qtw.QMessageBox.StandardButton.NoButton)
        mb_remove.setInformativeText(f'Удаляемый продукт:\n    [{product[1]}] {product[2]}, цена {product[5]} ₽')
        pb_yes, pb_no = qtw.QPushButton('Удалить'), qtw.QPushButton('Отмена')
        mb_remove.addButton(pb_yes, qtw.QMessageBox.ButtonRole.ApplyRole)
        mb_remove.addButton(pb_no, qtw.QMessageBox.ButtonRole.RejectRole)
        if mb_remove.exec() == 0: dbm.products.remove(product[1])
        self.update_data()

    def add_income(self):
        if self.tw_products.rowCount() == 0:
            return self.statusbar.showMessage('Для ввоза необходимо зарегистрировать хотя бы один продукт', 2500)
        add_dialog = AddIncomeDialog()
        add_dialog.exec()
        self.update_data()

    def add_outcome(self):
        if self.tw_products.rowCount() == 0:
            return self.statusbar.showMessage('Для вывоза необходимо зарегистрировать хотя бы один продукт', 2500)
        add_dialog = AddOutcomeDialog()
        add_dialog.exec()
        self.update_data()

    def show_income_outcome_history(self):
        history_dialog = IncomeOutcomeHistoryDialog()
        history_dialog.exec()
