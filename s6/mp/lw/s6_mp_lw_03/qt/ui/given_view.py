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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
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
        self.vl_main = QVBoxLayout(self.w_main)
        self.vl_main.setObjectName(u"vl_main")
        self.w_supply = QWidget(self.w_main)
        self.w_supply.setObjectName(u"w_supply")
        self.hl_supply = QHBoxLayout(self.w_supply)
        self.hl_supply.setObjectName(u"hl_supply")
        self.hl_supply.setContentsMargins(0, 0, 0, 0)
        self.l_supply = QLabel(self.w_supply)
        self.l_supply.setObjectName(u"l_supply")

        self.hl_supply.addWidget(self.l_supply)

        self.pb_supply_add = QPushButton(self.w_supply)
        self.pb_supply_add.setObjectName(u"pb_supply_add")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_supply_add.sizePolicy().hasHeightForWidth())
        self.pb_supply_add.setSizePolicy(sizePolicy)
        self.pb_supply_add.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/icons/icons/plus.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_supply_add.setIcon(icon)
        self.pb_supply_add.setIconSize(QSize(10, 10))

        self.hl_supply.addWidget(self.pb_supply_add)

        self.l_supply_count = QLabel(self.w_supply)
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

        self.hl_supply.addWidget(self.l_supply_count)

        self.pb_supply_remove = QPushButton(self.w_supply)
        self.pb_supply_remove.setObjectName(u"pb_supply_remove")
        sizePolicy.setHeightForWidth(self.pb_supply_remove.sizePolicy().hasHeightForWidth())
        self.pb_supply_remove.setSizePolicy(sizePolicy)
        self.pb_supply_remove.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_supply_remove.setIcon(icon1)
        self.pb_supply_remove.setIconSize(QSize(10, 10))

        self.hl_supply.addWidget(self.pb_supply_remove)


        self.vl_main.addWidget(self.w_supply)

        self.w_demand = QWidget(self.w_main)
        self.w_demand.setObjectName(u"w_demand")
        self.hl_demand = QHBoxLayout(self.w_demand)
        self.hl_demand.setObjectName(u"hl_demand")
        self.hl_demand.setContentsMargins(0, 0, 0, 0)
        self.l_demand = QLabel(self.w_demand)
        self.l_demand.setObjectName(u"l_demand")

        self.hl_demand.addWidget(self.l_demand)

        self.pb_demand_add = QPushButton(self.w_demand)
        self.pb_demand_add.setObjectName(u"pb_demand_add")
        sizePolicy.setHeightForWidth(self.pb_demand_add.sizePolicy().hasHeightForWidth())
        self.pb_demand_add.setSizePolicy(sizePolicy)
        self.pb_demand_add.setMaximumSize(QSize(20, 20))
        self.pb_demand_add.setIcon(icon)
        self.pb_demand_add.setIconSize(QSize(10, 10))

        self.hl_demand.addWidget(self.pb_demand_add)

        self.l_demand_count = QLabel(self.w_demand)
        self.l_demand_count.setObjectName(u"l_demand_count")
        sizePolicy1.setHeightForWidth(self.l_demand_count.sizePolicy().hasHeightForWidth())
        self.l_demand_count.setSizePolicy(sizePolicy1)
        self.l_demand_count.setFont(font)
        self.l_demand_count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.hl_demand.addWidget(self.l_demand_count)

        self.pb_demand_remove = QPushButton(self.w_demand)
        self.pb_demand_remove.setObjectName(u"pb_demand_remove")
        sizePolicy.setHeightForWidth(self.pb_demand_remove.sizePolicy().hasHeightForWidth())
        self.pb_demand_remove.setSizePolicy(sizePolicy)
        self.pb_demand_remove.setMaximumSize(QSize(20, 20))
        self.pb_demand_remove.setIcon(icon1)
        self.pb_demand_remove.setIconSize(QSize(10, 10))

        self.hl_demand.addWidget(self.pb_demand_remove)


        self.vl_main.addWidget(self.w_demand)

        self.w_solvers = QWidget(self.w_main)
        self.w_solvers.setObjectName(u"w_solvers")
        self.hl_solvers = QHBoxLayout(self.w_solvers)
        self.hl_solvers.setSpacing(24)
        self.hl_solvers.setObjectName(u"hl_solvers")
        self.hl_solvers.setContentsMargins(0, 0, 0, 0)
        self.l_solvers = QLabel(self.w_solvers)
        self.l_solvers.setObjectName(u"l_solvers")
        sizePolicy1.setHeightForWidth(self.l_solvers.sizePolicy().hasHeightForWidth())
        self.l_solvers.setSizePolicy(sizePolicy1)

        self.hl_solvers.addWidget(self.l_solvers)

        self.cb_solvers = QComboBox(self.w_solvers)
        self.cb_solvers.addItem("")
        self.cb_solvers.addItem("")
        self.cb_solvers.addItem("")
        self.cb_solvers.setObjectName(u"cb_solvers")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb_solvers.sizePolicy().hasHeightForWidth())
        self.cb_solvers.setSizePolicy(sizePolicy2)

        self.hl_solvers.addWidget(self.cb_solvers)

        self.pb_solve = QPushButton(self.w_solvers)
        self.pb_solve.setObjectName(u"pb_solve")

        self.hl_solvers.addWidget(self.pb_solve)


        self.vl_main.addWidget(self.w_solvers)

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
        self.l_supply.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432", None))
        self.pb_supply_add.setText("")
        self.l_supply_count.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"4", None))
        self.pb_supply_remove.setText("")
        self.l_demand.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432", None))
        self.pb_demand_add.setText("")
        self.l_demand_count.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"5", None))
        self.pb_demand_remove.setText("")
        self.l_solvers.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041c\u0435\u0442\u043e\u0434", None))
        self.cb_solvers.setItemText(0, QCoreApplication.translate("TransportProblemGivenWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u044c\u0448\u0435\u0439 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438", None))
        self.cb_solvers.setItemText(1, QCoreApplication.translate("TransportProblemGivenWindow", u"\u0421\u0435\u0432\u0435\u0440\u043e-\u0437\u0430\u043f\u0430\u0434\u043d\u043e\u0433\u043e \u0443\u0433\u043b\u0430", None))
        self.cb_solvers.setItemText(2, QCoreApplication.translate("TransportProblemGivenWindow", u"\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u0424\u043e\u0433\u0435\u043b\u044f", None))

        self.pb_solve.setText(QCoreApplication.translate("TransportProblemGivenWindow", u"\u041d\u0430\u0439\u0442\u0438 \u043e\u043f\u043e\u0440\u043d\u044b\u0439 \u043f\u043b\u0430\u043d", None))
    # retranslateUi

