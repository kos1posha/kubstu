# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result_view.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QSizePolicy,
    QTabWidget, QWidget)

class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        if not ResultWindow.objectName():
            ResultWindow.setObjectName(u"ResultWindow")
        ResultWindow.resize(500, 350)
        self.gl_main = QGridLayout(ResultWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.tw_iterations = QTabWidget(ResultWindow)
        self.tw_iterations.setObjectName(u"tw_iterations")
        self.tw_iterations.setTabPosition(QTabWidget.TabPosition.North)
        self.tw_iterations.setDocumentMode(True)

        self.gl_main.addWidget(self.tw_iterations, 0, 0, 1, 1)


        self.retranslateUi(ResultWindow)

        self.tw_iterations.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(ResultWindow)
    # setupUi

    def retranslateUi(self, ResultWindow):
        ResultWindow.setWindowTitle(QCoreApplication.translate("ResultWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
    # retranslateUi

