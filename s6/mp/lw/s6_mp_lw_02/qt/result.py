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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QSizePolicy,
    QTextEdit, QWidget)

class Ui_ResultDialog(object):
    def setupUi(self, ResultDialog):
        if not ResultDialog.objectName():
            ResultDialog.setObjectName(u"ResultDialog")
        ResultDialog.resize(544, 449)
        self.gl_main = QGridLayout(ResultDialog)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setContentsMargins(0, 0, 0, 0)
        self.te_result = QTextEdit(ResultDialog)
        self.te_result.setObjectName(u"te_result")
        self.te_result.setReadOnly(True)

        self.gl_main.addWidget(self.te_result, 0, 0, 1, 1)


        self.retranslateUi(ResultDialog)

        QMetaObject.connectSlotsByName(ResultDialog)
    # setupUi

    def retranslateUi(self, ResultDialog):
        ResultDialog.setWindowTitle(QCoreApplication.translate("ResultDialog", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
    # retranslateUi

