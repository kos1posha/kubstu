# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'genetic_algorithm_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_GeneticAlgorithmWindow(object):
    def setupUi(self, GeneticAlgorithmWindow):
        if not GeneticAlgorithmWindow.objectName():
            GeneticAlgorithmWindow.setObjectName(u"GeneticAlgorithmWindow")
        GeneticAlgorithmWindow.resize(666, 437)
        self.gl_main = QGridLayout(GeneticAlgorithmWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.l_plot = QLabel(GeneticAlgorithmWindow)
        self.l_plot.setObjectName(u"l_plot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_plot.sizePolicy().hasHeightForWidth())
        self.l_plot.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.l_plot.setFont(font)

        self.gl_main.addWidget(self.l_plot, 0, 0, 1, 2)

        self.w_plot = QWidget(GeneticAlgorithmWindow)
        self.w_plot.setObjectName(u"w_plot")
        self.w_plot.setMinimumSize(QSize(450, 406))
        self.w_plot.setMaximumSize(QSize(450, 406))
        self.vl_plot = QVBoxLayout(self.w_plot)
        self.vl_plot.setObjectName(u"vl_plot")
        self.vl_plot.setContentsMargins(0, 0, 0, 0)

        self.gl_main.addWidget(self.w_plot, 1, 0, 1, 2)

        self.tabw_sidebar = QTabWidget(GeneticAlgorithmWindow)
        self.tabw_sidebar.setObjectName(u"tabw_sidebar")
        self.tabw_sidebar.setMinimumSize(QSize(200, 425))
        self.tabw_sidebar.setMaximumSize(QSize(200, 425))
        self.tabw_sidebar.setStyleSheet(u"QTabBar {\n"
"     font-size: 12px;\n"
"	font-weight:bold\n"
"}")
        self.tabw_sidebar.setTabPosition(QTabWidget.North)
        self.tab_function = QWidget()
        self.tab_function.setObjectName(u"tab_function")
        self.vl_function = QVBoxLayout(self.tab_function)
        self.vl_function.setObjectName(u"vl_function")
        self.w_function_attrs = QWidget(self.tab_function)
        self.w_function_attrs.setObjectName(u"w_function_attrs")
        sizePolicy.setHeightForWidth(self.w_function_attrs.sizePolicy().hasHeightForWidth())
        self.w_function_attrs.setSizePolicy(sizePolicy)
        self.vl_function_attrs = QVBoxLayout(self.w_function_attrs)
        self.vl_function_attrs.setObjectName(u"vl_function_attrs")
        self.vl_function_attrs.setContentsMargins(0, 0, 0, 0)
        self.l_function = QLabel(self.w_function_attrs)
        self.l_function.setObjectName(u"l_function")
        sizePolicy.setHeightForWidth(self.l_function.sizePolicy().hasHeightForWidth())
        self.l_function.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.l_function.setFont(font1)

        self.vl_function_attrs.addWidget(self.l_function)

        self.le_function = QLineEdit(self.w_function_attrs)
        self.le_function.setObjectName(u"le_function")
        self.le_function.setClearButtonEnabled(True)

        self.vl_function_attrs.addWidget(self.le_function)

        self.l_function_help = QLabel(self.w_function_attrs)
        self.l_function_help.setObjectName(u"l_function_help")
        sizePolicy.setHeightForWidth(self.l_function_help.sizePolicy().hasHeightForWidth())
        self.l_function_help.setSizePolicy(sizePolicy)
        self.l_function_help.setWordWrap(True)

        self.vl_function_attrs.addWidget(self.l_function_help)

        self.l_function_bounds = QLabel(self.w_function_attrs)
        self.l_function_bounds.setObjectName(u"l_function_bounds")
        sizePolicy.setHeightForWidth(self.l_function_bounds.sizePolicy().hasHeightForWidth())
        self.l_function_bounds.setSizePolicy(sizePolicy)
        self.l_function_bounds.setFont(font1)

        self.vl_function_attrs.addWidget(self.l_function_bounds)

        self.w_function_bounds = QWidget(self.w_function_attrs)
        self.w_function_bounds.setObjectName(u"w_function_bounds")
        self.vl_function_bounds = QVBoxLayout(self.w_function_bounds)
        self.vl_function_bounds.setObjectName(u"vl_function_bounds")
        self.vl_function_bounds.setContentsMargins(0, 0, 0, 0)

        self.vl_function_attrs.addWidget(self.w_function_bounds)

        self.pb_apply_function = QPushButton(self.w_function_attrs)
        self.pb_apply_function.setObjectName(u"pb_apply_function")

        self.vl_function_attrs.addWidget(self.pb_apply_function)


        self.vl_function.addWidget(self.w_function_attrs)

        self.vs_function = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_function.addItem(self.vs_function)

        self.tabw_sidebar.addTab(self.tab_function, "")
        self.tab_genetic = QWidget()
        self.tab_genetic.setObjectName(u"tab_genetic")
        self.vl_genetic = QVBoxLayout(self.tab_genetic)
        self.vl_genetic.setObjectName(u"vl_genetic")
        self.w_genetic_attrs = QWidget(self.tab_genetic)
        self.w_genetic_attrs.setObjectName(u"w_genetic_attrs")
        sizePolicy.setHeightForWidth(self.w_genetic_attrs.sizePolicy().hasHeightForWidth())
        self.w_genetic_attrs.setSizePolicy(sizePolicy)
        self.vl_genetic_attrs = QVBoxLayout(self.w_genetic_attrs)
        self.vl_genetic_attrs.setObjectName(u"vl_genetic_attrs")
        self.vl_genetic_attrs.setContentsMargins(0, 0, 0, 0)
        self.l_opt_dir = QLabel(self.w_genetic_attrs)
        self.l_opt_dir.setObjectName(u"l_opt_dir")
        sizePolicy.setHeightForWidth(self.l_opt_dir.sizePolicy().hasHeightForWidth())
        self.l_opt_dir.setSizePolicy(sizePolicy)
        self.l_opt_dir.setFont(font1)

        self.vl_genetic_attrs.addWidget(self.l_opt_dir)

        self.cmb_opt_dir = QComboBox(self.w_genetic_attrs)
        self.cmb_opt_dir.addItem("")
        self.cmb_opt_dir.addItem("")
        self.cmb_opt_dir.setObjectName(u"cmb_opt_dir")

        self.vl_genetic_attrs.addWidget(self.cmb_opt_dir)

        self.l_population_size = QLabel(self.w_genetic_attrs)
        self.l_population_size.setObjectName(u"l_population_size")
        sizePolicy.setHeightForWidth(self.l_population_size.sizePolicy().hasHeightForWidth())
        self.l_population_size.setSizePolicy(sizePolicy)
        self.l_population_size.setFont(font1)

        self.vl_genetic_attrs.addWidget(self.l_population_size)

        self.sb_population_size = QSpinBox(self.w_genetic_attrs)
        self.sb_population_size.setObjectName(u"sb_population_size")
        self.sb_population_size.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sb_population_size.setMinimum(20)
        self.sb_population_size.setMaximum(5000)
        self.sb_population_size.setSingleStep(10)
        self.sb_population_size.setValue(500)

        self.vl_genetic_attrs.addWidget(self.sb_population_size)

        self.l_max_iterations = QLabel(self.w_genetic_attrs)
        self.l_max_iterations.setObjectName(u"l_max_iterations")
        sizePolicy.setHeightForWidth(self.l_max_iterations.sizePolicy().hasHeightForWidth())
        self.l_max_iterations.setSizePolicy(sizePolicy)
        self.l_max_iterations.setFont(font1)

        self.vl_genetic_attrs.addWidget(self.l_max_iterations)

        self.sb_max_iterations = QSpinBox(self.w_genetic_attrs)
        self.sb_max_iterations.setObjectName(u"sb_max_iterations")
        self.sb_max_iterations.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sb_max_iterations.setMinimum(2)
        self.sb_max_iterations.setMaximum(1000)
        self.sb_max_iterations.setSingleStep(5)
        self.sb_max_iterations.setValue(100)

        self.vl_genetic_attrs.addWidget(self.sb_max_iterations)


        self.vl_genetic.addWidget(self.w_genetic_attrs)

        self.pb_start_iter_genetic = QPushButton(self.tab_genetic)
        self.pb_start_iter_genetic.setObjectName(u"pb_start_iter_genetic")
        self.pb_start_iter_genetic.setEnabled(False)

        self.vl_genetic.addWidget(self.pb_start_iter_genetic)

        self.pb_stop_restart_genetic = QPushButton(self.tab_genetic)
        self.pb_stop_restart_genetic.setObjectName(u"pb_stop_restart_genetic")
        self.pb_stop_restart_genetic.setEnabled(False)

        self.vl_genetic.addWidget(self.pb_stop_restart_genetic)

        self.w_iterations = QWidget(self.tab_genetic)
        self.w_iterations.setObjectName(u"w_iterations")
        self.w_iterations.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.w_iterations.sizePolicy().hasHeightForWidth())
        self.w_iterations.setSizePolicy(sizePolicy1)
        self.vl_iterations = QVBoxLayout(self.w_iterations)
        self.vl_iterations.setObjectName(u"vl_iterations")
        self.vl_iterations.setContentsMargins(0, 0, 0, 0)
        self.l_iterations = QLabel(self.w_iterations)
        self.l_iterations.setObjectName(u"l_iterations")
        self.l_iterations.setFont(font1)

        self.vl_iterations.addWidget(self.l_iterations)

        self.tw_iterations = QTableWidget(self.w_iterations)
        if (self.tw_iterations.columnCount() < 2):
            self.tw_iterations.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_iterations.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_iterations.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tw_iterations.setObjectName(u"tw_iterations")
        self.tw_iterations.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_iterations.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_iterations.horizontalHeader().setStretchLastSection(True)
        self.tw_iterations.verticalHeader().setVisible(False)
        self.tw_iterations.verticalHeader().setDefaultSectionSize(18)

        self.vl_iterations.addWidget(self.tw_iterations)


        self.vl_genetic.addWidget(self.w_iterations)

        self.tabw_sidebar.addTab(self.tab_genetic, "")

        self.gl_main.addWidget(self.tabw_sidebar, 0, 2, 2, 1)


        self.retranslateUi(GeneticAlgorithmWindow)

        self.tabw_sidebar.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(GeneticAlgorithmWindow)
    # setupUi

    def retranslateUi(self, GeneticAlgorithmWindow):
        GeneticAlgorithmWindow.setWindowTitle(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u0413\u0435\u043d\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.l_plot.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u041f\u043e\u043f\u0443\u043b\u044f\u0446\u0438\u044f", None))
        self.l_function.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.le_function.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"x * y", None))
        self.l_function_help.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u0414\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435 x \u0438 y", None))
        self.l_function_bounds.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u041e\u0431\u043b\u0430\u0441\u0442\u044c \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.pb_apply_function.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabw_sidebar.setTabText(self.tabw_sidebar.indexOf(self.tab_function), QCoreApplication.translate("GeneticAlgorithmWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.l_opt_dir.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043f\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.cmb_opt_dir.setItemText(0, QCoreApplication.translate("GeneticAlgorithmWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.cmb_opt_dir.setItemText(1, QCoreApplication.translate("GeneticAlgorithmWindow", u"\u041c\u0438\u043d\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f", None))

        self.l_population_size.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u043e\u043f\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.l_max_iterations.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0439", None))
        self.pb_start_iter_genetic.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.pb_stop_restart_genetic.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.l_iterations.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u0418\u0442\u0435\u0440\u0430\u0446\u0438\u0438", None))
        ___qtablewidgetitem = self.tw_iterations.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"#", None));
        ___qtablewidgetitem1 = self.tw_iterations.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("GeneticAlgorithmWindow", u"\u0420\u0430\u0437\u0431\u0440\u043e\u0441", None));
        self.tabw_sidebar.setTabText(self.tabw_sidebar.indexOf(self.tab_genetic), QCoreApplication.translate("GeneticAlgorithmWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
    # retranslateUi

