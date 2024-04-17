# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file ''
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_StockBuyLpSolverWindow(object):
    def setupUi(self, StockBuyLpSolverWindow):
        if not StockBuyLpSolverWindow.objectName():
            StockBuyLpSolverWindow.setObjectName(u"StockBuyLpSolverWindow")
        StockBuyLpSolverWindow.resize(714, 360)
        StockBuyLpSolverWindow.setMinimumSize(QSize(714, 0))
        StockBuyLpSolverWindow.setMaximumSize(QSize(860, 16777215))
        self.gl_main = QGridLayout(StockBuyLpSolverWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.l_constraints = QLabel(StockBuyLpSolverWindow)
        self.l_constraints.setObjectName(u"l_constraints")

        self.gl_main.addWidget(self.l_constraints, 2, 0, 1, 1)

        self.pb_add_new_constraint = QPushButton(StockBuyLpSolverWindow)
        self.pb_add_new_constraint.setObjectName(u"pb_add_new_constraint")
        self.pb_add_new_constraint.setEnabled(False)

        self.gl_main.addWidget(self.pb_add_new_constraint, 3, 1, 1, 1)

        self.l_tasks_helptext = QLabel(StockBuyLpSolverWindow)
        self.l_tasks_helptext.setObjectName(u"l_tasks_helptext")
        font = QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.l_tasks_helptext.setFont(font)
        self.l_tasks_helptext.setStyleSheet(u"color:gray")
        self.l_tasks_helptext.setAlignment(Qt.AlignCenter)
        self.l_tasks_helptext.setWordWrap(True)

        self.gl_main.addWidget(self.l_tasks_helptext, 9, 1, 1, 2)

        self.l_obj_func = QLabel(StockBuyLpSolverWindow)
        self.l_obj_func.setObjectName(u"l_obj_func")

        self.gl_main.addWidget(self.l_obj_func, 0, 0, 1, 1)

        self.l_variables_helptext = QLabel(StockBuyLpSolverWindow)
        self.l_variables_helptext.setObjectName(u"l_variables_helptext")
        self.l_variables_helptext.setFont(font)
        self.l_variables_helptext.setStyleSheet(u"color:gray")
        self.l_variables_helptext.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.l_variables_helptext, 15, 0, 1, 3)

        self.le_obj_func = QLineEdit(StockBuyLpSolverWindow)
        self.le_obj_func.setObjectName(u"le_obj_func")

        self.gl_main.addWidget(self.le_obj_func, 1, 0, 1, 1)

        self.pb_clear = QPushButton(StockBuyLpSolverWindow)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setMinimumSize(QSize(140, 0))

        self.gl_main.addWidget(self.pb_clear, 12, 1, 1, 2)

        self.cmb_search = QComboBox(StockBuyLpSolverWindow)
        self.cmb_search.addItem("")
        self.cmb_search.addItem("")
        self.cmb_search.setObjectName(u"cmb_search")

        self.gl_main.addWidget(self.cmb_search, 1, 1, 1, 2)

        self.w_tasks = QWidget(StockBuyLpSolverWindow)
        self.w_tasks.setObjectName(u"w_tasks")
        self.gl_tasks = QGridLayout(self.w_tasks)
        self.gl_tasks.setObjectName(u"gl_tasks")
        self.gl_tasks.setContentsMargins(0, 0, 0, 0)
        self.pb_task6 = QPushButton(self.w_tasks)
        self.pb_task6.setObjectName(u"pb_task6")

        self.gl_tasks.addWidget(self.pb_task6, 2, 0, 1, 1)

        self.pb_task19 = QPushButton(self.w_tasks)
        self.pb_task19.setObjectName(u"pb_task19")

        self.gl_tasks.addWidget(self.pb_task19, 2, 1, 1, 1)

        self.pb_task3 = QPushButton(self.w_tasks)
        self.pb_task3.setObjectName(u"pb_task3")

        self.gl_tasks.addWidget(self.pb_task3, 1, 1, 1, 1)

        self.pb_task1 = QPushButton(self.w_tasks)
        self.pb_task1.setObjectName(u"pb_task1")

        self.gl_tasks.addWidget(self.pb_task1, 1, 0, 1, 1)


        self.gl_main.addWidget(self.w_tasks, 8, 1, 1, 2)

        self.pb_delete_constraint = QPushButton(StockBuyLpSolverWindow)
        self.pb_delete_constraint.setObjectName(u"pb_delete_constraint")
        self.pb_delete_constraint.setEnabled(False)

        self.gl_main.addWidget(self.pb_delete_constraint, 3, 2, 1, 1)

        self.pb_solve = QPushButton(StockBuyLpSolverWindow)
        self.pb_solve.setObjectName(u"pb_solve")
        self.pb_solve.setMinimumSize(QSize(140, 0))

        self.gl_main.addWidget(self.pb_solve, 14, 1, 1, 2)

        self.lw_constraints = QListWidget(StockBuyLpSolverWindow)
        QListWidgetItem(self.lw_constraints)
        QListWidgetItem(self.lw_constraints)
        self.lw_constraints.setObjectName(u"lw_constraints")

        self.gl_main.addWidget(self.lw_constraints, 5, 0, 10, 1)

        self.le_new_constraint = QLineEdit(StockBuyLpSolverWindow)
        self.le_new_constraint.setObjectName(u"le_new_constraint")

        self.gl_main.addWidget(self.le_new_constraint, 3, 0, 1, 1)

        self.l_search = QLabel(StockBuyLpSolverWindow)
        self.l_search.setObjectName(u"l_search")

        self.gl_main.addWidget(self.l_search, 0, 1, 1, 2)

        self.l_tasks = QLabel(StockBuyLpSolverWindow)
        self.l_tasks.setObjectName(u"l_tasks")

        self.gl_main.addWidget(self.l_tasks, 7, 1, 1, 2)

        self.vs_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gl_main.addItem(self.vs_1, 11, 1, 1, 2)


        self.retranslateUi(StockBuyLpSolverWindow)

        QMetaObject.connectSlotsByName(StockBuyLpSolverWindow)
    # setupUi

    def retranslateUi(self, StockBuyLpSolverWindow):
        StockBuyLpSolverWindow.setWindowTitle(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u0421\u0438\u043c\u043f\u043b\u0435\u043a\u0441", None))
        self.l_constraints.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f", None))
        self.pb_add_new_constraint.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.l_tasks_helptext.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u041f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u0432\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0443\u0441\u043b\u043e\u0432\u0438\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.l_obj_func.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.l_variables_helptext.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u0414\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0446\u0435\u043b\u0435\u0432\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b \u0441\u0438\u043c\u0432\u043e\u043b\u044b [x, x0, ..., x9], [y, y0, ..., y9] \u0438 [A, B]", None))
        self.le_obj_func.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"A + B", None))
        self.le_obj_func.setPlaceholderText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.pb_clear.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.cmb_search.setItemText(0, QCoreApplication.translate("StockBuyLpSolverWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c", None))
        self.cmb_search.setItemText(1, QCoreApplication.translate("StockBuyLpSolverWindow", u"\u041c\u0438\u043d\u0438\u043c\u0443\u043c", None))

        self.pb_task6.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"6", None))
        self.pb_task19.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"19", None))
        self.pb_task3.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"3", None))
        self.pb_task1.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"1", None))
        self.pb_delete_constraint.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pb_solve.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))

        __sortingEnabled = self.lw_constraints.isSortingEnabled()
        self.lw_constraints.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_constraints.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"27*A + 23*B <= 930", None));
        ___qlistwidgetitem1 = self.lw_constraints.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"A - B >= 10", None));
        self.lw_constraints.setSortingEnabled(__sortingEnabled)

        self.le_new_constraint.setPlaceholderText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435", None))
        self.l_search.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.l_tasks.setText(QCoreApplication.translate("StockBuyLpSolverWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
    # retranslateUi

