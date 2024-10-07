# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'language_expert.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LanguageExpertWindow(object):
    def setupUi(self, LanguageExpertWindow):
        if not LanguageExpertWindow.objectName():
            LanguageExpertWindow.setObjectName(u"LanguageExpertWindow")
        LanguageExpertWindow.resize(300, 250)
        LanguageExpertWindow.setMinimumSize(QSize(300, 250))
        LanguageExpertWindow.setMaximumSize(QSize(300, 16777215))
        self.vl_main = QVBoxLayout(LanguageExpertWindow)
        self.vl_main.setObjectName(u"vl_main")
        self.l_title = QLabel(LanguageExpertWindow)
        self.l_title.setObjectName(u"l_title")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.l_title.setFont(font)
        self.l_title.setWordWrap(True)

        self.vl_main.addWidget(self.l_title)

        self.vl_question = QVBoxLayout()
        self.vl_question.setObjectName(u"vl_question")
        self.vl_question.setContentsMargins(-1, -1, -1, 12)
        self.l_welcome_title = QLabel(LanguageExpertWindow)
        self.l_welcome_title.setObjectName(u"l_welcome_title")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.l_welcome_title.setFont(font1)
        self.l_welcome_title.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.vl_question.addWidget(self.l_welcome_title)

        self.l_welcome_decription = QLabel(LanguageExpertWindow)
        self.l_welcome_decription.setObjectName(u"l_welcome_decription")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI Light"])
        font2.setPointSize(9)
        self.l_welcome_decription.setFont(font2)
        self.l_welcome_decription.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.vl_question.addWidget(self.l_welcome_decription)


        self.vl_main.addLayout(self.vl_question)

        self.pb_choose = QPushButton(LanguageExpertWindow)
        self.pb_choose.setObjectName(u"pb_choose")
        self.pb_choose.setMinimumSize(QSize(0, 40))
        self.pb_choose.setStyleSheet(u".QPushButton {\n"
"  	color:#fff;\n"
"	border: 1px solid ;\n"
"	border-color: #00aaff;\n"
" 	border-radius: 3px;\n"
"  	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2dabf9, stop: 1 #0688fa);\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0688fa, stop: 1 #2dabf9);\n"
"}")

        self.vl_main.addWidget(self.pb_choose)


        self.retranslateUi(LanguageExpertWindow)

        QMetaObject.connectSlotsByName(LanguageExpertWindow)
    # setupUi

    def retranslateUi(self, LanguageExpertWindow):
        LanguageExpertWindow.setWindowTitle(QCoreApplication.translate("LanguageExpertWindow", u"\u042f\u0437\u044b\u043a\u043e\u0432\u043e\u0439 \u044d\u043a\u0441\u043f\u0435\u0440\u0442", None))
        self.l_welcome_title.setText(QCoreApplication.translate("LanguageExpertWindow", u"\u042f\u0437\u044b\u043a\u043e\u0432\u043e\u0439 \u044d\u043a\u0441\u043f\u0435\u0440\u0442", None))
        self.l_welcome_decription.setText(QCoreApplication.translate("LanguageExpertWindow", u"\u0414\u0430\u043d\u043d\u044b\u0439 \u043f\u043e\u043c\u043e\u0449\u043d\u0438\u043a \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0432\u044b\u0431\u0440\u0430\u0442\u044c\n"
"\u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438\u0439 \u0434\u043b\u044f \u043d\u0443\u0436\u0434 \u0432\u0430\u0448\u0435\u0433\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \n"
"\u044f\u0437\u044b\u043a \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.pb_choose.setText(QCoreApplication.translate("LanguageExpertWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
    # retranslateUi

