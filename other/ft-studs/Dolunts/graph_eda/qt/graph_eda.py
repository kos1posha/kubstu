# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph_eda.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_GraphEDA(object):
    def setupUi(self, GraphEDA):
        if not GraphEDA.objectName():
            GraphEDA.setObjectName(u"GraphEDA")
        GraphEDA.resize(400, 540)
        self.gl_main = QGridLayout(GraphEDA)
        self.gl_main.setSpacing(1)
        self.gl_main.setObjectName(u"gl_main")
        self.eda_examples_wd = QWidget(GraphEDA)
        self.eda_examples_wd.setObjectName(u"eda_examples_wd")
        self.gl_sec = QGridLayout(self.eda_examples_wd)
        self.gl_sec.setSpacing(1)
        self.gl_sec.setObjectName(u"gl_sec")
        self.gl_sec.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.eda_examples_wd)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_14, 4, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.eda_examples_wd)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.eda_examples_wd)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.eda_examples_wd)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.eda_examples_wd)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_1 = QPushButton(self.eda_examples_wd)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.eda_examples_wd)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_13, 4, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.eda_examples_wd)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.eda_examples_wd)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.eda_examples_wd)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.eda_examples_wd)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_15, 4, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.eda_examples_wd)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.eda_examples_wd)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.eda_examples_wd)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.eda_examples_wd)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)

        self.gl_sec.addWidget(self.pushButton_6, 1, 2, 1, 1)


        self.gl_main.addWidget(self.eda_examples_wd, 2, 0, 1, 4)

        self.eda_examples_lbl = QLabel(GraphEDA)
        self.eda_examples_lbl.setObjectName(u"eda_examples_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.eda_examples_lbl.sizePolicy().hasHeightForWidth())
        self.eda_examples_lbl.setSizePolicy(sizePolicy1)
        self.eda_examples_lbl.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.eda_examples_lbl, 1, 0, 1, 4)

        self.dataset_preview_btn = QPushButton(GraphEDA)
        self.dataset_preview_btn.setObjectName(u"dataset_preview_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dataset_preview_btn.sizePolicy().hasHeightForWidth())
        self.dataset_preview_btn.setSizePolicy(sizePolicy2)

        self.gl_main.addWidget(self.dataset_preview_btn, 0, 3, 1, 1)

        self.dataset_lbl = QLabel(GraphEDA)
        self.dataset_lbl.setObjectName(u"dataset_lbl")
        sizePolicy1.setHeightForWidth(self.dataset_lbl.sizePolicy().hasHeightForWidth())
        self.dataset_lbl.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.dataset_lbl, 0, 0, 1, 3)


        self.retranslateUi(GraphEDA)

        QMetaObject.connectSlotsByName(GraphEDA)
    # setupUi

    def retranslateUi(self, GraphEDA):
        GraphEDA.setWindowTitle(QCoreApplication.translate("GraphEDA", u"\u0420\u0410\u0414 - \u0413\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043c\u0435\u0442\u043e\u0434\u044b", None))
        self.pushButton_14.setText(QCoreApplication.translate("GraphEDA", u"14", None))
        self.pushButton_4.setText(QCoreApplication.translate("GraphEDA", u"4", None))
        self.pushButton_10.setText(QCoreApplication.translate("GraphEDA", u"10", None))
        self.pushButton_2.setText(QCoreApplication.translate("GraphEDA", u"2", None))
        self.pushButton_12.setText(QCoreApplication.translate("GraphEDA", u"12", None))
        self.pushButton_1.setText(QCoreApplication.translate("GraphEDA", u"1", None))
        self.pushButton_13.setText(QCoreApplication.translate("GraphEDA", u"13", None))
        self.pushButton_7.setText(QCoreApplication.translate("GraphEDA", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("GraphEDA", u"8", None))
        self.pushButton_3.setText(QCoreApplication.translate("GraphEDA", u"3", None))
        self.pushButton_15.setText(QCoreApplication.translate("GraphEDA", u"15", None))
        self.pushButton_11.setText(QCoreApplication.translate("GraphEDA", u"11", None))
        self.pushButton_5.setText(QCoreApplication.translate("GraphEDA", u"5", None))
        self.pushButton_9.setText(QCoreApplication.translate("GraphEDA", u"9", None))
        self.pushButton_6.setText(QCoreApplication.translate("GraphEDA", u"6", None))
        self.eda_examples_lbl.setText(QCoreApplication.translate("GraphEDA", u"\u0420\u0430\u0437\u0432\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u043d\u0430\u043b\u0438\u0437 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.dataset_preview_btn.setText(QCoreApplication.translate("GraphEDA", u"\u041f\u0440\u0435\u0434\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.dataset_lbl.setText(QCoreApplication.translate("GraphEDA", u"\u0414\u0430\u0442\u0430\u0441\u0435\u0442: Netflix", None))
    # retranslateUi

