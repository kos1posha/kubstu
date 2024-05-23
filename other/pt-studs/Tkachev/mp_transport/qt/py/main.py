# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_ncost_value = QLineEdit(self.centralwidget)
        self.le_ncost_value.setObjectName(u"le_ncost_value")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_ncost_value.sizePolicy().hasHeightForWidth())
        self.le_ncost_value.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_ncost_value, 1, 1, 1, 1)

        self.l_ncost = QLabel(self.centralwidget)
        self.l_ncost.setObjectName(u"l_ncost")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_ncost.sizePolicy().hasHeightForWidth())
        self.l_ncost.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.l_ncost, 1, 0, 1, 1)

        self.l_costs_table = QLabel(self.centralwidget)
        self.l_costs_table.setObjectName(u"l_costs_table")
        font = QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.l_costs_table.setFont(font)
        self.l_costs_table.setStyleSheet(u"color:rgb(0, 170, 255)")

        self.gridLayout.addWidget(self.l_costs_table, 2, 0, 1, 4)

        self.pb_ncost_cancel = QPushButton(self.centralwidget)
        self.pb_ncost_cancel.setObjectName(u"pb_ncost_cancel")

        self.gridLayout.addWidget(self.pb_ncost_cancel, 1, 3, 1, 1)

        self.tw_costs = QTableWidget(self.centralwidget)
        if (self.tw_costs.columnCount() < 8):
            self.tw_costs.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_costs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_costs.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_costs.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_costs.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_costs.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_costs.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_costs.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_costs.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tw_costs.rowCount() < 10):
            self.tw_costs.setRowCount(10)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_costs.setVerticalHeaderItem(9, __qtablewidgetitem17)
        self.tw_costs.setObjectName(u"tw_costs")
        self.tw_costs.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tw_costs.horizontalHeader().setVisible(False)
        self.tw_costs.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tw_costs, 3, 0, 1, 4)

        self.pb_ocost_cancel = QPushButton(self.centralwidget)
        self.pb_ocost_cancel.setObjectName(u"pb_ocost_cancel")

        self.gridLayout.addWidget(self.pb_ocost_cancel, 0, 3, 1, 1)

        self.pb_ocost_apply = QPushButton(self.centralwidget)
        self.pb_ocost_apply.setObjectName(u"pb_ocost_apply")

        self.gridLayout.addWidget(self.pb_ocost_apply, 0, 2, 1, 1)

        self.pb_ncost_apply = QPushButton(self.centralwidget)
        self.pb_ncost_apply.setObjectName(u"pb_ncost_apply")

        self.gridLayout.addWidget(self.pb_ncost_apply, 1, 2, 1, 1)

        self.le_ocost_value = QLineEdit(self.centralwidget)
        self.le_ocost_value.setObjectName(u"le_ocost_value")
        sizePolicy.setHeightForWidth(self.le_ocost_value.sizePolicy().hasHeightForWidth())
        self.le_ocost_value.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_ocost_value, 0, 1, 1, 1)

        self.l_ocost = QLabel(self.centralwidget)
        self.l_ocost.setObjectName(u"l_ocost")
        sizePolicy1.setHeightForWidth(self.l_ocost.sizePolicy().hasHeightForWidth())
        self.l_ocost.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.l_ocost, 0, 0, 1, 1)

        self.pb_solve = QPushButton(self.centralwidget)
        self.pb_solve.setObjectName(u"pb_solve")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_solve.sizePolicy().hasHeightForWidth())
        self.pb_solve.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pb_solve, 4, 2, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430", None))
        self.le_ncost_value.setText("")
        self.l_ncost.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f (\u0437\u0430 \u044f\u0449\u0438\u043a \u0432 \u043c\u0435\u0441\u044f\u0446)", None))
        self.l_costs_table.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0435\u0439", None))
        self.pb_ncost_cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.pb_ocost_cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.pb_ocost_apply.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.pb_ncost_apply.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.le_ocost_value.setText("")
        self.l_ocost.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u0440\u0430\u0431\u043e\u043a\u0438 (\u0437\u0430 \u044f\u0449\u0438\u043a)", None))
        self.pb_solve.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438\n"
"\u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
    # retranslateUi

