# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'given_view.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QGridLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resources_rc

class Ui_TransportProblemGivenWindow(object):
    def setupUi(self, TransportProblemGivenWindow):
        if not TransportProblemGivenWindow.objectName():
            TransportProblemGivenWindow.setObjectName(u"TransportProblemGivenWindow")
        TransportProblemGivenWindow.resize(600, 400)
        TransportProblemGivenWindow.setMinimumSize(QSize(600, 400))
        TransportProblemGivenWindow.setMaximumSize(QSize(600, 400))
        self.w_main = QWidget(TransportProblemGivenWindow)
        self.w_main.setObjectName(u"w_main")
        self.gl_main = QGridLayout(self.w_main)
        self.gl_main.setObjectName(u"gl_main")
        self.pb_demand_add = QPushButton(self.w_main)
        self.pb_demand_add.setObjectName(u"pb_demand_add")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_demand_add.sizePolicy().hasHeightForWidth())
        self.pb_demand_add.setSizePolicy(sizePolicy)
        self.pb_demand_add.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/icons/icons/plus.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_demand_add.setIcon(icon)
        self.pb_demand_add.setIconSize(QSize(10, 10))

        self.gl_main.addWidget(self.pb_demand_add, 2, 7, 1, 1)

        self.pb_demand_remove = QPushButton(self.w_main)
        self.pb_demand_remove.setObjectName(u"pb_demand_remove")
        sizePolicy.setHeightForWidth(self.pb_demand_remove.sizePolicy().hasHeightForWidth())
        self.pb_demand_remove.setSizePolicy(sizePolicy)
        self.pb_demand_remove.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_demand_remove.setIcon(icon1)
        self.pb_demand_remove.setIconSize(QSize(10, 10))

        self.gl_main.addWidget(self.pb_demand_remove, 2, 9, 1, 1)

        self.cb_solvers = QComboBox(self.w_main)
        self.cb_solvers.addItem("")
        self.cb_solvers.addItem("")
        self.cb_solvers.addItem("")
        self.cb_solvers.setObjectName(u"cb_solvers")

        self.gl_main.addWidget(self.cb_solvers, 7, 1, 1, 5)

        self.l_solvers = QLabel(self.w_main)
        self.l_solvers.setObjectName(u"l_solvers")

        self.gl_main.addWidget(self.l_solvers, 7, 0, 1, 1)

        self.tw_given = QTableWidget(self.w_main)
        if (self.tw_given.columnCount() < 6):
            self.tw_given.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_given.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_given.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_given.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_given.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_given.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_given.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tw_given.rowCount() < 5):
            self.tw_given.setRowCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_given.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_given.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_given.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_given.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(0, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(0, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(0, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(0, 3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(0, 4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(0, 5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(1, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(1, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(1, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(1, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(1, 4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(1, 5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(2, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(2, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(2, 2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(2, 3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(2, 4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(2, 5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(3, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(3, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(3, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(3, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(3, 4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(3, 5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(4, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(4, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(4, 2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(4, 3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tw_given.setItem(4, 4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem40.setFlags(Qt.NoItemFlags);
        self.tw_given.setItem(4, 5, __qtablewidgetitem40)
        self.tw_given.setObjectName(u"tw_given")
        self.tw_given.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tw_given.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tw_given.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tw_given.setAutoScroll(False)
        self.tw_given.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tw_given.horizontalHeader().setStretchLastSection(True)
        self.tw_given.verticalHeader().setStretchLastSection(True)

        self.gl_main.addWidget(self.tw_given, 5, 0, 1, 10)

        self.pb_solve = QPushButton(self.w_main)
        self.pb_solve.setObjectName(u"pb_solve")

        self.gl_main.addWidget(self.pb_solve, 7, 6, 1, 4)

        self.l_supply = QLabel(self.w_main)
        self.l_supply.setObjectName(u"l_supply")

        self.gl_main.addWidget(self.l_supply, 1, 0, 1, 4)

        self.l_supply_count = QLabel(self.w_main)
        self.l_supply_count.setObjectName(u"l_supply_count")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_supply_count.sizePolicy().hasHeightForWidth())
        self.l_supply_count.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        self.l_supply_count.setFont(font)
        self.l_supply_count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gl_main.addWidget(self.l_supply_count, 1, 8, 1, 1)

        self.l_demand_count = QLabel(self.w_main)
        self.l_demand_count.setObjectName(u"l_demand_count")
        sizePolicy1.setHeightForWidth(self.l_demand_count.sizePolicy().hasHeightForWidth())
        self.l_demand_count.setSizePolicy(sizePolicy1)
        self.l_demand_count.setFont(font)
        self.l_demand_count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gl_main.addWidget(self.l_demand_count, 2, 8, 1, 1)

        self.l_demand = QLabel(self.w_main)
        self.l_demand.setObjectName(u"l_demand")

        self.gl_main.addWidget(self.l_demand, 2, 0, 1, 4)

        self.pb_supply_remove = QPushButton(self.w_main)
        self.pb_supply_remove.setObjectName(u"pb_supply_remove")
        sizePolicy.setHeightForWidth(self.pb_supply_remove.sizePolicy().hasHeightForWidth())
        self.pb_supply_remove.setSizePolicy(sizePolicy)
        self.pb_supply_remove.setMaximumSize(QSize(20, 20))
        self.pb_supply_remove.setIcon(icon1)
        self.pb_supply_remove.setIconSize(QSize(10, 10))

        self.gl_main.addWidget(self.pb_supply_remove, 1, 9, 1, 1)

        self.pb_supply_add = QPushButton(self.w_main)
        self.pb_supply_add.setObjectName(u"pb_supply_add")
        sizePolicy.setHeightForWidth(self.pb_supply_add.sizePolicy().hasHeightForWidth())
        self.pb_supply_add.setSizePolicy(sizePolicy)
        self.pb_supply_add.setMaximumSize(QSize(20, 20))
        self.pb_supply_add.setIcon(icon)
        self.pb_supply_add.setIconSize(QSize(10, 10))

        self.gl_main.addWidget(self.pb_supply_add, 1, 7, 1, 1)

        TransportProblemGivenWindow.setCentralWidget(self.w_main)
        self.sb_main = QStatusBar(TransportProblemGivenWindow)
        self.sb_main.setObjectName(u"sb_main")
        self.sb_main.setSizeGripEnabled(False)
        TransportProblemGivenWindow.setStatusBar(self.sb_main)

        self.retranslateUi(TransportProblemGivenWindow)

        QMetaObject.connectSlotsByName(TransportProblemGivenWindow)
    # setupUi

    def retranslateUi(self, TransportProblemGivenWindow):
        TransportProblemGivenWindow.setWindowTitle(QCoreApplication.translate("TransportProblemGivenWindow", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430", None))
        self.pb_demand_add.setText("")
        self.pb_demand_remove.setText("")
        self.cb_solvers.setItemText(0, QCoreApplication.translate("TransportProblemGivenWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u044c\u0448\u0435\u0439 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438", None))
        self.cb_solvers.setItemText(1, QCoreApplication.translate("TransportProblemGivenWindow", u"\u0421\u0435\u0432\u0435\u0440\u043e-\u0437\u0430\u043f\u0430\u0434\u043d\u043e\u0433\u043e \u0443\u0433\u043b\u0430", None))
        self.cb_solvers.setItemText(2, QCoreApplication.translate("TransportProblemGivenWindow", u"\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u0424\u043e\u0433\u0435\u043b\u044f", None))

        self.l_solvers.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041c\u0435\u0442\u043e\u0434", None))
        ___qtablewidgetitem = self.tw_given.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"M1", None));
        ___qtablewidgetitem1 = self.tw_given.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"M2", None));
        ___qtablewidgetitem2 = self.tw_given.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041c3", None));
        ___qtablewidgetitem3 = self.tw_given.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041c4", None));
        ___qtablewidgetitem4 = self.tw_given.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"M5", None));
        ___qtablewidgetitem5 = self.tw_given.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"*", None));
        ___qtablewidgetitem6 = self.tw_given.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041f1", None));
        ___qtablewidgetitem7 = self.tw_given.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041f2", None));
        ___qtablewidgetitem8 = self.tw_given.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041f3", None));
        ___qtablewidgetitem9 = self.tw_given.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041f4", None));
        ___qtablewidgetitem10 = self.tw_given.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"*", None));

        __sortingEnabled = self.tw_given.isSortingEnabled()
        self.tw_given.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.tw_given.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"3", None));
        ___qtablewidgetitem12 = self.tw_given.item(0, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"5", None));
        ___qtablewidgetitem13 = self.tw_given.item(0, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"7", None));
        ___qtablewidgetitem14 = self.tw_given.item(0, 3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"2", None));
        ___qtablewidgetitem15 = self.tw_given.item(0, 4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"8", None));
        ___qtablewidgetitem16 = self.tw_given.item(0, 5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"500", None));
        ___qtablewidgetitem17 = self.tw_given.item(1, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"6", None));
        ___qtablewidgetitem18 = self.tw_given.item(1, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"5", None));
        ___qtablewidgetitem19 = self.tw_given.item(1, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"6", None));
        ___qtablewidgetitem20 = self.tw_given.item(1, 3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"8", None));
        ___qtablewidgetitem21 = self.tw_given.item(1, 4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"7", None));
        ___qtablewidgetitem22 = self.tw_given.item(1, 5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"400", None));
        ___qtablewidgetitem23 = self.tw_given.item(2, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"9", None));
        ___qtablewidgetitem24 = self.tw_given.item(2, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"1", None));
        ___qtablewidgetitem25 = self.tw_given.item(2, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"2", None));
        ___qtablewidgetitem26 = self.tw_given.item(2, 3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"4", None));
        ___qtablewidgetitem27 = self.tw_given.item(2, 4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"6", None));
        ___qtablewidgetitem28 = self.tw_given.item(2, 5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"800", None));
        ___qtablewidgetitem29 = self.tw_given.item(3, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"3", None));
        ___qtablewidgetitem30 = self.tw_given.item(3, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"5", None));
        ___qtablewidgetitem31 = self.tw_given.item(3, 2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"8", None));
        ___qtablewidgetitem32 = self.tw_given.item(3, 3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"9", None));
        ___qtablewidgetitem33 = self.tw_given.item(3, 4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"6", None));
        ___qtablewidgetitem34 = self.tw_given.item(3, 5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"500", None));
        ___qtablewidgetitem35 = self.tw_given.item(4, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"300", None));
        ___qtablewidgetitem36 = self.tw_given.item(4, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"500", None));
        ___qtablewidgetitem37 = self.tw_given.item(4, 2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"500", None));
        ___qtablewidgetitem38 = self.tw_given.item(4, 3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"600", None));
        ___qtablewidgetitem39 = self.tw_given.item(4, 4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"300", None));
        self.tw_given.setSortingEnabled(__sortingEnabled)

        self.pb_solve.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041d\u0430\u0439\u0442\u0438 \u043e\u043f\u043e\u0440\u043d\u044b\u0439 \u043f\u043b\u0430\u043d", None))
        self.l_supply.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432", None))
        self.l_supply_count.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"4", None))
        self.l_demand_count.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"5", None))
        self.l_demand.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432", None))
        self.pb_supply_remove.setText("")
        self.pb_supply_add.setText("")
    # retranslateUi

