# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parts_maximize.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_PartsMaximizeWindow(object):
    def setupUi(self, PartsMaximizeWindow):
        if not PartsMaximizeWindow.objectName():
            PartsMaximizeWindow.setObjectName(u"PartsMaximizeWindow")
        PartsMaximizeWindow.resize(560, 450)
        PartsMaximizeWindow.setMinimumSize(QSize(560, 450))
        PartsMaximizeWindow.setMaximumSize(QSize(560, 450))
        self.gl_main = QGridLayout(PartsMaximizeWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setContentsMargins(0, 0, 0, 0)
        self.tabw_steps = QTabWidget(PartsMaximizeWindow)
        self.tabw_steps.setObjectName(u"tabw_steps")
        self.tabw_steps.setTabPosition(QTabWidget.TabPosition.North)
        self.tabw_steps.setDocumentMode(True)
        self.tab_task = QWidget()
        self.tab_task.setObjectName(u"tab_task")
        self.gl_task = QGridLayout(self.tab_task)
        self.gl_task.setObjectName(u"gl_task")
        self.tw_task = QTableWidget(self.tab_task)
        if (self.tw_task.columnCount() < 6):
            self.tw_task.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_task.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_task.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_task.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_task.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_task.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_task.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tw_task.rowCount() < 7):
            self.tw_task.setRowCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_task.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_task.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_task.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_task.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_task.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_task.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_task.setVerticalHeaderItem(6, __qtablewidgetitem12)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font);
        __qtablewidgetitem13.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font);
        __qtablewidgetitem14.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(0, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_task.setItem(0, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font);
        __qtablewidgetitem16.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(0, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font);
        __qtablewidgetitem17.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(1, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font);
        __qtablewidgetitem18.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(2, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font);
        __qtablewidgetitem19.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(2, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font);
        __qtablewidgetitem20.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(2, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font);
        __qtablewidgetitem21.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(2, 4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font);
        __qtablewidgetitem22.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(2, 5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font);
        __qtablewidgetitem23.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(3, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFont(font);
        __qtablewidgetitem24.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(4, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(4, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(4, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(4, 3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(4, 4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(4, 5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFont(font);
        __qtablewidgetitem30.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(5, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(5, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(5, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(5, 3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(5, 4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(5, 5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font);
        __qtablewidgetitem36.setFlags(Qt.ItemIsEnabled);
        self.tw_task.setItem(6, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(6, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(6, 2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(6, 3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(6, 4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tw_task.setItem(6, 5, __qtablewidgetitem41)
        self.tw_task.setObjectName(u"tw_task")
        self.tw_task.horizontalHeader().setVisible(False)
        self.tw_task.verticalHeader().setVisible(False)

        self.gl_task.addWidget(self.tw_task, 2, 0, 1, 1)

        self.l_task_1 = QLabel(self.tab_task)
        self.l_task_1.setObjectName(u"l_task_1")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        self.l_task_1.setFont(font1)
        self.l_task_1.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_task_1.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_task_1.setWordWrap(True)
        self.l_task_1.setMargin(6)

        self.gl_task.addWidget(self.l_task_1, 1, 0, 1, 1)

        self.l_variant = QLabel(self.tab_task)
        self.l_variant.setObjectName(u"l_variant")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(True)
        self.l_variant.setFont(font2)
        self.l_variant.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gl_task.addWidget(self.l_variant, 0, 0, 1, 1)

        self.l_task_2 = QLabel(self.tab_task)
        self.l_task_2.setObjectName(u"l_task_2")
        self.l_task_2.setFont(font1)
        self.l_task_2.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_task_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_task_2.setWordWrap(True)
        self.l_task_2.setMargin(6)

        self.gl_task.addWidget(self.l_task_2, 3, 0, 1, 1)

        self.tabw_steps.addTab(self.tab_task, "")
        self.tab_obj_func = QWidget()
        self.tab_obj_func.setObjectName(u"tab_obj_func")
        self.gridLayout = QGridLayout(self.tab_obj_func)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_obj_func = QLabel(self.tab_obj_func)
        self.l_obj_func.setObjectName(u"l_obj_func")
        self.l_obj_func.setFont(font2)
        self.l_obj_func.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.l_obj_func, 0, 0, 1, 1)

        self.tabw_steps.addTab(self.tab_obj_func, "")
        self.tab_constraints = QWidget()
        self.tab_constraints.setObjectName(u"tab_constraints")
        self.gridLayout_2 = QGridLayout(self.tab_constraints)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.l_constraints = QLabel(self.tab_constraints)
        self.l_constraints.setObjectName(u"l_constraints")
        self.l_constraints.setFont(font2)
        self.l_constraints.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.l_constraints, 0, 0, 1, 1)

        self.tabw_steps.addTab(self.tab_constraints, "")
        self.tab_solution = QWidget()
        self.tab_solution.setObjectName(u"tab_solution")
        self.gridLayout_3 = QGridLayout(self.tab_solution)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.l_lp_given = QLabel(self.tab_solution)
        self.l_lp_given.setObjectName(u"l_lp_given")
        self.l_lp_given.setFont(font2)
        self.l_lp_given.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.l_lp_given, 0, 0, 1, 1)

        self.tabw_steps.addTab(self.tab_solution, "")

        self.gl_main.addWidget(self.tabw_steps, 0, 0, 1, 1)


        self.retranslateUi(PartsMaximizeWindow)

        self.tabw_steps.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(PartsMaximizeWindow)
    # setupUi

    def retranslateUi(self, PartsMaximizeWindow):
        PartsMaximizeWindow.setWindowTitle(QCoreApplication.translate("PartsMaximizeWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f \u0447\u0438\u0441\u043b\u0430 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432 \u0434\u0435\u0442\u0430\u043b\u0435\u0439", None))

        __sortingEnabled = self.tw_task.isSortingEnabled()
        self.tw_task.setSortingEnabled(False)
        ___qtablewidgetitem = self.tw_task.item(0, 0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0412\u0438\u0434 \u0434\u0435\u0442\u0430\u043b\u0438", None));
        ___qtablewidgetitem1 = self.tw_task.item(0, 1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041b\u0438\u0441\u0442\u044b \u0440\u0430\u0437\u043c\u0435\u0440\u0430 1", None));
        ___qtablewidgetitem2 = self.tw_task.item(0, 4)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041b\u0438\u0441\u0442 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 2", None));
        ___qtablewidgetitem3 = self.tw_task.item(1, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431\u044b \u0440\u0430\u0441\u043a\u0440\u043e\u044f", None));
        ___qtablewidgetitem4 = self.tw_task.item(2, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PartsMaximizeWindow", u"1", None));
        ___qtablewidgetitem5 = self.tw_task.item(2, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PartsMaximizeWindow", u"2", None));
        ___qtablewidgetitem6 = self.tw_task.item(2, 3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PartsMaximizeWindow", u"3", None));
        ___qtablewidgetitem7 = self.tw_task.item(2, 4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PartsMaximizeWindow", u"4", None));
        ___qtablewidgetitem8 = self.tw_task.item(2, 5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PartsMaximizeWindow", u"5", None));
        ___qtablewidgetitem9 = self.tw_task.item(3, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0442\u0430\u043b\u0435\u0439", None));
        ___qtablewidgetitem10 = self.tw_task.item(4, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PartsMaximizeWindow", u"1", None));
        ___qtablewidgetitem11 = self.tw_task.item(4, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PartsMaximizeWindow", u"0", None));
        ___qtablewidgetitem12 = self.tw_task.item(4, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PartsMaximizeWindow", u"2", None));
        ___qtablewidgetitem13 = self.tw_task.item(4, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PartsMaximizeWindow", u"9", None));
        ___qtablewidgetitem14 = self.tw_task.item(4, 4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("PartsMaximizeWindow", u"6", None));
        ___qtablewidgetitem15 = self.tw_task.item(4, 5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("PartsMaximizeWindow", u"5", None));
        ___qtablewidgetitem16 = self.tw_task.item(5, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("PartsMaximizeWindow", u"2", None));
        ___qtablewidgetitem17 = self.tw_task.item(5, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("PartsMaximizeWindow", u"4", None));
        ___qtablewidgetitem18 = self.tw_task.item(5, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("PartsMaximizeWindow", u"3", None));
        ___qtablewidgetitem19 = self.tw_task.item(5, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("PartsMaximizeWindow", u"4", None));
        ___qtablewidgetitem20 = self.tw_task.item(5, 4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("PartsMaximizeWindow", u"5", None));
        ___qtablewidgetitem21 = self.tw_task.item(5, 5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("PartsMaximizeWindow", u"4", None));
        ___qtablewidgetitem22 = self.tw_task.item(6, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("PartsMaximizeWindow", u"3", None));
        ___qtablewidgetitem23 = self.tw_task.item(6, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("PartsMaximizeWindow", u"10", None));
        ___qtablewidgetitem24 = self.tw_task.item(6, 2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("PartsMaximizeWindow", u"16", None));
        ___qtablewidgetitem25 = self.tw_task.item(6, 3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("PartsMaximizeWindow", u"0", None));
        ___qtablewidgetitem26 = self.tw_task.item(6, 4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("PartsMaximizeWindow", u"8", None));
        ___qtablewidgetitem27 = self.tw_task.item(6, 5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("PartsMaximizeWindow", u"0", None));
        self.tw_task.setSortingEnabled(__sortingEnabled)

        self.l_task_1.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0418\u0437 500 \u043b\u0438\u0441\u0442\u043e\u0432 \u0436\u0435\u043b\u0435\u0437\u0430 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0438 300 \u043b\u0438\u0441\u0442\u043e\u0432 \u0436\u0435\u043b\u0435\u0437\u0430 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u043c\u0438 \u0441\u043f\u043e\u0441\u043e\u0431\u0430\u043c\u0438 \u0432\u044b\u043a\u0440\u0430\u0438\u0432\u0430\u044e\u0442\u0441\u044f \u0442\u0440\u0438 \u0432\u0438\u0434\u0430 \u0434\u0435\u0442\u0430\u043b\u0435\u0439. \u0414\u0430\u043d\u044b \u043d\u043e\u0440\u043c\u044b \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u0432\u044b\u0445\u043e\u0434\u0430 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u043f\u043e \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u043c \u0441\u043f\u043e\u0441\u043e\u0431\u0430\u043c.", None))
        self.l_variant.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 - \u0412\u0430\u0440\u0438\u0430\u043d\u0442 6", None))
        self.l_task_2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432 \u0434\u0435\u0442\u0430\u043b\u0435\u0439, \u0435\u0441\u043b\u0438 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442 \u0441\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 \u0447\u0435\u0442\u044b\u0440\u0435\u0445 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u0432\u0438\u0434\u0430 1, \u0442\u0440\u0435\u0445 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u0432\u0438\u0434\u0430 2 \u0438 \u0434\u0432\u0443\u0445 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u0432\u0438\u0434\u0430 3. \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c, \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043b\u0438\u0441\u0442\u043e\u0432 \u0436\u0435\u043b\u0435\u0437\u0430 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 2 \u0440\u0430\u0441\u043a\u0440\u0430\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043f\u043e"
                        " \u043f\u0435\u0440\u0432\u043e\u043c\u0443 \u0441\u043f\u043e\u0441\u043e\u0431\u0443, \u043a\u0430\u043a\u043e\u0432\u043e \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432, \u043d\u0430 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u0441\u044f \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432, \u0435\u0441\u043b\u0438 \u0432 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442 \u0440\u0435\u0448\u0435\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0440\u0435\u0442\u044c\u044e \u0434\u0435\u0442\u0430\u043b\u044c \u0432\u0438\u0434\u0430 3?", None))
        self.tabw_steps.setTabText(self.tabw_steps.indexOf(self.tab_task), QCoreApplication.translate("PartsMaximizeWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.l_obj_func.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.tabw_steps.setTabText(self.tabw_steps.indexOf(self.tab_obj_func), QCoreApplication.translate("PartsMaximizeWindow", u"\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.l_constraints.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f", None))
        self.tabw_steps.setTabText(self.tabw_steps.indexOf(self.tab_constraints), QCoreApplication.translate("PartsMaximizeWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f", None))
        self.l_lp_given.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0420\u0435\u0448\u0438\u043c \u0437\u0430\u0434\u0430\u0447\u0443 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.tabw_steps.setTabText(self.tabw_steps.indexOf(self.tab_solution), QCoreApplication.translate("PartsMaximizeWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435", None))
    # retranslateUi

