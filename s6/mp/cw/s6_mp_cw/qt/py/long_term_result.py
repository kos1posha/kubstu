# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'long_term_result.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_LongTermResultDialog(object):
    def setupUi(self, LongTermResultDialog):
        if not LongTermResultDialog.objectName():
            LongTermResultDialog.setObjectName(u"LongTermResultDialog")
        LongTermResultDialog.resize(250, 330)
        LongTermResultDialog.setMinimumSize(QSize(250, 330))
        LongTermResultDialog.setMaximumSize(QSize(250, 330))
        self.vl_main = QVBoxLayout(LongTermResultDialog)
        self.vl_main.setObjectName(u"vl_main")
        self.vl_main.setContentsMargins(0, 0, 0, 0)
        self.tabw_plans = QTabWidget(LongTermResultDialog)
        self.tabw_plans.setObjectName(u"tabw_plans")
        self.tabw_plans.setDocumentMode(True)

        self.vl_main.addWidget(self.tabw_plans)


        self.retranslateUi(LongTermResultDialog)

        QMetaObject.connectSlotsByName(LongTermResultDialog)
    # setupUi

    def retranslateUi(self, LongTermResultDialog):
        LongTermResultDialog.setWindowTitle(QCoreApplication.translate("LongTermResultDialog", u"\u041f\u043b\u0430\u043d \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430", None))
    # retranslateUi

