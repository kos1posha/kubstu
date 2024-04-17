# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_FuncToGraphWindow(object):
    def setupUi(self, FuncToGraphWindow):
        if not FuncToGraphWindow.objectName():
            FuncToGraphWindow.setObjectName(u"FuncToGraphWindow")
        FuncToGraphWindow.resize(350, 175)
        self.gridLayout = QGridLayout(FuncToGraphWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_function = QLabel(FuncToGraphWindow)
        self.l_function.setObjectName(u"l_function")

        self.gridLayout.addWidget(self.l_function, 0, 0, 1, 4)

        self.l_y = QLabel(FuncToGraphWindow)
        self.l_y.setObjectName(u"l_y")

        self.gridLayout.addWidget(self.l_y, 1, 0, 1, 1)

        self.le_function = QLineEdit(FuncToGraphWindow)
        self.le_function.setObjectName(u"le_function")
        self.le_function.setStyleSheet(u"")

        self.gridLayout.addWidget(self.le_function, 1, 1, 1, 1)

        self.pb_draw = QPushButton(FuncToGraphWindow)
        self.pb_draw.setObjectName(u"pb_draw")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_draw.sizePolicy().hasHeightForWidth())
        self.pb_draw.setSizePolicy(sizePolicy)
        self.pb_draw.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.pb_draw, 1, 2, 1, 1)

        self.hl_params = QHBoxLayout()
        self.hl_params.setObjectName(u"hl_params")
        self.l_start = QLabel(FuncToGraphWindow)
        self.l_start.setObjectName(u"l_start")

        self.hl_params.addWidget(self.l_start)

        self.dsb_start = QDoubleSpinBox(FuncToGraphWindow)
        self.dsb_start.setObjectName(u"dsb_start")
        self.dsb_start.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_start.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.dsb_start.setDecimals(6)
        self.dsb_start.setMinimum(-999999.999998999992386)
        self.dsb_start.setMaximum(999999.999998999992386)
        self.dsb_start.setValue(0.000000000000000)

        self.hl_params.addWidget(self.dsb_start)

        self.l_end = QLabel(FuncToGraphWindow)
        self.l_end.setObjectName(u"l_end")

        self.hl_params.addWidget(self.l_end)

        self.dsb_end = QDoubleSpinBox(FuncToGraphWindow)
        self.dsb_end.setObjectName(u"dsb_end")
        self.dsb_end.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_end.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.dsb_end.setDecimals(6)
        self.dsb_end.setMinimum(-999999.999998999992386)
        self.dsb_end.setMaximum(999999.999998999992386)
        self.dsb_end.setValue(10.000000000000000)

        self.hl_params.addWidget(self.dsb_end)

        self.l_step = QLabel(FuncToGraphWindow)
        self.l_step.setObjectName(u"l_step")

        self.hl_params.addWidget(self.l_step)

        self.dsb_step = QDoubleSpinBox(FuncToGraphWindow)
        self.dsb_step.setObjectName(u"dsb_step")
        self.dsb_step.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_step.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.dsb_step.setDecimals(6)
        self.dsb_step.setMinimum(0.000001000000000)
        self.dsb_step.setMaximum(999999.999998999992386)
        self.dsb_step.setValue(1.000000000000000)

        self.hl_params.addWidget(self.dsb_step)


        self.gridLayout.addLayout(self.hl_params, 2, 0, 1, 3)

        self.gl_fxs = QGridLayout()
        self.gl_fxs.setObjectName(u"gl_fxs")
        self.pb_sin = QPushButton(FuncToGraphWindow)
        self.pb_sin.setObjectName(u"pb_sin")

        self.gl_fxs.addWidget(self.pb_sin, 3, 1, 1, 1)

        self.pb_pow = QPushButton(FuncToGraphWindow)
        self.pb_pow.setObjectName(u"pb_pow")

        self.gl_fxs.addWidget(self.pb_pow, 2, 1, 1, 1)

        self.pb_sqrt = QPushButton(FuncToGraphWindow)
        self.pb_sqrt.setObjectName(u"pb_sqrt")

        self.gl_fxs.addWidget(self.pb_sqrt, 2, 3, 1, 1)

        self.pb_cos = QPushButton(FuncToGraphWindow)
        self.pb_cos.setObjectName(u"pb_cos")

        self.gl_fxs.addWidget(self.pb_cos, 3, 3, 1, 1)

        self.pb_tan = QPushButton(FuncToGraphWindow)
        self.pb_tan.setObjectName(u"pb_tan")

        self.gl_fxs.addWidget(self.pb_tan, 3, 4, 1, 1)

        self.pb_e = QPushButton(FuncToGraphWindow)
        self.pb_e.setObjectName(u"pb_e")

        self.gl_fxs.addWidget(self.pb_e, 1, 3, 1, 1)

        self.pb_abs = QPushButton(FuncToGraphWindow)
        self.pb_abs.setObjectName(u"pb_abs")

        self.gl_fxs.addWidget(self.pb_abs, 4, 1, 1, 1)

        self.pb_exp = QPushButton(FuncToGraphWindow)
        self.pb_exp.setObjectName(u"pb_exp")

        self.gl_fxs.addWidget(self.pb_exp, 2, 4, 1, 1)

        self.pb_log = QPushButton(FuncToGraphWindow)
        self.pb_log.setObjectName(u"pb_log")

        self.gl_fxs.addWidget(self.pb_log, 4, 3, 1, 1)

        self.pb_log10 = QPushButton(FuncToGraphWindow)
        self.pb_log10.setObjectName(u"pb_log10")

        self.gl_fxs.addWidget(self.pb_log10, 4, 4, 1, 1)

        self.pb_pi = QPushButton(FuncToGraphWindow)
        self.pb_pi.setObjectName(u"pb_pi")

        self.gl_fxs.addWidget(self.pb_pi, 1, 1, 1, 1)

        self.pb_rad = QPushButton(FuncToGraphWindow)
        self.pb_rad.setObjectName(u"pb_rad")

        self.gl_fxs.addWidget(self.pb_rad, 1, 4, 1, 1)


        self.gridLayout.addLayout(self.gl_fxs, 5, 0, 1, 3)

        self.vs = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.vs, 4, 0, 1, 3)

        self.l_invalid = QLabel(FuncToGraphWindow)
        self.l_invalid.setObjectName(u"l_invalid")
        self.l_invalid.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.l_invalid, 3, 0, 1, 4)


        self.retranslateUi(FuncToGraphWindow)

        QMetaObject.connectSlotsByName(FuncToGraphWindow)
    # setupUi

    def retranslateUi(self, FuncToGraphWindow):
        FuncToGraphWindow.setWindowTitle(QCoreApplication.translate("FuncToGraphWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.l_function.setText(QCoreApplication.translate("FuncToGraphWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u044e", None))
        self.l_y.setText(QCoreApplication.translate("FuncToGraphWindow", u"y(x) =", None))
        self.pb_draw.setText(QCoreApplication.translate("FuncToGraphWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.l_start.setText(QCoreApplication.translate("FuncToGraphWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e", None))
        self.l_end.setText(QCoreApplication.translate("FuncToGraphWindow", u"\u041a\u043e\u043d\u0435\u0446", None))
        self.l_step.setText(QCoreApplication.translate("FuncToGraphWindow", u"\u0428\u0430\u0433", None))
        self.pb_sin.setText(QCoreApplication.translate("FuncToGraphWindow", u"sin(x)", None))
        self.pb_pow.setText(QCoreApplication.translate("FuncToGraphWindow", u"pow(x, 2)", None))
        self.pb_sqrt.setText(QCoreApplication.translate("FuncToGraphWindow", u"sqrt(x)", None))
        self.pb_cos.setText(QCoreApplication.translate("FuncToGraphWindow", u"cos(x)", None))
        self.pb_tan.setText(QCoreApplication.translate("FuncToGraphWindow", u"tan(x)", None))
        self.pb_e.setText(QCoreApplication.translate("FuncToGraphWindow", u"e", None))
        self.pb_abs.setText(QCoreApplication.translate("FuncToGraphWindow", u"abs(x)", None))
        self.pb_exp.setText(QCoreApplication.translate("FuncToGraphWindow", u"exp(x)", None))
        self.pb_log.setText(QCoreApplication.translate("FuncToGraphWindow", u"log(x)", None))
        self.pb_log10.setText(QCoreApplication.translate("FuncToGraphWindow", u"log10(x)", None))
        self.pb_pi.setText(QCoreApplication.translate("FuncToGraphWindow", u"pi", None))
        self.pb_rad.setText(QCoreApplication.translate("FuncToGraphWindow", u"(x*pi)/180", None))
        self.l_invalid.setText(QCoreApplication.translate("FuncToGraphWindow", u"\u0414\u0430\u043d\u043d\u0443\u044e \u0444\u0443\u043d\u043a\u0446\u0438\u044e \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e", None))
    # retranslateUi

