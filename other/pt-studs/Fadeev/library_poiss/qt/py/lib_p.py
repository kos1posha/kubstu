# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lib_p.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_LibPWindow(object):
    def setupUi(self, LibPWindow):
        if not LibPWindow.objectName():
            LibPWindow.setObjectName(u"LibPWindow")
        LibPWindow.resize(400, 300)
        self.gridLayout = QGridLayout(LibPWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_services_requests = QLabel(LibPWindow)
        self.l_services_requests.setObjectName(u"l_services_requests")

        self.gridLayout.addWidget(self.l_services_requests, 2, 0, 1, 1)

        self.l_income_requests = QLabel(LibPWindow)
        self.l_income_requests.setObjectName(u"l_income_requests")

        self.gridLayout.addWidget(self.l_income_requests, 0, 0, 1, 1)

        self.le_income_requests = QLineEdit(LibPWindow)
        self.le_income_requests.setObjectName(u"le_income_requests")

        self.gridLayout.addWidget(self.le_income_requests, 0, 1, 1, 1)

        self.le_services_requests = QLineEdit(LibPWindow)
        self.le_services_requests.setObjectName(u"le_services_requests")

        self.gridLayout.addWidget(self.le_services_requests, 2, 1, 1, 1)

        self.te_output = QTextEdit(LibPWindow)
        self.te_output.setObjectName(u"te_output")
        self.te_output.setReadOnly(True)

        self.gridLayout.addWidget(self.te_output, 5, 0, 1, 2)

        self.l_output = QLabel(LibPWindow)
        self.l_output.setObjectName(u"l_output")

        self.gridLayout.addWidget(self.l_output, 4, 0, 1, 2)

        self.pb_find = QPushButton(LibPWindow)
        self.pb_find.setObjectName(u"pb_find")

        self.gridLayout.addWidget(self.pb_find, 3, 0, 1, 2)


        self.retranslateUi(LibPWindow)

        QMetaObject.connectSlotsByName(LibPWindow)
    # setupUi

    def retranslateUi(self, LibPWindow):
        LibPWindow.setWindowTitle(QCoreApplication.translate("LibPWindow", u"\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430 - \u041e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.l_services_requests.setText(QCoreApplication.translate("LibPWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432 (\u0437/\u0447\u0430\u0441)", None))
        self.l_income_requests.setText(QCoreApplication.translate("LibPWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0438\u0445\u043e\u0434\u044f\u0449\u0438\u0445 \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432 (\u0437/\u0447\u0430\u0441)", None))
        self.le_income_requests.setText(QCoreApplication.translate("LibPWindow", u"10", None))
        self.le_services_requests.setText(QCoreApplication.translate("LibPWindow", u"12", None))
        self.l_output.setText(QCoreApplication.translate("LibPWindow", u"\u0412\u044b\u0432\u043e\u0434", None))
        self.pb_find.setText(QCoreApplication.translate("LibPWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
    # retranslateUi

