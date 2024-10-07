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
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_GeneticAlgorithmForm(object):
    def setupUi(self, GeneticAlgorithmForm):
        if not GeneticAlgorithmForm.objectName():
            GeneticAlgorithmForm.setObjectName(u"GeneticAlgorithmForm")
        GeneticAlgorithmForm.resize(617, 429)
        self.gridLayout = QGridLayout(GeneticAlgorithmForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_start = QPushButton(GeneticAlgorithmForm)
        self.pb_start.setObjectName(u"pb_start")

        self.gridLayout.addWidget(self.pb_start, 13, 0, 1, 2)

        self.le_function = QLineEdit(GeneticAlgorithmForm)
        self.le_function.setObjectName(u"le_function")

        self.gridLayout.addWidget(self.le_function, 1, 0, 1, 2)

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

        self.gridLayout.addWidget(self.l_function, 0, 0, 1, 2)

        self.gl_lims = QGridLayout()
        self.gl_lims.setObjectName(u"gl_lims")
        self.gl_lims.setHorizontalSpacing(0)
        self.gl_lims.setVerticalSpacing(6)
        self.dsb_xmin = QDoubleSpinBox(GeneticAlgorithmForm)
        self.dsb_xmin.setObjectName(u"dsb_xmin")
        self.dsb_xmin.setMaximumSize(QSize(80, 16777215))
        self.dsb_xmin.setAlignment(Qt.AlignCenter)
        self.dsb_xmin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_xmin.setDecimals(2)
        self.dsb_xmin.setMinimum(-9999999999999999464902769475481793196872414789632.000000000000000)
        self.dsb_xmin.setMaximum(1000000000000000048346692115553659057528394845890514255872.000000000000000)
        self.dsb_xmin.setValue(-10.000000000000000)

        self.gl_lims.addWidget(self.dsb_xmin, 0, 1, 1, 1)

        self.l_ylim_2 = QLabel(GeneticAlgorithmForm)
        self.l_ylim_2.setObjectName(u"l_ylim_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_ylim_2.sizePolicy().hasHeightForWidth())
        self.l_ylim_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.l_ylim_2.setFont(font1)

        self.gl_lims.addWidget(self.l_ylim_2, 1, 2, 1, 1)

        self.l_xlim_2 = QLabel(GeneticAlgorithmForm)
        self.l_xlim_2.setObjectName(u"l_xlim_2")
        sizePolicy1.setHeightForWidth(self.l_xlim_2.sizePolicy().hasHeightForWidth())
        self.l_xlim_2.setSizePolicy(sizePolicy1)
        self.l_xlim_2.setFont(font1)

        self.gl_lims.addWidget(self.l_xlim_2, 0, 2, 1, 1)

        self.dsb_ymax = QDoubleSpinBox(GeneticAlgorithmForm)
        self.dsb_ymax.setObjectName(u"dsb_ymax")
        self.dsb_ymax.setMaximumSize(QSize(80, 16777215))
        self.dsb_ymax.setAlignment(Qt.AlignCenter)
        self.dsb_ymax.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_ymax.setDecimals(2)
        self.dsb_ymax.setMinimum(-9999999999999999464902769475481793196872414789632.000000000000000)
        self.dsb_ymax.setMaximum(1000000000000000048346692115553659057528394845890514255872.000000000000000)
        self.dsb_ymax.setValue(10.000000000000000)

        self.gl_lims.addWidget(self.dsb_ymax, 1, 3, 1, 1)

        self.l_xlim_1 = QLabel(GeneticAlgorithmForm)
        self.l_xlim_1.setObjectName(u"l_xlim_1")
        sizePolicy1.setHeightForWidth(self.l_xlim_1.sizePolicy().hasHeightForWidth())
        self.l_xlim_1.setSizePolicy(sizePolicy1)
        self.l_xlim_1.setFont(font1)

        self.gl_lims.addWidget(self.l_xlim_1, 0, 0, 1, 1)

        self.l_ylim_3 = QLabel(GeneticAlgorithmForm)
        self.l_ylim_3.setObjectName(u"l_ylim_3")
        sizePolicy1.setHeightForWidth(self.l_ylim_3.sizePolicy().hasHeightForWidth())
        self.l_ylim_3.setSizePolicy(sizePolicy1)
        self.l_ylim_3.setFont(font1)
        self.l_ylim_3.setFrameShadow(QFrame.Raised)

        self.gl_lims.addWidget(self.l_ylim_3, 1, 4, 1, 1)

        self.l_xlim_3 = QLabel(GeneticAlgorithmForm)
        self.l_xlim_3.setObjectName(u"l_xlim_3")
        sizePolicy1.setHeightForWidth(self.l_xlim_3.sizePolicy().hasHeightForWidth())
        self.l_xlim_3.setSizePolicy(sizePolicy1)
        self.l_xlim_3.setFont(font1)

        self.gl_lims.addWidget(self.l_xlim_3, 0, 4, 1, 1)

        self.dsb_ymin = QDoubleSpinBox(GeneticAlgorithmForm)
        self.dsb_ymin.setObjectName(u"dsb_ymin")
        self.dsb_ymin.setMaximumSize(QSize(80, 16777215))
        self.dsb_ymin.setAlignment(Qt.AlignCenter)
        self.dsb_ymin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_ymin.setDecimals(2)
        self.dsb_ymin.setMinimum(-9999999999999999464902769475481793196872414789632.000000000000000)
        self.dsb_ymin.setMaximum(1000000000000000048346692115553659057528394845890514255872.000000000000000)
        self.dsb_ymin.setValue(-10.000000000000000)

        self.gl_lims.addWidget(self.dsb_ymin, 1, 1, 1, 1)

        self.dsb_xmax = QDoubleSpinBox(GeneticAlgorithmForm)
        self.dsb_xmax.setObjectName(u"dsb_xmax")
        self.dsb_xmax.setMaximumSize(QSize(80, 16777215))
        self.dsb_xmax.setAlignment(Qt.AlignCenter)
        self.dsb_xmax.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_xmax.setDecimals(2)
        self.dsb_xmax.setMinimum(-9999999999999999464902769475481793196872414789632.000000000000000)
        self.dsb_xmax.setMaximum(1000000000000000048346692115553659057528394845890514255872.000000000000000)
        self.dsb_xmax.setValue(10.000000000000000)

        self.gl_lims.addWidget(self.dsb_xmax, 0, 3, 1, 1)

        self.l_ylim_1 = QLabel(GeneticAlgorithmForm)
        self.l_ylim_1.setObjectName(u"l_ylim_1")
        sizePolicy1.setHeightForWidth(self.l_ylim_1.sizePolicy().hasHeightForWidth())
        self.l_ylim_1.setSizePolicy(sizePolicy1)
        self.l_ylim_1.setFont(font1)

        self.gl_lims.addWidget(self.l_ylim_1, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gl_lims, 2, 0, 1, 2)

        self.cmb_opt_dir = QComboBox(GeneticAlgorithmForm)
        self.cmb_opt_dir.addItem("")
        self.cmb_opt_dir.addItem("")
        self.cmb_opt_dir.setObjectName(u"cmb_opt_dir")

        self.gridLayout.addWidget(self.cmb_opt_dir, 4, 0, 1, 2)

        self.l_opt_dir = QLabel(GeneticAlgorithmForm)
        self.l_opt_dir.setObjectName(u"l_opt_dir")

        self.gridLayout.addWidget(self.l_opt_dir, 3, 0, 1, 2)

        self.sb_max_iteration = QSpinBox(GeneticAlgorithmForm)
        self.sb_max_iteration.setObjectName(u"sb_max_iteration")
        self.sb_max_iteration.setMinimum(2)
        self.sb_max_iteration.setMaximum(1000)
        self.sb_max_iteration.setValue(20)

        self.gridLayout.addWidget(self.sb_max_iteration, 12, 0, 1, 2)

        self.pb_next_iter = QPushButton(GeneticAlgorithmForm)
        self.pb_next_iter.setObjectName(u"pb_next_iter")
        self.pb_next_iter.setEnabled(False)

        self.gridLayout.addWidget(self.pb_next_iter, 14, 0, 1, 2)

        self.vl_population = QVBoxLayout()
        self.vl_population.setObjectName(u"vl_population")
        self.l_plot = QLabel(GeneticAlgorithmForm)
        self.l_plot.setObjectName(u"l_plot")
        sizePolicy.setHeightForWidth(self.l_plot.sizePolicy().hasHeightForWidth())
        self.l_plot.setSizePolicy(sizePolicy)
        self.l_plot.setFont(font)

        self.vl_population.addWidget(self.l_plot)

        self.f_plot = QFrame(GeneticAlgorithmForm)
        self.f_plot.setObjectName(u"f_plot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.f_plot.sizePolicy().hasHeightForWidth())
        self.f_plot.setSizePolicy(sizePolicy2)
        self.f_plot.setMinimumSize(QSize(400, 400))
        self.f_plot.setMaximumSize(QSize(400, 400))
        self.f_plot.setFrameShape(QFrame.StyledPanel)
        self.f_plot.setFrameShadow(QFrame.Sunken)
        self.vl_plot = QVBoxLayout(self.f_plot)
        self.vl_plot.setObjectName(u"vl_plot")
        self.vl_plot.setContentsMargins(0, 0, 0, 0)
        self.l_plot_placeholder = QLabel(self.f_plot)
        self.l_plot_placeholder.setObjectName(u"l_plot_placeholder")
        self.l_plot_placeholder.setStyleSheet(u"color:gray")
        self.l_plot_placeholder.setFrameShape(QFrame.NoFrame)
        self.l_plot_placeholder.setFrameShadow(QFrame.Sunken)
        self.l_plot_placeholder.setAlignment(Qt.AlignCenter)

        self.vl_plot.addWidget(self.l_plot_placeholder)


        self.vl_population.addWidget(self.f_plot)


        self.gridLayout.addLayout(self.vl_population, 0, 2, 15, 1)

        self.l_population_size = QLabel(GeneticAlgorithmForm)
        self.l_population_size.setObjectName(u"l_population_size")

        self.gridLayout.addWidget(self.l_population_size, 9, 0, 1, 2)

        self.sb_population_size = QSpinBox(GeneticAlgorithmForm)
        self.sb_population_size.setObjectName(u"sb_population_size")
        self.sb_population_size.setMinimum(4)
        self.sb_population_size.setMaximum(1000)
        self.sb_population_size.setValue(100)

        self.gridLayout.addWidget(self.sb_population_size, 10, 0, 1, 2)

        self.l_max_iteration = QLabel(GeneticAlgorithmForm)
        self.l_max_iteration.setObjectName(u"l_max_iteration")

        self.gridLayout.addWidget(self.l_max_iteration, 11, 0, 1, 2)

        self.vs = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.vs, 6, 0, 1, 2)


        self.retranslateUi(GeneticAlgorithmForm)

        QMetaObject.connectSlotsByName(GeneticAlgorithmForm)
    # setupUi

    def retranslateUi(self, GeneticAlgorithmForm):
        GeneticAlgorithmForm.setWindowTitle(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0413\u0435\u043d\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.pb_start.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.le_function.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"34 * x ** 2 + 5 * y", None))
        self.l_function.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f (x, y)", None))
        self.l_ylim_2.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"; ", None))
        self.l_xlim_2.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"; ", None))
        self.l_xlim_1.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"x \u2208 [", None))
        self.l_ylim_3.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"]", None))
        self.l_xlim_3.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"]", None))
        self.l_ylim_1.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"y \u2208 [", None))
        self.cmb_opt_dir.setItemText(0, QCoreApplication.translate("GeneticAlgorithmForm", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.cmb_opt_dir.setItemText(1, QCoreApplication.translate("GeneticAlgorithmForm", u"\u041c\u0438\u043d\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f", None))

        self.l_opt_dir.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.pb_next_iter.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0430\u044f \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.l_plot.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u041f\u043e\u043f\u0443\u043b\u044f\u0446\u0438\u044f", None))
        self.l_plot_placeholder.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0418\u043d\u0438\u0446\u0438\u0438\u0440\u0443\u0439\u0442\u0435 \u0437\u0430\u043f\u0443\u0441\u043a \u043c\u0435\u0442\u043e\u0434\u0430, \n"
"\u0447\u0442\u043e\u0431\u044b \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u043f\u0443\u043b\u044f\u0446\u0438\u044e", None))
        self.l_population_size.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u043e\u043f\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.l_max_iteration.setText(QCoreApplication.translate("GeneticAlgorithmForm", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043a\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0439", None))
    # retranslateUi

