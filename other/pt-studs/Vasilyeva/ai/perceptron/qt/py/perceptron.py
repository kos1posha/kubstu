# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perceptron.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolButton, QWidget)

class Ui_PerceptronWindow(object):
    def setupUi(self, PerceptronWindow):
        if not PerceptronWindow.objectName():
            PerceptronWindow.setObjectName(u"PerceptronWindow")
        PerceptronWindow.resize(600, 350)
        PerceptronWindow.setMinimumSize(QSize(600, 350))
        PerceptronWindow.setMaximumSize(QSize(471, 286))
        self.gl_main = QGridLayout(PerceptronWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.pb_choose_file = QPushButton(PerceptronWindow)
        self.pb_choose_file.setObjectName(u"pb_choose_file")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_choose_file.sizePolicy().hasHeightForWidth())
        self.pb_choose_file.setSizePolicy(sizePolicy)

        self.gl_main.addWidget(self.pb_choose_file, 2, 3, 1, 1)

        self.pb_predict = QPushButton(PerceptronWindow)
        self.pb_predict.setObjectName(u"pb_predict")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_predict.sizePolicy().hasHeightForWidth())
        self.pb_predict.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.pb_predict, 3, 2, 1, 2)

        self.tw_train_data = QTableWidget(PerceptronWindow)
        if (self.tw_train_data.columnCount() < 2):
            self.tw_train_data.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_train_data.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_train_data.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tw_train_data.setObjectName(u"tw_train_data")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tw_train_data.sizePolicy().hasHeightForWidth())
        self.tw_train_data.setSizePolicy(sizePolicy2)
        self.tw_train_data.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_train_data.horizontalHeader().setStretchLastSection(True)
        self.tw_train_data.verticalHeader().setVisible(False)

        self.gl_main.addWidget(self.tw_train_data, 1, 0, 1, 2)

        self.le_neurons = QLineEdit(PerceptronWindow)
        self.le_neurons.setObjectName(u"le_neurons")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.le_neurons.sizePolicy().hasHeightForWidth())
        self.le_neurons.setSizePolicy(sizePolicy3)

        self.gl_main.addWidget(self.le_neurons, 2, 0, 1, 1)

        self.hl_perceptron_output_header = QHBoxLayout()
        self.hl_perceptron_output_header.setObjectName(u"hl_perceptron_output_header")
        self.l_perceptron_output = QLabel(PerceptronWindow)
        self.l_perceptron_output.setObjectName(u"l_perceptron_output")

        self.hl_perceptron_output_header.addWidget(self.l_perceptron_output)

        self.cb_only_1 = QCheckBox(PerceptronWindow)
        self.cb_only_1.setObjectName(u"cb_only_1")
        sizePolicy.setHeightForWidth(self.cb_only_1.sizePolicy().hasHeightForWidth())
        self.cb_only_1.setSizePolicy(sizePolicy)

        self.hl_perceptron_output_header.addWidget(self.cb_only_1)


        self.gl_main.addLayout(self.hl_perceptron_output_header, 0, 2, 1, 2)

        self.hl_train_data_header = QHBoxLayout()
        self.hl_train_data_header.setObjectName(u"hl_train_data_header")
        self.l_train_data = QLabel(PerceptronWindow)
        self.l_train_data.setObjectName(u"l_train_data")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.l_train_data.sizePolicy().hasHeightForWidth())
        self.l_train_data.setSizePolicy(sizePolicy4)

        self.hl_train_data_header.addWidget(self.l_train_data)

        self.pb_add_td = QToolButton(PerceptronWindow)
        self.pb_add_td.setObjectName(u"pb_add_td")
        sizePolicy1.setHeightForWidth(self.pb_add_td.sizePolicy().hasHeightForWidth())
        self.pb_add_td.setSizePolicy(sizePolicy1)
        self.pb_add_td.setMinimumSize(QSize(14, 14))
        self.pb_add_td.setMaximumSize(QSize(14, 14))

        self.hl_train_data_header.addWidget(self.pb_add_td)

        self.pb_remove_td = QToolButton(PerceptronWindow)
        self.pb_remove_td.setObjectName(u"pb_remove_td")
        sizePolicy1.setHeightForWidth(self.pb_remove_td.sizePolicy().hasHeightForWidth())
        self.pb_remove_td.setSizePolicy(sizePolicy1)
        self.pb_remove_td.setMinimumSize(QSize(14, 14))
        self.pb_remove_td.setMaximumSize(QSize(14, 14))

        self.hl_train_data_header.addWidget(self.pb_remove_td)


        self.gl_main.addLayout(self.hl_train_data_header, 0, 0, 1, 2)

        self.pb_train_all = QPushButton(PerceptronWindow)
        self.pb_train_all.setObjectName(u"pb_train_all")
        sizePolicy1.setHeightForWidth(self.pb_train_all.sizePolicy().hasHeightForWidth())
        self.pb_train_all.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.pb_train_all, 3, 0, 1, 2)

        self.pb_train_selectively = QPushButton(PerceptronWindow)
        self.pb_train_selectively.setObjectName(u"pb_train_selectively")
        sizePolicy.setHeightForWidth(self.pb_train_selectively.sizePolicy().hasHeightForWidth())
        self.pb_train_selectively.setSizePolicy(sizePolicy)

        self.gl_main.addWidget(self.pb_train_selectively, 2, 1, 1, 1)

        self.le_file_path = QLineEdit(PerceptronWindow)
        self.le_file_path.setObjectName(u"le_file_path")
        sizePolicy3.setHeightForWidth(self.le_file_path.sizePolicy().hasHeightForWidth())
        self.le_file_path.setSizePolicy(sizePolicy3)
        self.le_file_path.setStyleSheet(u"border: none; background: transparent")
        self.le_file_path.setText(u"\ud83d\udcc1 \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b...")
        self.le_file_path.setReadOnly(True)

        self.gl_main.addWidget(self.le_file_path, 2, 2, 1, 1)

        self.te_perceptron_output = QTextEdit(PerceptronWindow)
        self.te_perceptron_output.setObjectName(u"te_perceptron_output")
        sizePolicy2.setHeightForWidth(self.te_perceptron_output.sizePolicy().hasHeightForWidth())
        self.te_perceptron_output.setSizePolicy(sizePolicy2)
        self.te_perceptron_output.setReadOnly(True)

        self.gl_main.addWidget(self.te_perceptron_output, 1, 2, 1, 2)


        self.retranslateUi(PerceptronWindow)

        QMetaObject.connectSlotsByName(PerceptronWindow)
    # setupUi

    def retranslateUi(self, PerceptronWindow):
        PerceptronWindow.setWindowTitle(QCoreApplication.translate("PerceptronWindow", u"\u0420\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435 \u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u0445 \u0431\u0443\u043a\u0432", None))
        self.pb_choose_file.setText(QCoreApplication.translate("PerceptronWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.pb_predict.setText(QCoreApplication.translate("PerceptronWindow", u"\u041f\u043e\u0434\u0430\u0442\u044c \u043d\u0430 \u0432\u0445\u043e\u0434 \u043f\u0435\u0440\u0441\u0435\u043f\u0442\u0440\u043e\u043d\u0443", None))
        ___qtablewidgetitem = self.tw_train_data.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PerceptronWindow", u" \u0411\u0443\u043a\u0432\u0430 ", None));
        ___qtablewidgetitem1 = self.tw_train_data.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PerceptronWindow", u"\u041f\u0443\u0442\u044c", None));
        self.le_neurons.setPlaceholderText(QCoreApplication.translate("PerceptronWindow", u"\u041d\u0435\u0439\u0440\u043e\u043d\u044b (A-Z)", None))
        self.l_perceptron_output.setText(QCoreApplication.translate("PerceptronWindow", u"\u0412\u044b\u0445\u043e\u0434 \u043f\u0435\u0440\u0441\u0435\u043f\u0442\u0440\u043e\u043d\u0430", None))
        self.cb_only_1.setText(QCoreApplication.translate("PerceptronWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e 1", None))
        self.l_train_data.setText(QCoreApplication.translate("PerceptronWindow", u"\u0422\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043e\u0447\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pb_add_td.setText(QCoreApplication.translate("PerceptronWindow", u"+", None))
        self.pb_remove_td.setText(QCoreApplication.translate("PerceptronWindow", u"-", None))
        self.pb_train_all.setText(QCoreApplication.translate("PerceptronWindow", u"\u041e\u0431\u0443\u0447\u0438\u0442\u044c \u0432\u0441\u0435", None))
        self.pb_train_selectively.setText(QCoreApplication.translate("PerceptronWindow", u"\u041e\u0431\u0443\u0447\u0438\u0442\u044c", None))
    # retranslateUi

