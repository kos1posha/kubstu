# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_ClfWindow(object):
    def setupUi(self, ClfWindow):
        if not ClfWindow.objectName():
            ClfWindow.setObjectName(u"ClfWindow")
        ClfWindow.resize(700, 520)
        ClfWindow.setMinimumSize(QSize(700, 520))
        icon = QIcon()
        icon.addFile(u":/icon/clf.ico", QSize(), QIcon.Normal, QIcon.Off)
        ClfWindow.setWindowIcon(icon)
        self.w_main = QWidget(ClfWindow)
        self.w_main.setObjectName(u"w_main")
        self.gridLayout = QGridLayout(self.w_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_clf_parameters = QGroupBox(self.w_main)
        self.gb_clf_parameters.setObjectName(u"gb_clf_parameters")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_clf_parameters.sizePolicy().hasHeightForWidth())
        self.gb_clf_parameters.setSizePolicy(sizePolicy)
        self.vl_clf_parameters = QVBoxLayout(self.gb_clf_parameters)
        self.vl_clf_parameters.setSpacing(4)
        self.vl_clf_parameters.setObjectName(u"vl_clf_parameters")
        self.vl_clf_parameters.setContentsMargins(4, 4, 4, 6)
        self.l_criterion = QLabel(self.gb_clf_parameters)
        self.l_criterion.setObjectName(u"l_criterion")
        self.l_criterion.setTextFormat(Qt.AutoText)
        self.l_criterion.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.l_criterion.setWordWrap(True)

        self.vl_clf_parameters.addWidget(self.l_criterion)

        self.cb_criterion = QComboBox(self.gb_clf_parameters)
        self.cb_criterion.setObjectName(u"cb_criterion")

        self.vl_clf_parameters.addWidget(self.cb_criterion)

        self.l_splitter = QLabel(self.gb_clf_parameters)
        self.l_splitter.setObjectName(u"l_splitter")
        self.l_splitter.setTextFormat(Qt.AutoText)
        self.l_splitter.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.l_splitter.setWordWrap(True)

        self.vl_clf_parameters.addWidget(self.l_splitter)

        self.cb_splitter = QComboBox(self.gb_clf_parameters)
        self.cb_splitter.setObjectName(u"cb_splitter")

        self.vl_clf_parameters.addWidget(self.cb_splitter)

        self.l_max_depth = QLabel(self.gb_clf_parameters)
        self.l_max_depth.setObjectName(u"l_max_depth")
        self.l_max_depth.setTextFormat(Qt.AutoText)
        self.l_max_depth.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.l_max_depth.setWordWrap(True)

        self.vl_clf_parameters.addWidget(self.l_max_depth)

        self.le_max_depth = QLineEdit(self.gb_clf_parameters)
        self.le_max_depth.setObjectName(u"le_max_depth")

        self.vl_clf_parameters.addWidget(self.le_max_depth)

        self.l_min_samples_split = QLabel(self.gb_clf_parameters)
        self.l_min_samples_split.setObjectName(u"l_min_samples_split")
        self.l_min_samples_split.setTextFormat(Qt.AutoText)
        self.l_min_samples_split.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.l_min_samples_split.setWordWrap(True)

        self.vl_clf_parameters.addWidget(self.l_min_samples_split)

        self.le_min_samples_split = QLineEdit(self.gb_clf_parameters)
        self.le_min_samples_split.setObjectName(u"le_min_samples_split")

        self.vl_clf_parameters.addWidget(self.le_min_samples_split)

        self.l_min_samples_leaf = QLabel(self.gb_clf_parameters)
        self.l_min_samples_leaf.setObjectName(u"l_min_samples_leaf")
        self.l_min_samples_leaf.setTextFormat(Qt.AutoText)
        self.l_min_samples_leaf.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.l_min_samples_leaf.setWordWrap(True)

        self.vl_clf_parameters.addWidget(self.l_min_samples_leaf)

        self.le_min_samples_leaf = QLineEdit(self.gb_clf_parameters)
        self.le_min_samples_leaf.setObjectName(u"le_min_samples_leaf")

        self.vl_clf_parameters.addWidget(self.le_min_samples_leaf)

        self.l_max_features = QLabel(self.gb_clf_parameters)
        self.l_max_features.setObjectName(u"l_max_features")
        self.l_max_features.setTextFormat(Qt.AutoText)
        self.l_max_features.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.l_max_features.setWordWrap(True)

        self.vl_clf_parameters.addWidget(self.l_max_features)

        self.le_max_features = QLineEdit(self.gb_clf_parameters)
        self.le_max_features.setObjectName(u"le_max_features")

        self.vl_clf_parameters.addWidget(self.le_max_features)

        self.l_max_leaf_nodes = QLabel(self.gb_clf_parameters)
        self.l_max_leaf_nodes.setObjectName(u"l_max_leaf_nodes")
        self.l_max_leaf_nodes.setTextFormat(Qt.AutoText)
        self.l_max_leaf_nodes.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.l_max_leaf_nodes.setWordWrap(True)

        self.vl_clf_parameters.addWidget(self.l_max_leaf_nodes)

        self.le_max_leaf_nodes = QLineEdit(self.gb_clf_parameters)
        self.le_max_leaf_nodes.setObjectName(u"le_max_leaf_nodes")

        self.vl_clf_parameters.addWidget(self.le_max_leaf_nodes)

        self.l_random_state = QLabel(self.gb_clf_parameters)
        self.l_random_state.setObjectName(u"l_random_state")
        self.l_random_state.setTextFormat(Qt.AutoText)
        self.l_random_state.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.l_random_state.setWordWrap(True)

        self.vl_clf_parameters.addWidget(self.l_random_state)

        self.le_random_state = QLineEdit(self.gb_clf_parameters)
        self.le_random_state.setObjectName(u"le_random_state")

        self.vl_clf_parameters.addWidget(self.le_random_state)


        self.gridLayout.addWidget(self.gb_clf_parameters, 0, 1, 3, 1)

        self.l_dataset = QLabel(self.w_main)
        self.l_dataset.setObjectName(u"l_dataset")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_dataset.sizePolicy().hasHeightForWidth())
        self.l_dataset.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.l_dataset, 0, 0, 1, 1)

        self.cb_dataset = QComboBox(self.w_main)
        self.cb_dataset.setObjectName(u"cb_dataset")

        self.gridLayout.addWidget(self.cb_dataset, 1, 0, 1, 1)

        self.pb_fit_and_plot_tree = QPushButton(self.w_main)
        self.pb_fit_and_plot_tree.setObjectName(u"pb_fit_and_plot_tree")

        self.gridLayout.addWidget(self.pb_fit_and_plot_tree, 3, 1, 1, 1)

        self.pb_show_digits_image = QPushButton(self.w_main)
        self.pb_show_digits_image.setObjectName(u"pb_show_digits_image")
        self.pb_show_digits_image.setEnabled(False)

        self.gridLayout.addWidget(self.pb_show_digits_image, 4, 1, 1, 1)

        self.vs_clf_params = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.vs_clf_params, 5, 1, 1, 1)

        self.tw_dataset = QTableWidget(self.w_main)
        self.tw_dataset.setObjectName(u"tw_dataset")
        self.tw_dataset.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_dataset.setTabKeyNavigation(False)
        self.tw_dataset.setProperty("showDropIndicator", False)
        self.tw_dataset.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_dataset.setSortingEnabled(True)
        self.tw_dataset.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout.addWidget(self.tw_dataset, 2, 0, 4, 1)

        ClfWindow.setCentralWidget(self.w_main)

        self.retranslateUi(ClfWindow)

        self.cb_criterion.setCurrentIndex(-1)
        self.cb_dataset.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(ClfWindow)
    # setupUi

    def retranslateUi(self, ClfWindow):
        ClfWindow.setWindowTitle(QCoreApplication.translate("ClfWindow", u"\u0414\u0435\u0440\u0435\u0432\u044c\u044f \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.gb_clf_parameters.setTitle(QCoreApplication.translate("ClfWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u0435\u0440\u0435\u0432\u0430 \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.l_criterion.setText(QCoreApplication.translate("ClfWindow", u"\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430 \u0440\u0430\u0437\u0431\u0438\u0435\u043d\u0438\u044f", None))
        self.l_splitter.setText(QCoreApplication.translate("ClfWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u0440\u0430\u0437\u0431\u0438\u0435\u043d\u0438\u044f", None))
        self.l_max_depth.setText(QCoreApplication.translate("ClfWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0433\u043b\u0443\u0431\u0438\u043d\u0430 [1; +\u221e)", None))
        self.le_max_depth.setPlaceholderText(QCoreApplication.translate("ClfWindow", u"\u041d\u0435 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0430", None))
        self.l_min_samples_split.setText(QCoreApplication.translate("ClfWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0434\u043b\u044f \u0440\u0430\u0437\u0431\u0438\u0435\u043d\u0438\u044f [2; +\u221e)", None))
        self.le_min_samples_split.setPlaceholderText(QCoreApplication.translate("ClfWindow", u"2", None))
        self.l_min_samples_leaf.setText(QCoreApplication.translate("ClfWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u0432 \u043b\u0438\u0441\u0442\u0435 [1; +\u221e)", None))
        self.le_min_samples_leaf.setPlaceholderText(QCoreApplication.translate("ClfWindow", u"1", None))
        self.l_max_features.setText(QCoreApplication.translate("ClfWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0438\u0437\u043d\u0430\u043a\u043e\u0432 \u0434\u043b\u044f \u0440\u0430\u0437\u0431\u0438\u0435\u043d\u0438\u044f [1; +\u221e)", None))
        self.le_max_features.setPlaceholderText(QCoreApplication.translate("ClfWindow", u"\u041d\u0435 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043e", None))
        self.l_max_leaf_nodes.setText(QCoreApplication.translate("ClfWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0443\u0437\u043b\u043e\u0432 [2; +\u221e)", None))
        self.le_max_leaf_nodes.setPlaceholderText(QCoreApplication.translate("ClfWindow", u"\u041d\u0435 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043e", None))
        self.l_random_state.setText(QCoreApplication.translate("ClfWindow", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u0435 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 [0; +\u221e)", None))
        self.le_random_state.setPlaceholderText(QCoreApplication.translate("ClfWindow", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.l_dataset.setText(QCoreApplication.translate("ClfWindow", u"\u0414\u0430\u0442\u0430\u0441\u0435\u0442 (\u0432\u044b\u0431\u043e\u0440\u043a\u0430)", None))
        self.pb_fit_and_plot_tree.setText(QCoreApplication.translate("ClfWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0434\u0435\u0440\u0435\u0432\u043e", None))
        self.pb_show_digits_image.setText(QCoreApplication.translate("ClfWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

