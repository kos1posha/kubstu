# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'genetic.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_GeneticWindow(object):
    def setupUi(self, GeneticWindow):
        if not GeneticWindow.objectName():
            GeneticWindow.setObjectName(u"GeneticWindow")
        GeneticWindow.resize(500, 422)
        self.gl_main = QGridLayout(GeneticWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.f_population = QFrame(GeneticWindow)
        self.f_population.setObjectName(u"f_population")
        self.f_population.setMinimumSize(QSize(350, 350))
        self.f_population.setMaximumSize(QSize(350, 350))
        self.f_population.setFrameShape(QFrame.StyledPanel)
        self.f_population.setFrameShadow(QFrame.Sunken)
        self.gl_population = QGridLayout(self.f_population)
        self.gl_population.setObjectName(u"gl_population")
        self.gl_population.setContentsMargins(0, 0, 0, 0)

        self.gl_main.addWidget(self.f_population, 2, 0, 1, 3)

        self.l_function = QLabel(GeneticWindow)
        self.l_function.setObjectName(u"l_function")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_function.sizePolicy().hasHeightForWidth())
        self.l_function.setSizePolicy(sizePolicy)

        self.gl_main.addWidget(self.l_function, 0, 0, 1, 1)

        self.l_ylim = QLabel(GeneticWindow)
        self.l_ylim.setObjectName(u"l_ylim")
        sizePolicy.setHeightForWidth(self.l_ylim.sizePolicy().hasHeightForWidth())
        self.l_ylim.setSizePolicy(sizePolicy)
        self.l_ylim.setMaximumSize(QSize(80, 16777215))

        self.gl_main.addWidget(self.l_ylim, 0, 2, 1, 1)

        self.l_health = QLabel(GeneticWindow)
        self.l_health.setObjectName(u"l_health")
        sizePolicy.setHeightForWidth(self.l_health.sizePolicy().hasHeightForWidth())
        self.l_health.setSizePolicy(sizePolicy)

        self.gl_main.addWidget(self.l_health, 0, 3, 1, 1)

        self.le_function = QLineEdit(GeneticWindow)
        self.le_function.setObjectName(u"le_function")

        self.gl_main.addWidget(self.le_function, 1, 0, 1, 1)

        self.le_xlim = QLineEdit(GeneticWindow)
        self.le_xlim.setObjectName(u"le_xlim")
        self.le_xlim.setMaximumSize(QSize(80, 16777215))

        self.gl_main.addWidget(self.le_xlim, 1, 1, 1, 1)

        self.le_ylim = QLineEdit(GeneticWindow)
        self.le_ylim.setObjectName(u"le_ylim")
        self.le_ylim.setMaximumSize(QSize(80, 16777215))

        self.gl_main.addWidget(self.le_ylim, 1, 2, 1, 1)

        self.l_xlim = QLabel(GeneticWindow)
        self.l_xlim.setObjectName(u"l_xlim")
        sizePolicy.setHeightForWidth(self.l_xlim.sizePolicy().hasHeightForWidth())
        self.l_xlim.setSizePolicy(sizePolicy)
        self.l_xlim.setMaximumSize(QSize(80, 16777215))

        self.gl_main.addWidget(self.l_xlim, 0, 1, 1, 1)

        self.hl_actions = QHBoxLayout()
        self.hl_actions.setObjectName(u"hl_actions")
        self.pb_start = QPushButton(GeneticWindow)
        self.pb_start.setObjectName(u"pb_start")

        self.hl_actions.addWidget(self.pb_start)

        self.pb_stop = QPushButton(GeneticWindow)
        self.pb_stop.setObjectName(u"pb_stop")
        self.pb_stop.setEnabled(False)

        self.hl_actions.addWidget(self.pb_stop)

        self.pb_next = QPushButton(GeneticWindow)
        self.pb_next.setObjectName(u"pb_next")
        self.pb_next.setEnabled(False)

        self.hl_actions.addWidget(self.pb_next)


        self.gl_main.addLayout(self.hl_actions, 3, 0, 1, 3)

        self.tw_health = QTableWidget(GeneticWindow)
        if (self.tw_health.columnCount() < 3):
            self.tw_health.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_health.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_health.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_health.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tw_health.setObjectName(u"tw_health")
        self.tw_health.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_health.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_health.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_health.setSortingEnabled(True)
        self.tw_health.verticalHeader().setVisible(False)

        self.gl_main.addWidget(self.tw_health, 1, 3, 3, 1)


        self.retranslateUi(GeneticWindow)

        QMetaObject.connectSlotsByName(GeneticWindow)
    # setupUi

    def retranslateUi(self, GeneticWindow):
        GeneticWindow.setWindowTitle(QCoreApplication.translate("GeneticWindow", u"\u041e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f: \u0413\u0435\u043d\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.l_function.setText(QCoreApplication.translate("GeneticWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f f(x, y)", None))
        self.l_ylim.setText(QCoreApplication.translate("GeneticWindow", u"y (min max)", None))
        self.l_health.setText(QCoreApplication.translate("GeneticWindow", u"\u0417\u0434\u043e\u0440\u043e\u0432\u044c\u0435 \u043f\u043e\u043f\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.le_function.setText(QCoreApplication.translate("GeneticWindow", u"x + y", None))
        self.le_xlim.setText(QCoreApplication.translate("GeneticWindow", u"-50 50", None))
        self.le_ylim.setText(QCoreApplication.translate("GeneticWindow", u"-50 50", None))
        self.l_xlim.setText(QCoreApplication.translate("GeneticWindow", u"x (min max)", None))
        self.pb_start.setText(QCoreApplication.translate("GeneticWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.pb_stop.setText(QCoreApplication.translate("GeneticWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pb_next.setText(QCoreApplication.translate("GeneticWindow", u"\u0414\u0430\u043b\u044c\u0448\u0435", None))
        ___qtablewidgetitem = self.tw_health.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("GeneticWindow", u"x", None));
        ___qtablewidgetitem1 = self.tw_health.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("GeneticWindow", u"y", None));
        ___qtablewidgetitem2 = self.tw_health.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("GeneticWindow", u"f", None));
    # retranslateUi

