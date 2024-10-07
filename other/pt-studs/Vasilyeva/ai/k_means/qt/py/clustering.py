# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clustering.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_KMeansWindow(object):
    def setupUi(self, KMeansWindow):
        if not KMeansWindow.objectName():
            KMeansWindow.setObjectName(u"KMeansWindow")
        KMeansWindow.resize(566, 418)
        self.gl_main = QGridLayout(KMeansWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.pb_clustering = QPushButton(KMeansWindow)
        self.pb_clustering.setObjectName(u"pb_clustering")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_clustering.sizePolicy().hasHeightForWidth())
        self.pb_clustering.setSizePolicy(sizePolicy)
        self.pb_clustering.setMinimumSize(QSize(200, 0))
        self.pb_clustering.setMaximumSize(QSize(200, 16777215))

        self.gl_main.addWidget(self.pb_clustering, 11, 1, 1, 1)

        self.w_plot = QWidget(KMeansWindow)
        self.w_plot.setObjectName(u"w_plot")
        self.w_plot.setMinimumSize(QSize(350, 350))
        self.w_plot.setMaximumSize(QSize(350, 350))
        self.vl_plot = QVBoxLayout(self.w_plot)
        self.vl_plot.setObjectName(u"vl_plot")
        self.vl_plot.setContentsMargins(0, 0, 0, 0)

        self.gl_main.addWidget(self.w_plot, 1, 0, 9, 1)

        self.lw_points = QListWidget(KMeansWindow)
        self.lw_points.setObjectName(u"lw_points")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lw_points.sizePolicy().hasHeightForWidth())
        self.lw_points.setSizePolicy(sizePolicy1)
        self.lw_points.setMinimumSize(QSize(200, 0))
        self.lw_points.setMaximumSize(QSize(200, 16777215))

        self.gl_main.addWidget(self.lw_points, 1, 1, 8, 1)

        self.l_points = QLabel(KMeansWindow)
        self.l_points.setObjectName(u"l_points")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.l_points.sizePolicy().hasHeightForWidth())
        self.l_points.setSizePolicy(sizePolicy2)
        self.l_points.setMinimumSize(QSize(200, 0))
        self.l_points.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.l_points.setFont(font)

        self.gl_main.addWidget(self.l_points, 0, 1, 1, 1)

        self.hl_actions = QHBoxLayout()
        self.hl_actions.setObjectName(u"hl_actions")
        self.rb_add_point = QRadioButton(KMeansWindow)
        self.rb_add_point.setObjectName(u"rb_add_point")
        sizePolicy.setHeightForWidth(self.rb_add_point.sizePolicy().hasHeightForWidth())
        self.rb_add_point.setSizePolicy(sizePolicy)

        self.hl_actions.addWidget(self.rb_add_point)

        self.rb_delete_point = QRadioButton(KMeansWindow)
        self.rb_delete_point.setObjectName(u"rb_delete_point")
        sizePolicy.setHeightForWidth(self.rb_delete_point.sizePolicy().hasHeightForWidth())
        self.rb_delete_point.setSizePolicy(sizePolicy)

        self.hl_actions.addWidget(self.rb_delete_point)

        self.rb_do_nothing = QRadioButton(KMeansWindow)
        self.rb_do_nothing.setObjectName(u"rb_do_nothing")
        sizePolicy.setHeightForWidth(self.rb_do_nothing.sizePolicy().hasHeightForWidth())
        self.rb_do_nothing.setSizePolicy(sizePolicy)
        self.rb_do_nothing.setChecked(True)

        self.hl_actions.addWidget(self.rb_do_nothing)


        self.gl_main.addLayout(self.hl_actions, 11, 0, 1, 1)

        self.l_plot = QLabel(KMeansWindow)
        self.l_plot.setObjectName(u"l_plot")
        sizePolicy2.setHeightForWidth(self.l_plot.sizePolicy().hasHeightForWidth())
        self.l_plot.setSizePolicy(sizePolicy2)
        self.l_plot.setFont(font)

        self.gl_main.addWidget(self.l_plot, 0, 0, 1, 1)

        self.w_params = QWidget(KMeansWindow)
        self.w_params.setObjectName(u"w_params")
        self.w_params.setMaximumSize(QSize(200, 16777215))
        self.gl_params = QGridLayout(self.w_params)
        self.gl_params.setObjectName(u"gl_params")
        self.gl_params.setContentsMargins(0, 0, 0, 0)
        self.l_clusters_count = QLabel(self.w_params)
        self.l_clusters_count.setObjectName(u"l_clusters_count")
        sizePolicy2.setHeightForWidth(self.l_clusters_count.sizePolicy().hasHeightForWidth())
        self.l_clusters_count.setSizePolicy(sizePolicy2)

        self.gl_params.addWidget(self.l_clusters_count, 0, 0, 1, 1)

        self.l_iterations = QLabel(self.w_params)
        self.l_iterations.setObjectName(u"l_iterations")
        sizePolicy2.setHeightForWidth(self.l_iterations.sizePolicy().hasHeightForWidth())
        self.l_iterations.setSizePolicy(sizePolicy2)

        self.gl_params.addWidget(self.l_iterations, 0, 1, 1, 1)

        self.sb_clusters_count = QSpinBox(self.w_params)
        self.sb_clusters_count.setObjectName(u"sb_clusters_count")
        self.sb_clusters_count.setMinimum(2)
        self.sb_clusters_count.setMaximum(24)

        self.gl_params.addWidget(self.sb_clusters_count, 1, 0, 1, 1)

        self.sb_iterations = QSpinBox(self.w_params)
        self.sb_iterations.setObjectName(u"sb_iterations")
        self.sb_iterations.setMinimum(2)
        self.sb_iterations.setMaximum(150)
        self.sb_iterations.setValue(10)

        self.gl_params.addWidget(self.sb_iterations, 1, 1, 1, 1)


        self.gl_main.addWidget(self.w_params, 9, 1, 1, 1)


        self.retranslateUi(KMeansWindow)

        QMetaObject.connectSlotsByName(KMeansWindow)
    # setupUi

    def retranslateUi(self, KMeansWindow):
        KMeansWindow.setWindowTitle(QCoreApplication.translate("KMeansWindow", u"k-means", None))
        self.pb_clustering.setText(QCoreApplication.translate("KMeansWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.l_points.setText(QCoreApplication.translate("KMeansWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u0442\u043e\u0447\u0435\u043a", None))
        self.rb_add_point.setText(QCoreApplication.translate("KMeansWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0442\u044c \u0442\u043e\u0447\u043a\u0443", None))
        self.rb_delete_point.setText(QCoreApplication.translate("KMeansWindow", u"\u0423\u0434\u0430\u043b\u044f\u0442\u044c \u0442\u043e\u0447\u043a\u0443", None))
        self.rb_do_nothing.setText(QCoreApplication.translate("KMeansWindow", u"\u041d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u0434\u0435\u043b\u0430\u0442\u044c", None))
        self.l_plot.setText(QCoreApplication.translate("KMeansWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0442\u043e\u0447\u0435\u043a", None))
        self.l_clusters_count.setText(QCoreApplication.translate("KMeansWindow", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u043e\u0432", None))
        self.l_iterations.setText(QCoreApplication.translate("KMeansWindow", u"\u0418\u0442\u0435\u0440\u0430\u0446\u0438\u0439", None))
    # retranslateUi

