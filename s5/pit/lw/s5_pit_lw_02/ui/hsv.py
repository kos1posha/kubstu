# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hsv.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSlider, QWidget)

class Ui_HSVEditorWindow(object):
    def setupUi(self, HSVEditorWindow):
        if not HSVEditorWindow.objectName():
            HSVEditorWindow.setObjectName(u"HSVEditorWindow")
        HSVEditorWindow.resize(241, 74)
        self.gl_main = QGridLayout(HSVEditorWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.hs_saturation = QSlider(HSVEditorWindow)
        self.hs_saturation.setObjectName(u"hs_saturation")
        self.hs_saturation.setMaximum(100)
        self.hs_saturation.setOrientation(Qt.Horizontal)

        self.gl_main.addWidget(self.hs_saturation, 1, 1, 1, 1)

        self.l_saturation_v = QLabel(HSVEditorWindow)
        self.l_saturation_v.setObjectName(u"l_saturation_v")

        self.gl_main.addWidget(self.l_saturation_v, 1, 2, 1, 1)

        self.l_saturation = QLabel(HSVEditorWindow)
        self.l_saturation.setObjectName(u"l_saturation")

        self.gl_main.addWidget(self.l_saturation, 1, 0, 1, 1)

        self.hs_value = QSlider(HSVEditorWindow)
        self.hs_value.setObjectName(u"hs_value")
        self.hs_value.setMaximum(100)
        self.hs_value.setOrientation(Qt.Horizontal)

        self.gl_main.addWidget(self.hs_value, 2, 1, 1, 1)

        self.l_hue_v = QLabel(HSVEditorWindow)
        self.l_hue_v.setObjectName(u"l_hue_v")

        self.gl_main.addWidget(self.l_hue_v, 0, 2, 1, 1)

        self.l_value = QLabel(HSVEditorWindow)
        self.l_value.setObjectName(u"l_value")

        self.gl_main.addWidget(self.l_value, 2, 0, 1, 1)

        self.l_hue = QLabel(HSVEditorWindow)
        self.l_hue.setObjectName(u"l_hue")

        self.gl_main.addWidget(self.l_hue, 0, 0, 1, 1)

        self.l_value_v = QLabel(HSVEditorWindow)
        self.l_value_v.setObjectName(u"l_value_v")

        self.gl_main.addWidget(self.l_value_v, 2, 2, 1, 1)

        self.hs_hue = QSlider(HSVEditorWindow)
        self.hs_hue.setObjectName(u"hs_hue")
        self.hs_hue.setMaximum(100)
        self.hs_hue.setOrientation(Qt.Horizontal)

        self.gl_main.addWidget(self.hs_hue, 0, 1, 1, 1)


        self.retranslateUi(HSVEditorWindow)

        QMetaObject.connectSlotsByName(HSVEditorWindow)
    # setupUi

    def retranslateUi(self, HSVEditorWindow):
        HSVEditorWindow.setWindowTitle(QCoreApplication.translate("HSVEditorWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 HSV", None))
        self.l_saturation_v.setText(QCoreApplication.translate("HSVEditorWindow", u"0.00", None))
        self.l_saturation.setText(QCoreApplication.translate("HSVEditorWindow", u"\u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u043e\u0441\u0442\u044c", None))
        self.l_hue_v.setText(QCoreApplication.translate("HSVEditorWindow", u"0.00", None))
        self.l_value.setText(QCoreApplication.translate("HSVEditorWindow", u"\u042f\u0440\u043a\u043e\u0441\u0442\u044c", None))
        self.l_hue.setText(QCoreApplication.translate("HSVEditorWindow", u"\u0422\u043e\u043d", None))
        self.l_value_v.setText(QCoreApplication.translate("HSVEditorWindow", u"0.00", None))
    # retranslateUi

