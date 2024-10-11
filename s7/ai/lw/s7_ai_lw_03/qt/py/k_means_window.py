# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'k_means_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QGridLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_KMeansWindow(object):
    def setupUi(self, KMeansWindow):
        if not KMeansWindow.objectName():
            KMeansWindow.setObjectName(u"KMeansWindow")
        KMeansWindow.resize(668, 437)
        self.gl_main = QGridLayout(KMeansWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.l_edit_points = QLabel(KMeansWindow)
        self.l_edit_points.setObjectName(u"l_edit_points")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.l_edit_points.setFont(font)

        self.gl_main.addWidget(self.l_edit_points, 0, 2, 1, 1)

        self.tb_adjust_plot = QToolButton(KMeansWindow)
        self.tb_adjust_plot.setObjectName(u"tb_adjust_plot")
        self.tb_adjust_plot.setStyleSheet(u"background:transparent;border:none")
        icon = QIcon()
        icon.addFile(u":/plot_scale/icons/adjust.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_adjust_plot.setIcon(icon)

        self.gl_main.addWidget(self.tb_adjust_plot, 0, 1, 1, 1)

        self.l_plot = QLabel(KMeansWindow)
        self.l_plot.setObjectName(u"l_plot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_plot.sizePolicy().hasHeightForWidth())
        self.l_plot.setSizePolicy(sizePolicy)
        self.l_plot.setFont(font)

        self.gl_main.addWidget(self.l_plot, 0, 0, 1, 1)

        self.w_plot = QWidget(KMeansWindow)
        self.w_plot.setObjectName(u"w_plot")
        self.w_plot.setMinimumSize(QSize(450, 406))
        self.w_plot.setMaximumSize(QSize(450, 406))
        self.vl_plot = QVBoxLayout(self.w_plot)
        self.vl_plot.setObjectName(u"vl_plot")
        self.vl_plot.setContentsMargins(0, 0, 0, 0)

        self.gl_main.addWidget(self.w_plot, 1, 0, 1, 2)

        self.vl_right = QVBoxLayout()
        self.vl_right.setObjectName(u"vl_right")
        self.w_sidebar = QWidget(KMeansWindow)
        self.w_sidebar.setObjectName(u"w_sidebar")
        self.w_sidebar.setMinimumSize(QSize(200, 0))
        self.w_sidebar.setMaximumSize(QSize(200, 383))
        self.vl_sidebar = QVBoxLayout(self.w_sidebar)
        self.vl_sidebar.setObjectName(u"vl_sidebar")
        self.vl_sidebar.setContentsMargins(0, 0, 0, 0)
        self.vl_edit_points = QVBoxLayout()
        self.vl_edit_points.setObjectName(u"vl_edit_points")
        self.l_mouse_press_description = QLabel(self.w_sidebar)
        self.l_mouse_press_description.setObjectName(u"l_mouse_press_description")
        self.l_mouse_press_description.setStyleSheet(u"color:grey")
        self.l_mouse_press_description.setWordWrap(True)

        self.vl_edit_points.addWidget(self.l_mouse_press_description)

        self.l_random_points_lims = QLabel(self.w_sidebar)
        self.l_random_points_lims.setObjectName(u"l_random_points_lims")
        sizePolicy.setHeightForWidth(self.l_random_points_lims.sizePolicy().hasHeightForWidth())
        self.l_random_points_lims.setSizePolicy(sizePolicy)

        self.vl_edit_points.addWidget(self.l_random_points_lims)

        self.tw_random_points_lims = QTableWidget(self.w_sidebar)
        if (self.tw_random_points_lims.columnCount() < 2):
            self.tw_random_points_lims.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_random_points_lims.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_random_points_lims.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tw_random_points_lims.rowCount() < 2):
            self.tw_random_points_lims.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_random_points_lims.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_random_points_lims.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tw_random_points_lims.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tw_random_points_lims.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tw_random_points_lims.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tw_random_points_lims.setItem(1, 1, __qtablewidgetitem7)
        self.tw_random_points_lims.setObjectName(u"tw_random_points_lims")
        self.tw_random_points_lims.setSelectionMode(QAbstractItemView.NoSelection)

        self.vl_edit_points.addWidget(self.tw_random_points_lims)

        self.l_random_points_count = QLabel(self.w_sidebar)
        self.l_random_points_count.setObjectName(u"l_random_points_count")
        sizePolicy.setHeightForWidth(self.l_random_points_count.sizePolicy().hasHeightForWidth())
        self.l_random_points_count.setSizePolicy(sizePolicy)

        self.vl_edit_points.addWidget(self.l_random_points_count)

        self.sb_random_points_count = QSpinBox(self.w_sidebar)
        self.sb_random_points_count.setObjectName(u"sb_random_points_count")
        self.sb_random_points_count.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sb_random_points_count.setMinimum(1)
        self.sb_random_points_count.setMaximum(100)
        self.sb_random_points_count.setValue(20)

        self.vl_edit_points.addWidget(self.sb_random_points_count)

        self.pb_add_random_points = QPushButton(self.w_sidebar)
        self.pb_add_random_points.setObjectName(u"pb_add_random_points")

        self.vl_edit_points.addWidget(self.pb_add_random_points)


        self.vl_sidebar.addLayout(self.vl_edit_points)

        self.l_clustering = QLabel(self.w_sidebar)
        self.l_clustering.setObjectName(u"l_clustering")
        self.l_clustering.setFont(font)

        self.vl_sidebar.addWidget(self.l_clustering)

        self.vl_clustering = QVBoxLayout()
        self.vl_clustering.setObjectName(u"vl_clustering")
        self.l_clusters_count = QLabel(self.w_sidebar)
        self.l_clusters_count.setObjectName(u"l_clusters_count")
        sizePolicy.setHeightForWidth(self.l_clusters_count.sizePolicy().hasHeightForWidth())
        self.l_clusters_count.setSizePolicy(sizePolicy)

        self.vl_clustering.addWidget(self.l_clusters_count)

        self.sb_clusters_count = QSpinBox(self.w_sidebar)
        self.sb_clusters_count.setObjectName(u"sb_clusters_count")
        self.sb_clusters_count.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sb_clusters_count.setMinimum(2)
        self.sb_clusters_count.setMaximum(100)
        self.sb_clusters_count.setValue(3)

        self.vl_clustering.addWidget(self.sb_clusters_count)

        self.l_max_iterations = QLabel(self.w_sidebar)
        self.l_max_iterations.setObjectName(u"l_max_iterations")
        sizePolicy.setHeightForWidth(self.l_max_iterations.sizePolicy().hasHeightForWidth())
        self.l_max_iterations.setSizePolicy(sizePolicy)

        self.vl_clustering.addWidget(self.l_max_iterations)

        self.sb_max_iterations = QSpinBox(self.w_sidebar)
        self.sb_max_iterations.setObjectName(u"sb_max_iterations")
        self.sb_max_iterations.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sb_max_iterations.setMinimum(2)
        self.sb_max_iterations.setMaximum(1000)
        self.sb_max_iterations.setSingleStep(5)
        self.sb_max_iterations.setValue(100)

        self.vl_clustering.addWidget(self.sb_max_iterations)


        self.vl_sidebar.addLayout(self.vl_clustering)


        self.vl_right.addWidget(self.w_sidebar)

        self.pb_clustering = QPushButton(KMeansWindow)
        self.pb_clustering.setObjectName(u"pb_clustering")

        self.vl_right.addWidget(self.pb_clustering)


        self.gl_main.addLayout(self.vl_right, 1, 2, 1, 1)


        self.retranslateUi(KMeansWindow)

        QMetaObject.connectSlotsByName(KMeansWindow)
    # setupUi

    def retranslateUi(self, KMeansWindow):
        KMeansWindow.setWindowTitle(QCoreApplication.translate("KMeansWindow", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.l_edit_points.setText(QCoreApplication.translate("KMeansWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0447\u043a\u0438", None))
        self.l_plot.setText(QCoreApplication.translate("KMeansWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.l_mouse_press_description.setText(QCoreApplication.translate("KMeansWindow", u"\u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0442\u044c \u0438 \u0443\u0434\u0430\u043b\u044f\u0442\u044c \u0442\u043e\u0447\u043a\u0438 \u043f\u0440\u044f\u043c\u043e \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044f \u043b\u0435\u0432\u0443\u044e \u0438 \u043f\u0440\u0430\u0432\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0438 \u043c\u044b\u0448\u0438 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e", None))
        self.l_random_points_lims.setText(QCoreApplication.translate("KMeansWindow", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0435 \u0442\u043e\u0447\u043a\u0438 \u0432 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0435", None))
        ___qtablewidgetitem = self.tw_random_points_lims.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("KMeansWindow", u"min", None));
        ___qtablewidgetitem1 = self.tw_random_points_lims.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("KMeansWindow", u"max", None));
        ___qtablewidgetitem2 = self.tw_random_points_lims.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("KMeansWindow", u"x", None));
        ___qtablewidgetitem3 = self.tw_random_points_lims.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("KMeansWindow", u"y", None));

        __sortingEnabled = self.tw_random_points_lims.isSortingEnabled()
        self.tw_random_points_lims.setSortingEnabled(False)
        self.tw_random_points_lims.setSortingEnabled(__sortingEnabled)

        self.l_random_points_count.setText(QCoreApplication.translate("KMeansWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.pb_add_random_points.setText(QCoreApplication.translate("KMeansWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.l_clustering.setText(QCoreApplication.translate("KMeansWindow", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f (k-means)", None))
        self.l_clusters_count.setText(QCoreApplication.translate("KMeansWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u043e\u0432", None))
        self.l_max_iterations.setText(QCoreApplication.translate("KMeansWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0439", None))
        self.pb_clustering.setText(QCoreApplication.translate("KMeansWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
    # retranslateUi

