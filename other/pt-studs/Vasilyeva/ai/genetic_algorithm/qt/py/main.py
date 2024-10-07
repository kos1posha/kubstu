# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_GeneticAlgorithmForm(object):
    def setupUi(self, GeneticAlgorithmForm):
        if not GeneticAlgorithmForm.objectName():
            GeneticAlgorithmForm.setObjectName(u"GeneticAlgorithmForm")
        GeneticAlgorithmForm.resize(222, 306)
        self.gl_main = QGridLayout(GeneticAlgorithmForm)
        self.gl_main.setObjectName(u"gl_main")
        self.l_function = QLabel(GeneticAlgorithmForm)
        self.l_function.setObjectName(u"l_function")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_function.sizePolicy().hasHeightForWidth())
        self.l_function.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.l_function.setFont(font)

        self.gl_main.addWidget(self.l_function, 0, 0, 1, 2)

        self.le_function = QLineEdit(GeneticAlgorithmForm)
        self.le_function.setObjectName(u"le_function")

        self.gl_main.addWidget(self.le_function, 1, 0, 1, 2)

        self.pb_start = QPushButton(GeneticAlgorithmForm)
        self.pb_start.setObjectName(u"pb_start")

        self.gl_main.addWidget(self.pb_start, 15, 0, 1, 2)

        self.cmb_opt_dir = QComboBox(GeneticAlgorithmForm)
        self.cmb_opt_dir.addItem("")
        self.cmb_opt_dir.addItem("")
        self.cmb_opt_dir.setObjectName(u"cmb_opt_dir")

        self.gl_main.addWidget(self.cmb_opt_dir, 10, 0, 1, 2)

        self.sb_population_size = QSpinBox(GeneticAlgorithmForm)
        self.sb_population_size.setObjectName(u"sb_population_size")
        self.sb_population_size.setMinimum(4)
        self.sb_population_size.setMaximum(1000)
        self.sb_population_size.setValue(100)

        self.gl_main.addWidget(self.sb_population_size, 13, 0, 1, 2)

        self.dsb_xmin = QDoubleSpinBox(GeneticAlgorithmForm)
        self.dsb_xmin.setObjectName(u"dsb_xmin")
        self.dsb_xmin.setAlignment(Qt.AlignCenter)
        self.dsb_xmin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_xmin.setDecimals(2)
        self.dsb_xmin.setMinimum(-9999999999999999464902769475481793196872414789632.000000000000000)
        self.dsb_xmin.setMaximum(1000000000000000048346692115553659057528394845890514255872.000000000000000)
        self.dsb_xmin.setValue(-5.000000000000000)

        self.gl_main.addWidget(self.dsb_xmin, 5, 0, 1, 1)

        self.dsb_xmax = QDoubleSpinBox(GeneticAlgorithmForm)
        self.dsb_xmax.setObjectName(u"dsb_xmax")
        self.dsb_xmax.setAlignment(Qt.AlignCenter)
        self.dsb_xmax.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_xmax.setDecimals(2)
        self.dsb_xmax.setMinimum(-9999999999999999464902769475481793196872414789632.000000000000000)
        self.dsb_xmax.setMaximum(1000000000000000048346692115553659057528394845890514255872.000000000000000)
        self.dsb_xmax.setValue(5.000000000000000)

        self.gl_main.addWidget(self.dsb_xmax, 5, 1, 1, 1)

        self.dsb_ymin = QDoubleSpinBox(GeneticAlgorithmForm)
        self.dsb_ymin.setObjectName(u"dsb_ymin")
        self.dsb_ymin.setAlignment(Qt.AlignCenter)
        self.dsb_ymin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_ymin.setDecimals(2)
        self.dsb_ymin.setMinimum(-9999999999999999464902769475481793196872414789632.000000000000000)
        self.dsb_ymin.setMaximum(1000000000000000048346692115553659057528394845890514255872.000000000000000)
        self.dsb_ymin.setValue(-5.000000000000000)

        self.gl_main.addWidget(self.dsb_ymin, 7, 0, 1, 1)

        self.dsb_ymax = QDoubleSpinBox(GeneticAlgorithmForm)
        self.dsb_ymax.setObjectName(u"dsb_ymax")
        self.dsb_ymax.setAlignment(Qt.AlignCenter)
        self.dsb_ymax.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_ymax.setDecimals(2)
        self.dsb_ymax.setMinimum(-9999999999999999464902769475481793196872414789632.000000000000000)
        self.dsb_ymax.setMaximum(1000000000000000048346692115553659057528394845890514255872.000000000000000)
        self.dsb_ymax.setValue(5.000000000000000)

        self.gl_main.addWidget(self.dsb_ymax, 7, 1, 1, 1)

        self.l_xlim = QLabel(GeneticAlgorithmForm)
        self.l_xlim.setObjectName(u"l_xlim")
        sizePolicy.setHeightForWidth(self.l_xlim.sizePolicy().hasHeightForWidth())
        self.l_xlim.setSizePolicy(sizePolicy)
        self.l_xlim.setFont(font)

        self.gl_main.addWidget(self.l_xlim, 4, 0, 1, 2)

        self.l_ylim = QLabel(GeneticAlgorithmForm)
        self.l_ylim.setObjectName(u"l_ylim")
        sizePolicy.setHeightForWidth(self.l_ylim.sizePolicy().hasHeightForWidth())
        self.l_ylim.setSizePolicy(sizePolicy)
        self.l_ylim.setFont(font)

        self.gl_main.addWidget(self.l_ylim, 6, 0, 1, 2)

        self.l_opt_dir = QLabel(GeneticAlgorithmForm)
        self.l_opt_dir.setObjectName(u"l_opt_dir")
        sizePolicy.setHeightForWidth(self.l_opt_dir.sizePolicy().hasHeightForWidth())
        self.l_opt_dir.setSizePolicy(sizePolicy)
        self.l_opt_dir.setFont(font)

        self.gl_main.addWidget(self.l_opt_dir, 9, 0, 1, 2)

        self.l_population_size = QLabel(GeneticAlgorithmForm)
        self.l_population_size.setObjectName(u"l_population_size")
        sizePolicy.setHeightForWidth(self.l_population_size.sizePolicy().hasHeightForWidth())
        self.l_population_size.setSizePolicy(sizePolicy)
        self.l_population_size.setFont(font)

        self.gl_main.addWidget(self.l_population_size, 12, 0, 1, 2)

        self.pb_check = QPushButton(GeneticAlgorithmForm)
        self.pb_check.setObjectName(u"pb_check")

        self.gl_main.addWidget(self.pb_check, 3, 0, 1, 2)

        self.l_function_helptext = QLabel(GeneticAlgorithmForm)
        self.l_function_helptext.setObjectName(u"l_function_helptext")
        self.l_function_helptext.setStyleSheet(u"color:grey")
        self.l_function_helptext.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.l_function_helptext, 2, 0, 1, 2)

        self.l_lims_helptext = QLabel(GeneticAlgorithmForm)
        self.l_lims_helptext.setObjectName(u"l_lims_helptext")
        self.l_lims_helptext.setStyleSheet(u"color:grey")
        self.l_lims_helptext.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.l_lims_helptext, 8, 0, 1, 2)

        self.l_opt_dir_helptext = QLabel(GeneticAlgorithmForm)
        self.l_opt_dir_helptext.setObjectName(u"l_opt_dir_helptext")
        self.l_opt_dir_helptext.setStyleSheet(u"color:grey")
        self.l_opt_dir_helptext.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.l_opt_dir_helptext, 11, 0, 1, 2)

        self.l_population_size_helptext = QLabel(GeneticAlgorithmForm)
        self.l_population_size_helptext.setObjectName(u"l_population_size_helptext")
        self.l_population_size_helptext.setStyleSheet(u"color:grey")
        self.l_population_size_helptext.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.l_population_size_helptext, 14, 0, 1, 2)


        self.retranslateUi(GeneticAlgorithmForm)

        QMetaObject.connectSlotsByName(GeneticAlgorithmForm)
    # setupUi

    def retranslateUi(self, GeneticAlgorithmForm):
        GeneticAlgorithmForm.setWindowTitle(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0414\u0430\u043d\u043e", None))
        self.l_function.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u044e \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.le_function.setPlaceholderText(QCoreApplication.translate("GeneticAlgorithmForm", u"f(x, y)", None))
        self.pb_start.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.cmb_opt_dir.setItemText(0, QCoreApplication.translate("GeneticAlgorithmForm", u"\u043c\u0430\u043a\u0441\u0438\u043c\u0443\u043c\u0430", None))
        self.cmb_opt_dir.setItemText(1, QCoreApplication.translate("GeneticAlgorithmForm", u"\u043c\u0438\u043d\u0438\u043c\u0443\u043c\u0430", None))

        self.l_xlim.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d x", None))
        self.l_ylim.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d y", None))
        self.l_opt_dir.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.l_population_size.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0445\u0440\u043e\u043c\u043e\u0441\u043e\u043c", None))
        self.pb_check.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.l_function_helptext.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f \u0434\u043e\u043b\u0436\u043d\u0430 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442\u044c \u0438 x, \u0438 y, \u0442\u0430\u043a \u043a\u0430\u043a \u0432 \u0442\u0430\u043a\u043e\u043c\n"
"\u0432\u0438\u0434\u0435 \u0435\u0435 \u043c\u043e\u0436\u043d\u043e \u0443\u0434\u043e\u0431\u043d\u043e \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.l_lims_helptext.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0438\u0432\u0430\u044e\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 x \u0438 y", None))
        self.l_opt_dir_helptext.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0418\u0441\u043a\u043e\u043c\u044b\u0439 \u044d\u043a\u0441\u0442\u0440\u0435\u043c\u0443\u043c", None))
        self.l_population_size_helptext.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u043e\u043f\u0443\u043b\u044f\u0446\u0438\u0438 \u0445\u0440\u043e\u043c\u043e\u0441\u043e\u043c \u0433\u0435\u043d\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430", None))
    # retranslateUi

