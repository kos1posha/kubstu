# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lp_result_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LpResultDialog(object):
    def setupUi(self, LpResultDialog):
        if not LpResultDialog.objectName():
            LpResultDialog.setObjectName(u"LpResultDialog")
        LpResultDialog.resize(460, 365)
        self.vl_main = QVBoxLayout(LpResultDialog)
        self.vl_main.setObjectName(u"vl_main")
        self.l_title = QLabel(LpResultDialog)
        self.l_title.setObjectName(u"l_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_title.sizePolicy().hasHeightForWidth())
        self.l_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.l_title.setFont(font)
        self.l_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.vl_main.addWidget(self.l_title)

        self.l_text_1 = QLabel(LpResultDialog)
        self.l_text_1.setObjectName(u"l_text_1")
        sizePolicy.setHeightForWidth(self.l_text_1.sizePolicy().hasHeightForWidth())
        self.l_text_1.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        self.l_text_1.setFont(font1)
        self.l_text_1.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_text_1.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_text_1.setWordWrap(True)
        self.l_text_1.setMargin(6)

        self.vl_main.addWidget(self.l_text_1)

        self.l_lp_status = QLabel(LpResultDialog)
        self.l_lp_status.setObjectName(u"l_lp_status")
        sizePolicy.setHeightForWidth(self.l_lp_status.sizePolicy().hasHeightForWidth())
        self.l_lp_status.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.l_lp_status.setFont(font2)
        self.l_lp_status.setTextFormat(Qt.TextFormat.RichText)
        self.l_lp_status.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_status.setMargin(4)

        self.vl_main.addWidget(self.l_lp_status)

        self.l_text_2 = QLabel(LpResultDialog)
        self.l_text_2.setObjectName(u"l_text_2")
        sizePolicy.setHeightForWidth(self.l_text_2.sizePolicy().hasHeightForWidth())
        self.l_text_2.setSizePolicy(sizePolicy)
        self.l_text_2.setFont(font1)
        self.l_text_2.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_text_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_text_2.setWordWrap(True)
        self.l_text_2.setMargin(6)

        self.vl_main.addWidget(self.l_text_2)

        self.l_extr_value = QLabel(LpResultDialog)
        self.l_extr_value.setObjectName(u"l_extr_value")
        sizePolicy.setHeightForWidth(self.l_extr_value.sizePolicy().hasHeightForWidth())
        self.l_extr_value.setSizePolicy(sizePolicy)
        self.l_extr_value.setFont(font2)
        self.l_extr_value.setTextFormat(Qt.TextFormat.RichText)
        self.l_extr_value.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_extr_value.setMargin(4)

        self.vl_main.addWidget(self.l_extr_value)

        self.l_text_3 = QLabel(LpResultDialog)
        self.l_text_3.setObjectName(u"l_text_3")
        sizePolicy.setHeightForWidth(self.l_text_3.sizePolicy().hasHeightForWidth())
        self.l_text_3.setSizePolicy(sizePolicy)
        self.l_text_3.setFont(font1)
        self.l_text_3.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_text_3.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_text_3.setWordWrap(True)
        self.l_text_3.setMargin(6)

        self.vl_main.addWidget(self.l_text_3)

        self.l_extr_point = QLabel(LpResultDialog)
        self.l_extr_point.setObjectName(u"l_extr_point")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_extr_point.sizePolicy().hasHeightForWidth())
        self.l_extr_point.setSizePolicy(sizePolicy1)
        self.l_extr_point.setFont(font2)
        self.l_extr_point.setTextFormat(Qt.TextFormat.RichText)
        self.l_extr_point.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_extr_point.setMargin(4)

        self.vl_main.addWidget(self.l_extr_point)

        self.l_text_4 = QLabel(LpResultDialog)
        self.l_text_4.setObjectName(u"l_text_4")
        sizePolicy.setHeightForWidth(self.l_text_4.sizePolicy().hasHeightForWidth())
        self.l_text_4.setSizePolicy(sizePolicy)
        self.l_text_4.setFont(font1)
        self.l_text_4.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_text_4.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_text_4.setWordWrap(True)
        self.l_text_4.setMargin(6)

        self.vl_main.addWidget(self.l_text_4)

        self.l_constraints_default = QLabel(LpResultDialog)
        self.l_constraints_default.setObjectName(u"l_constraints_default")
        sizePolicy1.setHeightForWidth(self.l_constraints_default.sizePolicy().hasHeightForWidth())
        self.l_constraints_default.setSizePolicy(sizePolicy1)
        self.l_constraints_default.setFont(font2)
        self.l_constraints_default.setTextFormat(Qt.TextFormat.RichText)
        self.l_constraints_default.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_constraints_default.setMargin(4)

        self.vl_main.addWidget(self.l_constraints_default)


        self.retranslateUi(LpResultDialog)

        QMetaObject.connectSlotsByName(LpResultDialog)
    # setupUi

    def retranslateUi(self, LpResultDialog):
        LpResultDialog.setWindowTitle(QCoreApplication.translate("LpResultDialog", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.l_title.setText(QCoreApplication.translate("LpResultDialog", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.l_text_1.setText(QCoreApplication.translate("LpResultDialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0435\u0448\u0435\u043d\u0438\u044f:", None))
        self.l_text_2.setText(QCoreApplication.translate("LpResultDialog", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 (\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u0432 \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u043e\u0439 \u0442\u043e\u0447\u043a\u0435):", None))
        self.l_text_3.setText(QCoreApplication.translate("LpResultDialog", u"\u0422\u043e\u0447\u043a\u0430 \u044d\u043a\u0441\u0442\u0440\u0435\u043c\u0443\u043c\u0430 (\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0438\u0441\u043a\u043e\u043c\u044b\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432):", None))
        self.l_text_4.setText(QCoreApplication.translate("LpResultDialog", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f:", None))
    # retranslateUi

