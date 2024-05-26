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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 380)
        self.w_main = QWidget(MainWindow)
        self.w_main.setObjectName(u"w_main")
        self.gridLayout = QGridLayout(self.w_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_solve = QPushButton(self.w_main)
        self.pb_solve.setObjectName(u"pb_solve")

        self.gridLayout.addWidget(self.pb_solve, 4, 0, 1, 3)

        self.tw_model = QTableWidget(self.w_main)
        if (self.tw_model.columnCount() < 5):
            self.tw_model.setColumnCount(5)
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
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
        self.tw_model.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tw_model.rowCount() < 5):
            self.tw_model.setRowCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_model.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_model.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_model.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_model.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_model.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(0, 4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(1, 4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(2, 4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(3, 4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(4, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(4, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(4, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(4, 3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tw_model.setItem(4, 4, __qtablewidgetitem34)
        self.tw_model.setObjectName(u"tw_model")
        self.tw_model.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_model.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tw_model, 1, 0, 1, 3)

        self.l_model = QLabel(self.w_main)
        self.l_model.setObjectName(u"l_model")

        self.gridLayout.addWidget(self.l_model, 0, 0, 1, 3)

        self.pb_apply = QPushButton(self.w_main)
        self.pb_apply.setObjectName(u"pb_apply")
        self.pb_apply.setMinimumSize(QSize(75, 0))

        self.gridLayout.addWidget(self.pb_apply, 3, 2, 1, 1)

        self.le_demand = QLineEdit(self.w_main)
        self.le_demand.setObjectName(u"le_demand")

        self.gridLayout.addWidget(self.le_demand, 3, 1, 1, 1)

        self.l_demand = QLabel(self.w_main)
        self.l_demand.setObjectName(u"l_demand")

        self.gridLayout.addWidget(self.l_demand, 2, 1, 1, 2)

        MainWindow.setCentralWidget(self.w_main)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0442\u0435\u0440 \u0413\u0430\u043c\u0431\u0441", None))
        self.pb_solve.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u043f\u043b\u0430\u043d \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430", None))
        ___qtablewidgetitem = self.tw_model.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None));
        ___qtablewidgetitem1 = self.tw_model.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0430,\n"
"\u0447\u0435\u043b/\u0434\u043d\u0435\u0439", None));
        ___qtablewidgetitem2 = self.tw_model.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u043e\u0440\u043a\u0430,\n"
"\u0447\u0435\u0434/\u0434\u043d\u0435\u0439", None));
        ___qtablewidgetitem3 = self.tw_model.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0440\u0430\u0441\u043a\u0430,\n"
"\u0447\u0435\u043b/\u0434\u043d\u0435\u0439", None));
        ___qtablewidgetitem4 = self.tw_model.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c,\n"
"\u0442\u044b\u0441.\u0440/\u0448\u0442", None));

        __sortingEnabled = self.tw_model.isSortingEnabled()
        self.tw_model.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tw_model.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0410", None));
        ___qtablewidgetitem6 = self.tw_model.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem7 = self.tw_model.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem8 = self.tw_model.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem9 = self.tw_model.item(0, 4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"25", None));
        ___qtablewidgetitem10 = self.tw_model.item(1, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0411", None));
        ___qtablewidgetitem11 = self.tw_model.item(1, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem12 = self.tw_model.item(1, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem13 = self.tw_model.item(1, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem14 = self.tw_model.item(1, 4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem15 = self.tw_model.item(2, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u0412", None));
        ___qtablewidgetitem16 = self.tw_model.item(2, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem17 = self.tw_model.item(2, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem18 = self.tw_model.item(2, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem19 = self.tw_model.item(2, 4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem20 = self.tw_model.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043e\u043a\u0440\u0430\u0448\u0435\u043d\u043d\u044b\u0435\n"
"\u0412", None));
        ___qtablewidgetitem21 = self.tw_model.item(3, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem22 = self.tw_model.item(3, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem23 = self.tw_model.item(3, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem24 = self.tw_model.item(3, 4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem25 = self.tw_model.item(4, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0430\u0441\u044b", None));
        ___qtablewidgetitem26 = self.tw_model.item(4, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u0425", None));
        ___qtablewidgetitem27 = self.tw_model.item(4, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u0425", None));
        ___qtablewidgetitem28 = self.tw_model.item(4, 3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u0425", None));
        self.tw_model.setSortingEnabled(__sortingEnabled)

        self.l_model.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u0442\u044b \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432 \u043d\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u0441\u0442\u043e\u043b\u043e\u0432", None))
        self.pb_apply.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.le_demand.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0425", None))
        self.l_demand.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0430\u0441\u044b", None))
    # retranslateUi

