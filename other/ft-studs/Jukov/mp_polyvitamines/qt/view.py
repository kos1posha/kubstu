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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_VitaminsLpSolverWindow(object):
    def setupUi(self, VitaminsLpSolverWindow):
        if not VitaminsLpSolverWindow.objectName():
            VitaminsLpSolverWindow.setObjectName(u"VitaminsLpSolverWindow")
        VitaminsLpSolverWindow.resize(714, 359)
        VitaminsLpSolverWindow.setMinimumSize(QSize(714, 0))
        VitaminsLpSolverWindow.setMaximumSize(QSize(860, 16777215))
        self.gl_main = QGridLayout(VitaminsLpSolverWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.tw_model = QTableWidget(VitaminsLpSolverWindow)
        if (self.tw_model.columnCount() < 8):
            self.tw_model.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_model.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tw_model.rowCount() < 4):
            self.tw_model.setRowCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setVerticalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 7, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 5, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 6, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem43.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tw_model.setItem(3, 7, __qtablewidgetitem43)
        self.tw_model.setObjectName(u"tw_model")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_model.sizePolicy().hasHeightForWidth())
        self.tw_model.setSizePolicy(sizePolicy)
        self.tw_model.setMinimumSize(QSize(696, 142))
        self.tw_model.setMaximumSize(QSize(696, 142))
        self.tw_model.horizontalHeader().setDefaultSectionSize(80)

        self.gl_main.addWidget(self.tw_model, 1, 0, 1, 1)

        self.l_model = QLabel(VitaminsLpSolverWindow)
        self.l_model.setObjectName(u"l_model")

        self.gl_main.addWidget(self.l_model, 0, 0, 1, 1)

        self.pb_solve = QPushButton(VitaminsLpSolverWindow)
        self.pb_solve.setObjectName(u"pb_solve")
        self.pb_solve.setMinimumSize(QSize(140, 0))

        self.gl_main.addWidget(self.pb_solve, 2, 1, 1, 1)

        self.vs = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gl_main.addItem(self.vs, 3, 1, 1, 1)

        self.te_output = QTextEdit(VitaminsLpSolverWindow)
        self.te_output.setObjectName(u"te_output")
        self.te_output.setReadOnly(True)

        self.gl_main.addWidget(self.te_output, 2, 0, 3, 1)


        self.retranslateUi(VitaminsLpSolverWindow)

        QMetaObject.connectSlotsByName(VitaminsLpSolverWindow)
    # setupUi

    def retranslateUi(self, VitaminsLpSolverWindow):
        VitaminsLpSolverWindow.setWindowTitle(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043a\u0443\u0440\u0441\u0430 \u0432\u0438\u0442\u0430\u043c\u0438\u043d\u043e\u0432", None))
        ___qtablewidgetitem = self.tw_model.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P1", None));
        ___qtablewidgetitem1 = self.tw_model.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P2", None));
        ___qtablewidgetitem2 = self.tw_model.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P3", None));
        ___qtablewidgetitem3 = self.tw_model.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P4", None));
        ___qtablewidgetitem4 = self.tw_model.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P5", None));
        ___qtablewidgetitem5 = self.tw_model.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P6", None));
        ___qtablewidgetitem6 = self.tw_model.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"P7", None));
        ___qtablewidgetitem7 = self.tw_model.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e", None));
        ___qtablewidgetitem8 = self.tw_model.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"A", None));
        ___qtablewidgetitem9 = self.tw_model.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"C", None));
        ___qtablewidgetitem10 = self.tw_model.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"B6", None));
        ___qtablewidgetitem11 = self.tw_model.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"   \u0426\u0435\u043d\u0430   ", None));

        __sortingEnabled = self.tw_model.isSortingEnabled()
        self.tw_model.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.tw_model.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"5", None));
        ___qtablewidgetitem13 = self.tw_model.item(0, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem14 = self.tw_model.item(0, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"2", None));
        ___qtablewidgetitem15 = self.tw_model.item(0, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem16 = self.tw_model.item(0, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"3", None));
        ___qtablewidgetitem17 = self.tw_model.item(0, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem18 = self.tw_model.item(0, 6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"2", None));
        ___qtablewidgetitem19 = self.tw_model.item(0, 7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"100", None));
        ___qtablewidgetitem20 = self.tw_model.item(1, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"3", None));
        ___qtablewidgetitem21 = self.tw_model.item(1, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem22 = self.tw_model.item(1, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"5", None));
        ___qtablewidgetitem23 = self.tw_model.item(1, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem24 = self.tw_model.item(1, 4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"2", None));
        ___qtablewidgetitem25 = self.tw_model.item(1, 5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem26 = self.tw_model.item(1, 6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem27 = self.tw_model.item(1, 7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"80", None));
        ___qtablewidgetitem28 = self.tw_model.item(2, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem29 = self.tw_model.item(2, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem30 = self.tw_model.item(2, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"3", None));
        ___qtablewidgetitem31 = self.tw_model.item(2, 3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem32 = self.tw_model.item(2, 4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"2", None));
        ___qtablewidgetitem33 = self.tw_model.item(2, 5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"0", None));
        ___qtablewidgetitem34 = self.tw_model.item(2, 6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"6", None));
        ___qtablewidgetitem35 = self.tw_model.item(2, 7)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"120", None));
        ___qtablewidgetitem36 = self.tw_model.item(3, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"4", None));
        ___qtablewidgetitem37 = self.tw_model.item(3, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"1", None));
        ___qtablewidgetitem38 = self.tw_model.item(3, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"5", None));
        ___qtablewidgetitem39 = self.tw_model.item(3, 3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"6", None));
        ___qtablewidgetitem40 = self.tw_model.item(3, 4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"3.5", None));
        ___qtablewidgetitem41 = self.tw_model.item(3, 5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"7", None));
        ___qtablewidgetitem42 = self.tw_model.item(3, 6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"4", None));
        ___qtablewidgetitem43 = self.tw_model.item(3, 7)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"min", None));
        self.tw_model.setSortingEnabled(__sortingEnabled)

        self.l_model.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c:", None))
        self.pb_solve.setText(QCoreApplication.translate("VitaminsLpSolverWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
    # retranslateUi

