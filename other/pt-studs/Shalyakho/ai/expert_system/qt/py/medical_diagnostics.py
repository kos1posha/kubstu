# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'medical_diagnostics.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_MedicalDiagnosticsWindow(object):
    def setupUi(self, MedicalDiagnosticsWindow):
        if not MedicalDiagnosticsWindow.objectName():
            MedicalDiagnosticsWindow.setObjectName(u"MedicalDiagnosticsWindow")
        MedicalDiagnosticsWindow.resize(500, 300)
        MedicalDiagnosticsWindow.setMinimumSize(QSize(500, 300))
        MedicalDiagnosticsWindow.setMaximumSize(QSize(500, 300))
        self.gridLayout = QGridLayout(MedicalDiagnosticsWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pte_output = QPlainTextEdit(MedicalDiagnosticsWindow)
        self.pte_output.setObjectName(u"pte_output")
        font = QFont()
        font.setPointSize(11)
        self.pte_output.setFont(font)
        self.pte_output.setReadOnly(True)

        self.gridLayout.addWidget(self.pte_output, 1, 0, 1, 3)

        self.l_expert_system_output = QLabel(MedicalDiagnosticsWindow)
        self.l_expert_system_output.setObjectName(u"l_expert_system_output")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_expert_system_output.sizePolicy().hasHeightForWidth())
        self.l_expert_system_output.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.l_expert_system_output.setFont(font1)

        self.gridLayout.addWidget(self.l_expert_system_output, 0, 0, 1, 2)

        self.le_input = QLineEdit(MedicalDiagnosticsWindow)
        self.le_input.setObjectName(u"le_input")
        self.le_input.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.le_input, 2, 1, 1, 2)

        self.l_input = QLabel(MedicalDiagnosticsWindow)
        self.l_input.setObjectName(u"l_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_input.sizePolicy().hasHeightForWidth())
        self.l_input.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.l_input.setFont(font2)

        self.gridLayout.addWidget(self.l_input, 2, 0, 1, 1)

        self.pb_clear = QPushButton(MedicalDiagnosticsWindow)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setMaximumSize(QSize(90, 16777215))

        self.gridLayout.addWidget(self.pb_clear, 0, 2, 1, 1)


        self.retranslateUi(MedicalDiagnosticsWindow)

        QMetaObject.connectSlotsByName(MedicalDiagnosticsWindow)
    # setupUi

    def retranslateUi(self, MedicalDiagnosticsWindow):
        MedicalDiagnosticsWindow.setWindowTitle(QCoreApplication.translate("MedicalDiagnosticsWindow", u"\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u0430\u044f \u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430", None))
        self.l_expert_system_output.setText(QCoreApplication.translate("MedicalDiagnosticsWindow", u"\u0412\u044b\u0432\u043e\u0434 \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043d\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.l_input.setText(QCoreApplication.translate("MedicalDiagnosticsWindow", u"\u0412\u0432\u043e\u0434 ", None))
        self.pb_clear.setText(QCoreApplication.translate("MedicalDiagnosticsWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

