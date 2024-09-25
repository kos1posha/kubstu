# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QWidget)

class Ui_PerceptronWindow(object):
    def setupUi(self, PerceptronWindow):
        if not PerceptronWindow.objectName():
            PerceptronWindow.setObjectName(u"PerceptronWindow")
        PerceptronWindow.resize(471, 413)
        self.gl_main = QGridLayout(PerceptronWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.l_preview = QLabel(PerceptronWindow)
        self.l_preview.setObjectName(u"l_preview")
        self.l_preview.setMinimumSize(QSize(300, 300))
        self.l_preview.setMaximumSize(QSize(300, 300))
        self.l_preview.setFrameShape(QFrame.Box)
        self.l_preview.setFrameShadow(QFrame.Sunken)
        self.l_preview.setScaledContents(True)
        self.l_preview.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.l_preview, 1, 1, 1, 1)

        self.gl_neurons = QGridLayout()
        self.gl_neurons.setObjectName(u"gl_neurons")
        self.l_neurons = QLabel(PerceptronWindow)
        self.l_neurons.setObjectName(u"l_neurons")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_neurons.sizePolicy().hasHeightForWidth())
        self.l_neurons.setSizePolicy(sizePolicy)

        self.gl_neurons.addWidget(self.l_neurons, 0, 0, 1, 1)

        self.tw_neurons = QTableWidget(PerceptronWindow)
        if (self.tw_neurons.columnCount() < 3):
            self.tw_neurons.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_neurons.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_neurons.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_neurons.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tw_neurons.setObjectName(u"tw_neurons")
        self.tw_neurons.setMaximumSize(QSize(150, 16777215))
        self.tw_neurons.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_neurons.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_neurons.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_neurons.verticalHeader().setVisible(False)

        self.gl_neurons.addWidget(self.tw_neurons, 1, 0, 1, 1)


        self.gl_main.addLayout(self.gl_neurons, 0, 0, 4, 1)

        self.l_letter_preview = QLabel(PerceptronWindow)
        self.l_letter_preview.setObjectName(u"l_letter_preview")

        self.gl_main.addWidget(self.l_letter_preview, 0, 1, 1, 1)

        self.w_actions_and_inputs = QWidget(PerceptronWindow)
        self.w_actions_and_inputs.setObjectName(u"w_actions_and_inputs")
        self.w_actions_and_inputs.setMaximumSize(QSize(300, 16777215))
        self.gl_actions_and_inputs = QGridLayout(self.w_actions_and_inputs)
        self.gl_actions_and_inputs.setObjectName(u"gl_actions_and_inputs")
        self.gl_actions_and_inputs.setVerticalSpacing(2)
        self.gl_actions_and_inputs.setContentsMargins(0, 0, 0, 0)
        self.dsb_alpha = QDoubleSpinBox(self.w_actions_and_inputs)
        self.dsb_alpha.setObjectName(u"dsb_alpha")
        sizePolicy.setHeightForWidth(self.dsb_alpha.sizePolicy().hasHeightForWidth())
        self.dsb_alpha.setSizePolicy(sizePolicy)
        self.dsb_alpha.setMaximumSize(QSize(97, 16777215))
        self.dsb_alpha.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dsb_alpha.setMinimum(0.010000000000000)
        self.dsb_alpha.setMaximum(1.000000000000000)
        self.dsb_alpha.setSingleStep(0.010000000000000)
        self.dsb_alpha.setValue(0.050000000000000)

        self.gl_actions_and_inputs.addWidget(self.dsb_alpha, 2, 1, 1, 1)

        self.le_letter = QLineEdit(self.w_actions_and_inputs)
        self.le_letter.setObjectName(u"le_letter")
        sizePolicy.setHeightForWidth(self.le_letter.sizePolicy().hasHeightForWidth())
        self.le_letter.setSizePolicy(sizePolicy)
        self.le_letter.setMaximumSize(QSize(97, 16777215))
        self.le_letter.setMaxLength(1)

        self.gl_actions_and_inputs.addWidget(self.le_letter, 2, 0, 1, 1)

        self.l_epochs = QLabel(self.w_actions_and_inputs)
        self.l_epochs.setObjectName(u"l_epochs")
        sizePolicy.setHeightForWidth(self.l_epochs.sizePolicy().hasHeightForWidth())
        self.l_epochs.setSizePolicy(sizePolicy)

        self.gl_actions_and_inputs.addWidget(self.l_epochs, 1, 2, 1, 1)

        self.sb_epochs = QSpinBox(self.w_actions_and_inputs)
        self.sb_epochs.setObjectName(u"sb_epochs")
        sizePolicy.setHeightForWidth(self.sb_epochs.sizePolicy().hasHeightForWidth())
        self.sb_epochs.setSizePolicy(sizePolicy)
        self.sb_epochs.setMaximumSize(QSize(97, 16777215))
        self.sb_epochs.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_epochs.setMinimum(1)
        self.sb_epochs.setMaximum(100)
        self.sb_epochs.setValue(20)

        self.gl_actions_and_inputs.addWidget(self.sb_epochs, 2, 2, 1, 1)

        self.l_alpha = QLabel(self.w_actions_and_inputs)
        self.l_alpha.setObjectName(u"l_alpha")
        sizePolicy.setHeightForWidth(self.l_alpha.sizePolicy().hasHeightForWidth())
        self.l_alpha.setSizePolicy(sizePolicy)

        self.gl_actions_and_inputs.addWidget(self.l_alpha, 1, 1, 1, 1)

        self.l_letter = QLabel(self.w_actions_and_inputs)
        self.l_letter.setObjectName(u"l_letter")
        sizePolicy.setHeightForWidth(self.l_letter.sizePolicy().hasHeightForWidth())
        self.l_letter.setSizePolicy(sizePolicy)

        self.gl_actions_and_inputs.addWidget(self.l_letter, 1, 0, 1, 1)

        self.hl_train = QHBoxLayout()
        self.hl_train.setObjectName(u"hl_train")
        self.hl_train.setContentsMargins(-1, 2, -1, -1)
        self.pb_train_one = QPushButton(self.w_actions_and_inputs)
        self.pb_train_one.setObjectName(u"pb_train_one")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_train_one.sizePolicy().hasHeightForWidth())
        self.pb_train_one.setSizePolicy(sizePolicy1)

        self.hl_train.addWidget(self.pb_train_one)

        self.pb_train_all = QPushButton(self.w_actions_and_inputs)
        self.pb_train_all.setObjectName(u"pb_train_all")
        sizePolicy1.setHeightForWidth(self.pb_train_all.sizePolicy().hasHeightForWidth())
        self.pb_train_all.setSizePolicy(sizePolicy1)

        self.hl_train.addWidget(self.pb_train_all)


        self.gl_actions_and_inputs.addLayout(self.hl_train, 3, 0, 1, 3)

        self.pb_predict = QPushButton(self.w_actions_and_inputs)
        self.pb_predict.setObjectName(u"pb_predict")

        self.gl_actions_and_inputs.addWidget(self.pb_predict, 0, 0, 1, 3)


        self.gl_main.addWidget(self.w_actions_and_inputs, 2, 1, 2, 1)


        self.retranslateUi(PerceptronWindow)

        QMetaObject.connectSlotsByName(PerceptronWindow)
    # setupUi

    def retranslateUi(self, PerceptronWindow):
        PerceptronWindow.setWindowTitle(QCoreApplication.translate("PerceptronWindow", u"\u041f\u0435\u0440\u0441\u0435\u043f\u0442\u0440\u043e\u043d", None))
        self.l_neurons.setText(QCoreApplication.translate("PerceptronWindow", u"\u041d\u0435\u0439\u0440\u043e\u043d\u044b", None))
        ___qtablewidgetitem = self.tw_neurons.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PerceptronWindow", u"\u0411\u0443\u043a\u0432\u0430", None));
        ___qtablewidgetitem1 = self.tw_neurons.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PerceptronWindow", u"\u0412\u0435\u0441\u0430", None));
        ___qtablewidgetitem2 = self.tw_neurons.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PerceptronWindow", u"\u0412\u044b\u0445\u043e\u0434", None));
        self.l_letter_preview.setText(QCoreApplication.translate("PerceptronWindow", u"\u041f\u0440\u0435\u0432\u044c\u044e \u0431\u0443\u043a\u0432\u044b", None))
        self.l_epochs.setText(QCoreApplication.translate("PerceptronWindow", u"\u0418\u0442\u0435\u0440\u0430\u0446\u0438\u0439", None))
        self.l_alpha.setText(QCoreApplication.translate("PerceptronWindow", u"\u0410\u043b\u044c\u0444\u0430", None))
        self.l_letter.setText(QCoreApplication.translate("PerceptronWindow", u"\u0411\u0443\u043a\u0432\u0430", None))
        self.pb_train_one.setText(QCoreApplication.translate("PerceptronWindow", u"\u041e\u0431\u0443\u0447\u0438\u0442\u044c \u043e\u0434\u0438\u043d \u043d\u0435\u0439\u0440\u043e\u043d", None))
        self.pb_train_all.setText(QCoreApplication.translate("PerceptronWindow", u"\u041e\u0431\u0443\u0447\u0438\u0442\u044c \u0432\u0441\u0435 \u043d\u0435\u0439\u0440\u043e\u043d\u044b", None))
        self.pb_predict.setText(QCoreApplication.translate("PerceptronWindow", u"\u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u0442\u044c", None))
    # retranslateUi

