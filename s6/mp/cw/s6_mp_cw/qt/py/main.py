# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 303)
        MainWindow.setMinimumSize(QSize(700, 0))
        self.w_main = QWidget(MainWindow)
        self.w_main.setObjectName(u"w_main")
        self.gl_main = QGridLayout(self.w_main)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setContentsMargins(-1, -1, -1, 0)
        self.tw_model = QTableWidget(self.w_main)
        if (self.tw_model.columnCount() < 4):
            self.tw_model.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
        self.tw_model.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
        self.tw_model.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
        self.tw_model.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
        self.tw_model.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tw_model.rowCount() < 4):
            self.tw_model.setRowCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(1, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(1, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(2, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(2, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(2, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(3, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(3, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(3, 3, __qtablewidgetitem23)
        self.tw_model.setObjectName(u"tw_model")

        self.gl_main.addWidget(self.tw_model, 2, 0, 1, 2)

        self.l_model = QLabel(self.w_main)
        self.l_model.setObjectName(u"l_model")

        self.gl_main.addWidget(self.l_model, 0, 0, 2, 3)

        self.tabw_solve = QTabWidget(self.w_main)
        self.tabw_solve.setObjectName(u"tabw_solve")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabw_solve.sizePolicy().hasHeightForWidth())
        self.tabw_solve.setSizePolicy(sizePolicy)
        self.tabw_solve.setMinimumSize(QSize(268, 0))
        self.t_one_off = QWidget()
        self.t_one_off.setObjectName(u"t_one_off")
        self.vl_one_off = QVBoxLayout(self.t_one_off)
        self.vl_one_off.setObjectName(u"vl_one_off")
        self.l_oo_supply = QLabel(self.t_one_off)
        self.l_oo_supply.setObjectName(u"l_oo_supply")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.l_oo_supply.setFont(font)

        self.vl_one_off.addWidget(self.l_oo_supply)

        self.le_oo_supply = QLineEdit(self.t_one_off)
        self.le_oo_supply.setObjectName(u"le_oo_supply")

        self.vl_one_off.addWidget(self.le_oo_supply)

        self.l_oo_supply_hint = QLabel(self.t_one_off)
        self.l_oo_supply_hint.setObjectName(u"l_oo_supply_hint")
        self.l_oo_supply_hint.setStyleSheet(u"color:grey")

        self.vl_one_off.addWidget(self.l_oo_supply_hint)

        self.vs_oo = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_one_off.addItem(self.vs_oo)

        self.pb_oo_solve = QPushButton(self.t_one_off)
        self.pb_oo_solve.setObjectName(u"pb_oo_solve")

        self.vl_one_off.addWidget(self.pb_oo_solve)

        self.tabw_solve.addTab(self.t_one_off, "")
        self.t_long_term = QWidget()
        self.t_long_term.setObjectName(u"t_long_term")
        self.vl_long_term = QVBoxLayout(self.t_long_term)
        self.vl_long_term.setObjectName(u"vl_long_term")
        self.l_lt_supply = QLabel(self.t_long_term)
        self.l_lt_supply.setObjectName(u"l_lt_supply")
        self.l_lt_supply.setFont(font)

        self.vl_long_term.addWidget(self.l_lt_supply)

        self.le_lt_supply = QLineEdit(self.t_long_term)
        self.le_lt_supply.setObjectName(u"le_lt_supply")

        self.vl_long_term.addWidget(self.le_lt_supply)

        self.l_lt_supply_hint = QLabel(self.t_long_term)
        self.l_lt_supply_hint.setObjectName(u"l_lt_supply_hint")
        self.l_lt_supply_hint.setStyleSheet(u"color:grey")

        self.vl_long_term.addWidget(self.l_lt_supply_hint)

        self.l_lt_step = QLabel(self.t_long_term)
        self.l_lt_step.setObjectName(u"l_lt_step")
        self.l_lt_step.setFont(font)

        self.vl_long_term.addWidget(self.l_lt_step)

        self.le_lt_step = QLineEdit(self.t_long_term)
        self.le_lt_step.setObjectName(u"le_lt_step")

        self.vl_long_term.addWidget(self.le_lt_step)

        self.l_lt_supply_hint_2 = QLabel(self.t_long_term)
        self.l_lt_supply_hint_2.setObjectName(u"l_lt_supply_hint_2")
        self.l_lt_supply_hint_2.setStyleSheet(u"color:grey")

        self.vl_long_term.addWidget(self.l_lt_supply_hint_2)

        self.l_lt_long = QLabel(self.t_long_term)
        self.l_lt_long.setObjectName(u"l_lt_long")
        self.l_lt_long.setFont(font)

        self.vl_long_term.addWidget(self.l_lt_long)

        self.le_lt_period = QLineEdit(self.t_long_term)
        self.le_lt_period.setObjectName(u"le_lt_period")

        self.vl_long_term.addWidget(self.le_lt_period)

        self.vs_lt = QSpacerItem(20, 192, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_long_term.addItem(self.vs_lt)

        self.pb_lt_solve = QPushButton(self.t_long_term)
        self.pb_lt_solve.setObjectName(u"pb_lt_solve")

        self.vl_long_term.addWidget(self.pb_lt_solve)

        self.tabw_solve.addTab(self.t_long_term, "")

        self.gl_main.addWidget(self.tabw_solve, 2, 2, 1, 1)

        MainWindow.setCentralWidget(self.w_main)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabw_solve.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043f\u043b\u0430\u043d\u0430", None))
        ___qtablewidgetitem = self.tw_model.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0430,\n"
"\u0447\u0435\u043b/\u0434\u043d\u0435\u0439", None));
        ___qtablewidgetitem1 = self.tw_model.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u043e\u0440\u043a\u0430,\n"
"\u0447\u0435\u043b/\u0434\u043d\u0435\u0439", None));
        ___qtablewidgetitem2 = self.tw_model.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0440\u0430\u0441\u043a\u0430,\n"
"\u0447\u0435\u043b/\u0434\u043d\u0435\u0439", None));
        ___qtablewidgetitem3 = self.tw_model.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c,\n"
"\u0442\u044b\u0441.\u0440/\u0448\u0442", None));
        ___qtablewidgetitem4 = self.tw_model.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0410", None));
        ___qtablewidgetitem5 = self.tw_model.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0411", None));
        ___qtablewidgetitem6 = self.tw_model.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0412", None));
        ___qtablewidgetitem7 = self.tw_model.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0412(\u043d)", None));

        __sortingEnabled = self.tw_model.isSortingEnabled()
        self.tw_model.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tw_model.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem9 = self.tw_model.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem10 = self.tw_model.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem11 = self.tw_model.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"25", None));
        ___qtablewidgetitem12 = self.tw_model.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem13 = self.tw_model.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem14 = self.tw_model.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem15 = self.tw_model.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem16 = self.tw_model.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem17 = self.tw_model.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem18 = self.tw_model.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem19 = self.tw_model.item(2, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem20 = self.tw_model.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem21 = self.tw_model.item(3, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem22 = self.tw_model.item(3, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem23 = self.tw_model.item(3, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"30", None));
        self.tw_model.setSortingEnabled(__sortingEnabled)

        self.l_model.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u0442\u044b \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432 \u043d\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u0441\u0442\u043e\u043b\u043e\u0432", None))
        self.l_oo_supply.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0430\u0441\u044b", None))
        self.le_oo_supply.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0430\u0441\u044b (\u0447\u0435\u043b/\u0434\u043d\u0435\u0439)", None))
        self.l_oo_supply_hint.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0432\u0438\u0434\u044b \u0437\u0430\u0442\u0440\u0430\u0442 \u0438\u043c\u0435\u044e\u0442 \u0440\u0430\u0432\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0430\u0441\u043e\u0432", None))
        self.pb_oo_solve.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u043f\u043b\u0430\u043d \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430", None))
        self.tabw_solve.setTabText(self.tabw_solve.indexOf(self.t_one_off), QCoreApplication.translate("MainWindow", u"\u041e\u0434\u043d\u043e\u0440\u0430\u0437\u043e\u0432\u044b\u0439 \u043f\u043b\u0430\u043d", None))
        self.l_lt_supply.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u044b\u0435 \u0437\u0430\u043f\u0430\u0441\u044b", None))
        self.le_lt_supply.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0430\u0441\u044b (\u0447\u0435\u043b/\u0434\u043d\u0435\u0439) \u043d\u0430 \u0441\u0442\u0430\u0440\u0442\u0435 \u043f\u043b\u0430\u043d\u0430", None))
        self.l_lt_supply_hint.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0432\u0438\u0434\u044b \u0437\u0430\u0442\u0440\u0430\u0442 \u0438\u043c\u0435\u044e\u0442 \u0440\u0430\u0432\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0430\u0441\u043e\u0432", None))
        self.l_lt_step.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0440\u043e\u0441\u0442/\u0443\u0431\u044b\u0442\u043e\u043a \u0437\u0430\u043f\u0430\u0441\u043e\u0432", None))
        self.le_lt_step.setText("")
        self.le_lt_step.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0435\u043b\u0438\u0447\u0438\u043d\u0443 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u043f\u0430\u0441\u043e\u0432", None))
        self.l_lt_supply_hint_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0430\u0441\u044b \u0431\u0443\u0434\u0443\u0442 \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c\u0441\u044f \u0435\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u043e", None))
        self.l_lt_long.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a", None))
        self.le_lt_period.setText("")
        self.le_lt_period.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0440\u043e\u043a \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432 \u043c\u0435\u0441\u044f\u0446\u0430\u0445", None))
        self.pb_lt_solve.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u043f\u043b\u0430\u043d \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430", None))
        self.tabw_solve.setTabText(self.tabw_solve.indexOf(self.t_long_term), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0441\u0440\u043e\u0447\u043d\u044b\u0439 \u043f\u043b\u0430\u043d", None))
    # retranslateUi

