# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_VitaminsLpSolverWindow(object):
    def setupUi(self, VitaminsLpSolverWindow):
        if not VitaminsLpSolverWindow.objectName():
            VitaminsLpSolverWindow.setObjectName(u"VitaminsLpSolverWindow")
        VitaminsLpSolverWindow.resize(714, 361)
        VitaminsLpSolverWindow.setMinimumSize(QSize(714, 0))
        VitaminsLpSolverWindow.setMaximumSize(QSize(860, 16777215))
        self.gl_main = QGridLayout(VitaminsLpSolverWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.tw_point = QTableWidget(VitaminsLpSolverWindow)
        if (self.tw_point.columnCount() < 7):
            self.tw_point.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_point.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_point.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_point.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_point.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_point.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_point.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_point.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tw_point.rowCount() < 1):
            self.tw_point.setRowCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tw_point.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tw_point.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tw_point.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tw_point.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tw_point.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tw_point.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tw_point.setItem(0, 5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tw_point.setItem(0, 6, __qtablewidgetitem14)
        self.tw_point.setObjectName(u"tw_point")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_point.sizePolicy().hasHeightForWidth())
        self.tw_point.setSizePolicy(sizePolicy)
        self.tw_point.horizontalHeader().setDefaultSectionSize(80)
        self.tw_point.verticalHeader().setVisible(False)

        self.gl_main.addWidget(self.tw_point, 6, 0, 7, 1)

        self.w_result = QWidget(VitaminsLpSolverWindow)
        self.w_result.setObjectName(u"w_result")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.w_result.sizePolicy().hasHeightForWidth())
        self.w_result.setSizePolicy(sizePolicy1)
        self.vl_result = QVBoxLayout(self.w_result)
        self.vl_result.setObjectName(u"vl_result")
        self.vl_result.setContentsMargins(0, 0, 0, 0)
        self.l_extr = QLabel(self.w_result)
        self.l_extr.setObjectName(u"l_extr")
        sizePolicy1.setHeightForWidth(self.l_extr.sizePolicy().hasHeightForWidth())
        self.l_extr.setSizePolicy(sizePolicy1)

        self.vl_result.addWidget(self.l_extr)

        self.l_a = QLabel(self.w_result)
        self.l_a.setObjectName(u"l_a")
        sizePolicy1.setHeightForWidth(self.l_a.sizePolicy().hasHeightForWidth())
        self.l_a.setSizePolicy(sizePolicy1)

        self.vl_result.addWidget(self.l_a)

        self.l_c = QLabel(self.w_result)
        self.l_c.setObjectName(u"l_c")
        sizePolicy1.setHeightForWidth(self.l_c.sizePolicy().hasHeightForWidth())
        self.l_c.setSizePolicy(sizePolicy1)

        self.vl_result.addWidget(self.l_c)

        self.l_b6 = QLabel(self.w_result)
        self.l_b6.setObjectName(u"l_b6")

        self.vl_result.addWidget(self.l_b6)


        self.gl_main.addWidget(self.w_result, 2, 0, 4, 1)

        self.tw_model = QTableWidget(VitaminsLpSolverWindow)
        if (self.tw_model.columnCount() < 8):
            self.tw_model.setColumnCount(8)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        if (self.tw_model.rowCount() < 4):
            self.tw_model.setRowCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 7, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 7, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 6, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 7, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 6, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem58.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(3, 7, __qtablewidgetitem58)
        self.tw_model.setObjectName(u"tw_model")
        sizePolicy.setHeightForWidth(self.tw_model.sizePolicy().hasHeightForWidth())
        self.tw_model.setSizePolicy(sizePolicy)
        self.tw_model.horizontalHeader().setDefaultSectionSize(80)

        self.gl_main.addWidget(self.tw_model, 0, 0, 1, 2)

        self.w_buttons = QWidget(VitaminsLpSolverWindow)
        self.w_buttons.setObjectName(u"w_buttons")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.w_buttons.sizePolicy().hasHeightForWidth())
        self.w_buttons.setSizePolicy(sizePolicy2)
        self.vl_buttons = QVBoxLayout(self.w_buttons)
        self.vl_buttons.setObjectName(u"vl_buttons")
        self.vl_buttons.setContentsMargins(0, 0, 0, 0)
        self.pb_task = QPushButton(self.w_buttons)
        self.pb_task.setObjectName(u"pb_task")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pb_task.sizePolicy().hasHeightForWidth())
        self.pb_task.setSizePolicy(sizePolicy3)

        self.vl_buttons.addWidget(self.pb_task)

        self.pb_defaults = QPushButton(self.w_buttons)
        self.pb_defaults.setObjectName(u"pb_defaults")
        sizePolicy3.setHeightForWidth(self.pb_defaults.sizePolicy().hasHeightForWidth())
        self.pb_defaults.setSizePolicy(sizePolicy3)

        self.vl_buttons.addWidget(self.pb_defaults)

        self.pb_clear = QPushButton(self.w_buttons)
        self.pb_clear.setObjectName(u"pb_clear")
        sizePolicy3.setHeightForWidth(self.pb_clear.sizePolicy().hasHeightForWidth())
        self.pb_clear.setSizePolicy(sizePolicy3)

        self.vl_buttons.addWidget(self.pb_clear)

        self.pb_solve = QPushButton(self.w_buttons)
        self.pb_solve.setObjectName(u"pb_solve")
        sizePolicy3.setHeightForWidth(self.pb_solve.sizePolicy().hasHeightForWidth())
        self.pb_solve.setSizePolicy(sizePolicy3)

        self.vl_buttons.addWidget(self.pb_solve)


        self.gl_main.addWidget(self.w_buttons, 2, 1, 11, 1)


        self.retranslateUi(VitaminsLpSolverWindow)

        QMetaObject.connectSlotsByName(VitaminsLpSolverWindow)
    # setupUi

    def retranslateUi(self, VitaminsLpSolverWindow):
        VitaminsLpSolverWindow.setWindowTitle(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043a\u0443\u0440\u0441\u0430 \u0432\u0438\u0442\u0430\u043c\u0438\u043d\u043e\u0432", None))
        ___qtablewidgetitem = self.tw_point.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P1", None));
        ___qtablewidgetitem1 = self.tw_point.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P2", None));
        ___qtablewidgetitem2 = self.tw_point.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P3", None));
        ___qtablewidgetitem3 = self.tw_point.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P4", None));
        ___qtablewidgetitem4 = self.tw_point.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P5", None));
        ___qtablewidgetitem5 = self.tw_point.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P6", None));
        ___qtablewidgetitem6 = self.tw_point.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P7", None));
        ___qtablewidgetitem7 = self.tw_point.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e", None));

        __sortingEnabled = self.tw_point.isSortingEnabled()
        self.tw_point.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tw_point.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u043d/\u0434", None));
        ___qtablewidgetitem9 = self.tw_point.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u043d/\u0434", None));
        ___qtablewidgetitem10 = self.tw_point.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u043d/\u0434", None));
        ___qtablewidgetitem11 = self.tw_point.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u043d/\u0434", None));
        ___qtablewidgetitem12 = self.tw_point.item(0, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u043d/\u0434", None));
        ___qtablewidgetitem13 = self.tw_point.item(0, 5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u043d/\u0434", None));
        ___qtablewidgetitem14 = self.tw_point.item(0, 6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u043d/\u0434", None));
        self.tw_point.setSortingEnabled(__sortingEnabled)

        self.l_extr.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043a\u0443\u0440\u0441\u0430: \u043d/\u0434", None))
        self.l_a.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u0412\u0438\u0442\u0430\u043c\u0438\u043d \u0410: \u043d/\u0434", None))
        self.l_c.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u0412\u0438\u0442\u0430\u043c\u0438\u043d \u0421: \u043d/\u0434", None))
        self.l_b6.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u0412\u0438\u0442\u0430\u043c\u0438\u043d B\u2086: \u043d/\u0434", None))
        ___qtablewidgetitem15 = self.tw_model.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P1", None));
        ___qtablewidgetitem16 = self.tw_model.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P2", None));
        ___qtablewidgetitem17 = self.tw_model.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P3", None));
        ___qtablewidgetitem18 = self.tw_model.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P4", None));
        ___qtablewidgetitem19 = self.tw_model.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P5", None));
        ___qtablewidgetitem20 = self.tw_model.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P6", None));
        ___qtablewidgetitem21 = self.tw_model.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P7", None));
        ___qtablewidgetitem22 = self.tw_model.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e", None));
        ___qtablewidgetitem23 = self.tw_model.verticalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"A", None));
        ___qtablewidgetitem24 = self.tw_model.verticalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"C", None));
        ___qtablewidgetitem25 = self.tw_model.verticalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"B\u2086", None));
        ___qtablewidgetitem26 = self.tw_model.verticalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u0426\u0435\u043d\u0430 \u0437\u0430 1 \u0433\u0440.,\n"
"\u0442\u044b\u0441. \u0440\u0443\u0431.", None));

        __sortingEnabled1 = self.tw_model.isSortingEnabled()
        self.tw_model.setSortingEnabled(False)
        ___qtablewidgetitem27 = self.tw_model.item(0, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"5", None));
        ___qtablewidgetitem28 = self.tw_model.item(0, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem29 = self.tw_model.item(0, 2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"2", None));
        ___qtablewidgetitem30 = self.tw_model.item(0, 3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem31 = self.tw_model.item(0, 4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"3", None));
        ___qtablewidgetitem32 = self.tw_model.item(0, 5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem33 = self.tw_model.item(0, 6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"2", None));
        ___qtablewidgetitem34 = self.tw_model.item(0, 7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"100", None));
        ___qtablewidgetitem35 = self.tw_model.item(1, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"3", None));
        ___qtablewidgetitem36 = self.tw_model.item(1, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem37 = self.tw_model.item(1, 2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"5", None));
        ___qtablewidgetitem38 = self.tw_model.item(1, 3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem39 = self.tw_model.item(1, 4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"2", None));
        ___qtablewidgetitem40 = self.tw_model.item(1, 5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem41 = self.tw_model.item(1, 6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem42 = self.tw_model.item(1, 7)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"80", None));
        ___qtablewidgetitem43 = self.tw_model.item(2, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem44 = self.tw_model.item(2, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem45 = self.tw_model.item(2, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"3", None));
        ___qtablewidgetitem46 = self.tw_model.item(2, 3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem47 = self.tw_model.item(2, 4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"2", None));
        ___qtablewidgetitem48 = self.tw_model.item(2, 5)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem49 = self.tw_model.item(2, 6)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"6", None));
        ___qtablewidgetitem50 = self.tw_model.item(2, 7)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"120", None));
        ___qtablewidgetitem51 = self.tw_model.item(3, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"4", None));
        ___qtablewidgetitem52 = self.tw_model.item(3, 1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem53 = self.tw_model.item(3, 2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"5", None));
        ___qtablewidgetitem54 = self.tw_model.item(3, 3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"6", None));
        ___qtablewidgetitem55 = self.tw_model.item(3, 4)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"3.5", None));
        ___qtablewidgetitem56 = self.tw_model.item(3, 5)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"7", None));
        ___qtablewidgetitem57 = self.tw_model.item(3, 6)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"4", None));
        self.tw_model.setSortingEnabled(__sortingEnabled1)

        self.pb_task.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c\n"
"\u0437\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.pb_defaults.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\n"
"\u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.pb_clear.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pb_solve.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u041d\u0430\u0439\u0442\u0438\n"
"\u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
    # retranslateUi

