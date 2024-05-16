from typing import List, Union

from PySide6 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw


class NumericDelegate(qtw.QStyledItemDelegate):
    def __init__(self, table: qtw.QTableWidget, highlight_empty: bool = False):
        super().__init__()
        self.table = table
        self.highlight_empty = highlight_empty

    def createEditor(self, parent: qtw.QWidget, option: qtw.QStyleOptionViewItem, index: Union[qtc.QModelIndex, qtc.QPersistentModelIndex]) -> qtw.QWidget:
        editor = super().createEditor(parent, option, index)
        if isinstance(editor, qtw.QLineEdit):
            validator = qtg.QIntValidator(bottom=0)
            editor.setValidator(validator)
        return editor

    def initStyleOption(self, option: qtw.QStyleOptionViewItem, index: Union[qtc.QModelIndex, qtc.QPersistentModelIndex]) -> None:
        super().initStyleOption(option, index)
        if (index.column() == self.table.columnCount() - 1) or (index.row() == self.table.rowCount() - 1):
            option.backgroundBrush = qtg.QBrush(qtg.QColor(35, 35, 35, 255))
        if self.highlight_empty:
            item = self.table.item(index.row(), index.column())
            if '-' in item.text():
                if item.text().split('\n')[-1] == '0':
                    option.backgroundBrush = qtg.QBrush(qtg.QColor(160, 20, 20, 160))
                else:
                    option.backgroundBrush = qtg.QBrush(qtg.QColor(60, 160, 60, 120))
            elif item.text() == '0':
                option.backgroundBrush = qtg.QBrush(qtg.QColor(160, 20, 20, 80))


class TransportTableWidget(qtw.QTableWidget):
    def __init__(self, costs: List[List[int]], supply: List[int], demand: List[int], highlight_empty: bool = False):
        super().__init__()
        self.setup_ui(highlight_empty)
        self.put_data(costs, supply, demand)

    def setup_ui(self, highlight_empty: bool) -> None:
        self.setItemDelegate(NumericDelegate(self, highlight_empty))
        self.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)

    def insert_zz_item(self, row: int, column: int) -> None:
        self.setVerticalHeaderItem(row, qtw.QTableWidgetItem('*'))
        self.setHorizontalHeaderItem(column, qtw.QTableWidgetItem('*'))
        item = qtw.QTableWidgetItem()
        item.setFlags(item.flags() ^ ~qtc.Qt.ItemFlag.ItemIsEditable)
        self.setItem(row, column, item)

    def put_data(self, costs: List[List[int]], supply: List[int], demand: List[int]) -> None:
        super().setRowCount(0)
        super().setColumnCount(0)
        rows, columns = len(supply), len(demand)
        self.setRowCount(rows + 1)
        self.setColumnCount(columns + 1)
        for i, s in enumerate(supply):
            self.setItem(i, len(demand), qtw.QTableWidgetItem(str(s)))
            for j, d in enumerate(demand):
                self.setItem(i, j, qtw.QTableWidgetItem(str(costs[i][j])))
        for j, d in enumerate(demand):
            self.setItem(len(supply), j, qtw.QTableWidgetItem(str(d)))
        self.insert_zz_item(rows, columns)

    def insertRow(self, row: int) -> None:
        super().insertRow(row)
        self.setVerticalHeaderItem(row, qtw.QTableWidgetItem(f'П{row + 1}'))
        for column in range(self.columnCount()):
            item = qtw.QTableWidgetItem('1')
            self.setItem(row, column, item)

    def insertColumn(self, column: int) -> None:
        super().insertColumn(column)
        self.setHorizontalHeaderItem(column, qtw.QTableWidgetItem(f'М{column + 1}'))
        for row in range(self.rowCount()):
            item = qtw.QTableWidgetItem('1')
            item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
            self.setItem(row, column, item)

    def setRowCount(self, rows: int) -> None:
        for row in range(self.rowCount(), rows):
            self.insertRow(row)

    def setColumnCount(self, columns: int) -> None:
        for column in range(self.columnCount(), columns):
            self.insertColumn(column)

    def setVerticalHeaderItem(self, row: int, item: qtw.QTableWidgetItem) -> None:
        super().setVerticalHeaderItem(row, item)
        self.verticalHeaderItem(row).setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

    def setHorizontalHeaderItem(self, column: int, item: qtw.QTableWidgetItem) -> None:
        super().setHorizontalHeaderItem(column, item)
        self.horizontalHeaderItem(column).setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

    def setItem(self, row: int, column: int, item: qtw.QTableWidgetItem) -> None:
        item.setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        super().setItem(row, column, item)
