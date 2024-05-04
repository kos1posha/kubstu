# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolButton, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.w_main = QWidget(MainWindow)
        self.w_main.setObjectName(u"w_main")
        self.gl_main = QGridLayout(self.w_main)
        self.gl_main.setSpacing(3)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setContentsMargins(3, 3, 3, 3)
        self.f_top = QFrame(self.w_main)
        self.f_top.setObjectName(u"f_top")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_top.sizePolicy().hasHeightForWidth())
        self.f_top.setSizePolicy(sizePolicy)
        self.f_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_top.setFrameShadow(QFrame.Shadow.Raised)
        self.gl_top = QGridLayout(self.f_top)
        self.gl_top.setObjectName(u"gl_top")
        self.l_categories = QLabel(self.f_top)
        self.l_categories.setObjectName(u"l_categories")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.l_categories.setFont(font)

        self.gl_top.addWidget(self.l_categories, 9, 4, 1, 9)

        self.treew_storage = QTreeWidget(self.f_top)
        font1 = QFont()
        font1.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font1);
        self.treew_storage.setHeaderItem(__qtreewidgetitem)
        self.treew_storage.setObjectName(u"treew_storage")
        self.treew_storage.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.gl_top.addWidget(self.treew_storage, 9, 3, 3, 1)

        self.pb_outcome = QPushButton(self.f_top)
        self.pb_outcome.setObjectName(u"pb_outcome")

        self.gl_top.addWidget(self.pb_outcome, 9, 1, 1, 1)

        self.gb_metrics = QGroupBox(self.f_top)
        self.gb_metrics.setObjectName(u"gb_metrics")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gb_metrics.sizePolicy().hasHeightForWidth())
        self.gb_metrics.setSizePolicy(sizePolicy1)
        self.gl_metrics = QGridLayout(self.gb_metrics)
        self.gl_metrics.setObjectName(u"gl_metrics")
        self.l_inventory_count_value = QLabel(self.gb_metrics)
        self.l_inventory_count_value.setObjectName(u"l_inventory_count_value")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.l_inventory_count_value.sizePolicy().hasHeightForWidth())
        self.l_inventory_count_value.setSizePolicy(sizePolicy2)
        self.l_inventory_count_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gl_metrics.addWidget(self.l_inventory_count_value, 1, 1, 1, 1)

        self.l_outcome_last_week_value = QLabel(self.gb_metrics)
        self.l_outcome_last_week_value.setObjectName(u"l_outcome_last_week_value")
        sizePolicy2.setHeightForWidth(self.l_outcome_last_week_value.sizePolicy().hasHeightForWidth())
        self.l_outcome_last_week_value.setSizePolicy(sizePolicy2)
        self.l_outcome_last_week_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gl_metrics.addWidget(self.l_outcome_last_week_value, 7, 1, 1, 1)

        self.l_products_count_value = QLabel(self.gb_metrics)
        self.l_products_count_value.setObjectName(u"l_products_count_value")
        sizePolicy2.setHeightForWidth(self.l_products_count_value.sizePolicy().hasHeightForWidth())
        self.l_products_count_value.setSizePolicy(sizePolicy2)
        self.l_products_count_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gl_metrics.addWidget(self.l_products_count_value, 0, 1, 1, 1)

        self.l_outcome_last_week = QLabel(self.gb_metrics)
        self.l_outcome_last_week.setObjectName(u"l_outcome_last_week")
        sizePolicy2.setHeightForWidth(self.l_outcome_last_week.sizePolicy().hasHeightForWidth())
        self.l_outcome_last_week.setSizePolicy(sizePolicy2)

        self.gl_metrics.addWidget(self.l_outcome_last_week, 7, 0, 1, 1)

        self.l_income_last_week_value = QLabel(self.gb_metrics)
        self.l_income_last_week_value.setObjectName(u"l_income_last_week_value")
        sizePolicy2.setHeightForWidth(self.l_income_last_week_value.sizePolicy().hasHeightForWidth())
        self.l_income_last_week_value.setSizePolicy(sizePolicy2)
        self.l_income_last_week_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gl_metrics.addWidget(self.l_income_last_week_value, 6, 1, 1, 1)

        self.l_run_out = QLabel(self.gb_metrics)
        self.l_run_out.setObjectName(u"l_run_out")
        sizePolicy2.setHeightForWidth(self.l_run_out.sizePolicy().hasHeightForWidth())
        self.l_run_out.setSizePolicy(sizePolicy2)

        self.gl_metrics.addWidget(self.l_run_out, 2, 0, 1, 1)

        self.l_total_price = QLabel(self.gb_metrics)
        self.l_total_price.setObjectName(u"l_total_price")
        sizePolicy2.setHeightForWidth(self.l_total_price.sizePolicy().hasHeightForWidth())
        self.l_total_price.setSizePolicy(sizePolicy2)

        self.gl_metrics.addWidget(self.l_total_price, 4, 0, 1, 1)

        self.l_total_price_value = QLabel(self.gb_metrics)
        self.l_total_price_value.setObjectName(u"l_total_price_value")
        sizePolicy2.setHeightForWidth(self.l_total_price_value.sizePolicy().hasHeightForWidth())
        self.l_total_price_value.setSizePolicy(sizePolicy2)
        self.l_total_price_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gl_metrics.addWidget(self.l_total_price_value, 4, 1, 1, 1)

        self.l_run_out_value = QLabel(self.gb_metrics)
        self.l_run_out_value.setObjectName(u"l_run_out_value")
        sizePolicy2.setHeightForWidth(self.l_run_out_value.sizePolicy().hasHeightForWidth())
        self.l_run_out_value.setSizePolicy(sizePolicy2)
        self.l_run_out_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gl_metrics.addWidget(self.l_run_out_value, 2, 1, 1, 1)

        self.l_income_last_week = QLabel(self.gb_metrics)
        self.l_income_last_week.setObjectName(u"l_income_last_week")
        sizePolicy2.setHeightForWidth(self.l_income_last_week.sizePolicy().hasHeightForWidth())
        self.l_income_last_week.setSizePolicy(sizePolicy2)

        self.gl_metrics.addWidget(self.l_income_last_week, 6, 0, 1, 1)

        self.l_products_count = QLabel(self.gb_metrics)
        self.l_products_count.setObjectName(u"l_products_count")
        sizePolicy2.setHeightForWidth(self.l_products_count.sizePolicy().hasHeightForWidth())
        self.l_products_count.setSizePolicy(sizePolicy2)

        self.gl_metrics.addWidget(self.l_products_count, 0, 0, 1, 1)

        self.l_inventory_count = QLabel(self.gb_metrics)
        self.l_inventory_count.setObjectName(u"l_inventory_count")
        sizePolicy2.setHeightForWidth(self.l_inventory_count.sizePolicy().hasHeightForWidth())
        self.l_inventory_count.setSizePolicy(sizePolicy2)

        self.gl_metrics.addWidget(self.l_inventory_count, 1, 0, 1, 1)


        self.gl_top.addWidget(self.gb_metrics, 11, 0, 1, 2)

        self.lw_categories = QListWidget(self.f_top)
        self.lw_categories.setObjectName(u"lw_categories")
        self.lw_categories.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.gl_top.addWidget(self.lw_categories, 10, 4, 2, 11)

        self.tb_add_product = QToolButton(self.f_top)
        self.tb_add_product.setObjectName(u"tb_add_product")
        self.tb_add_product.setMinimumSize(QSize(20, 20))
        self.tb_add_product.setMaximumSize(QSize(20, 20))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.tb_add_product.setFont(font2)
        self.tb_add_product.setStyleSheet(u"color:green")

        self.gl_top.addWidget(self.tb_add_product, 1, 13, 1, 1)

        self.tb_remove_product = QToolButton(self.f_top)
        self.tb_remove_product.setObjectName(u"tb_remove_product")
        self.tb_remove_product.setMinimumSize(QSize(20, 20))
        self.tb_remove_product.setMaximumSize(QSize(20, 20))
        self.tb_remove_product.setFont(font2)
        self.tb_remove_product.setStyleSheet(u"color:red")

        self.gl_top.addWidget(self.tb_remove_product, 1, 14, 1, 1)

        self.l_products = QLabel(self.f_top)
        self.l_products.setObjectName(u"l_products")
        self.l_products.setFont(font)

        self.gl_top.addWidget(self.l_products, 1, 0, 1, 13)

        self.tw_products = QTableWidget(self.f_top)
        if (self.tw_products.columnCount() < 8):
            self.tw_products.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_products.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_products.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_products.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_products.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_products.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_products.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_products.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_products.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tw_products.setObjectName(u"tw_products")
        self.tw_products.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tw_products.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tw_products.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tw_products.setSortingEnabled(True)
        self.tw_products.verticalHeader().setVisible(False)

        self.gl_top.addWidget(self.tw_products, 3, 0, 2, 15)

        self.tb_add_category = QToolButton(self.f_top)
        self.tb_add_category.setObjectName(u"tb_add_category")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tb_add_category.sizePolicy().hasHeightForWidth())
        self.tb_add_category.setSizePolicy(sizePolicy3)
        self.tb_add_category.setMinimumSize(QSize(20, 20))
        self.tb_add_category.setMaximumSize(QSize(20, 20))
        self.tb_add_category.setFont(font2)
        self.tb_add_category.setStyleSheet(u"color:green")

        self.gl_top.addWidget(self.tb_add_category, 9, 13, 1, 1)

        self.tb_remove_category = QToolButton(self.f_top)
        self.tb_remove_category.setObjectName(u"tb_remove_category")
        sizePolicy3.setHeightForWidth(self.tb_remove_category.sizePolicy().hasHeightForWidth())
        self.tb_remove_category.setSizePolicy(sizePolicy3)
        self.tb_remove_category.setMinimumSize(QSize(20, 20))
        self.tb_remove_category.setMaximumSize(QSize(20, 20))
        self.tb_remove_category.setFont(font2)
        self.tb_remove_category.setStyleSheet(u"color:red")

        self.gl_top.addWidget(self.tb_remove_category, 9, 14, 1, 1)

        self.pb_income = QPushButton(self.f_top)
        self.pb_income.setObjectName(u"pb_income")

        self.gl_top.addWidget(self.pb_income, 9, 0, 1, 1)

        self.pb_income_outcome = QPushButton(self.f_top)
        self.pb_income_outcome.setObjectName(u"pb_income_outcome")

        self.gl_top.addWidget(self.pb_income_outcome, 10, 0, 1, 2)


        self.gl_main.addWidget(self.f_top, 0, 0, 2, 3)

        self.w_analytics = QWidget(self.w_main)
        self.w_analytics.setObjectName(u"w_analytics")
        sizePolicy1.setHeightForWidth(self.w_analytics.sizePolicy().hasHeightForWidth())
        self.w_analytics.setSizePolicy(sizePolicy1)
        self.gl_analytics = QGridLayout(self.w_analytics)
        self.gl_analytics.setObjectName(u"gl_analytics")
        self.gl_analytics.setHorizontalSpacing(12)
        self.gl_analytics.setVerticalSpacing(0)
        self.l_analytics_by_categories = QLabel(self.w_analytics)
        self.l_analytics_by_categories.setObjectName(u"l_analytics_by_categories")
        sizePolicy3.setHeightForWidth(self.l_analytics_by_categories.sizePolicy().hasHeightForWidth())
        self.l_analytics_by_categories.setSizePolicy(sizePolicy3)

        self.gl_analytics.addWidget(self.l_analytics_by_categories, 2, 0, 1, 1)

        self.l_analytics = QLabel(self.w_analytics)
        self.l_analytics.setObjectName(u"l_analytics")
        sizePolicy3.setHeightForWidth(self.l_analytics.sizePolicy().hasHeightForWidth())
        self.l_analytics.setSizePolicy(sizePolicy3)
        self.l_analytics.setFont(font)

        self.gl_analytics.addWidget(self.l_analytics, 0, 0, 1, 1)

        self.l_analytics_by_price = QLabel(self.w_analytics)
        self.l_analytics_by_price.setObjectName(u"l_analytics_by_price")
        sizePolicy3.setHeightForWidth(self.l_analytics_by_price.sizePolicy().hasHeightForWidth())
        self.l_analytics_by_price.setSizePolicy(sizePolicy3)

        self.gl_analytics.addWidget(self.l_analytics_by_price, 4, 0, 1, 1)

        self.hl_abc = QHBoxLayout()
        self.hl_abc.setSpacing(0)
        self.hl_abc.setObjectName(u"hl_abc")
        self.pb_abc_average_price = QPushButton(self.w_analytics)
        self.pb_abc_average_price.setObjectName(u"pb_abc_average_price")
        sizePolicy3.setHeightForWidth(self.pb_abc_average_price.sizePolicy().hasHeightForWidth())
        self.pb_abc_average_price.setSizePolicy(sizePolicy3)
        self.pb_abc_average_price.setStyleSheet(u"color:blue")
        self.pb_abc_average_price.setFlat(True)

        self.hl_abc.addWidget(self.pb_abc_average_price)

        self.pb_abc_product_count = QPushButton(self.w_analytics)
        self.pb_abc_product_count.setObjectName(u"pb_abc_product_count")
        sizePolicy3.setHeightForWidth(self.pb_abc_product_count.sizePolicy().hasHeightForWidth())
        self.pb_abc_product_count.setSizePolicy(sizePolicy3)
        self.pb_abc_product_count.setStyleSheet(u"color:blue")
        self.pb_abc_product_count.setFlat(True)

        self.hl_abc.addWidget(self.pb_abc_product_count)

        self.pb_abc_total_weight = QPushButton(self.w_analytics)
        self.pb_abc_total_weight.setObjectName(u"pb_abc_total_weight")
        sizePolicy3.setHeightForWidth(self.pb_abc_total_weight.sizePolicy().hasHeightForWidth())
        self.pb_abc_total_weight.setSizePolicy(sizePolicy3)
        self.pb_abc_total_weight.setStyleSheet(u"color:blue")
        self.pb_abc_total_weight.setFlat(True)

        self.hl_abc.addWidget(self.pb_abc_total_weight)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_abc.addItem(self.horizontalSpacer_2)


        self.gl_analytics.addLayout(self.hl_abc, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_abp_product_distribution = QPushButton(self.w_analytics)
        self.pb_abp_product_distribution.setObjectName(u"pb_abp_product_distribution")
        sizePolicy3.setHeightForWidth(self.pb_abp_product_distribution.sizePolicy().hasHeightForWidth())
        self.pb_abp_product_distribution.setSizePolicy(sizePolicy3)
        self.pb_abp_product_distribution.setStyleSheet(u"color:blue")
        self.pb_abp_product_distribution.setFlat(True)

        self.horizontalLayout.addWidget(self.pb_abp_product_distribution)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gl_analytics.addLayout(self.horizontalLayout, 4, 1, 1, 1)


        self.gl_main.addWidget(self.w_analytics, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.w_main)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u0442 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.l_categories.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        ___qtreewidgetitem = self.treew_storage.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043b\u0430\u0434", None));
#if QT_CONFIG(tooltip)
        self.pb_outcome.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0437\u0442\u0438 \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044e", None))
#endif // QT_CONFIG(tooltip)
        self.pb_outcome.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0437", None))
        self.gb_metrics.setTitle("")
        self.l_inventory_count_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_outcome_last_week_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_products_count_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_outcome_last_week.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0437 (\u043d\u0435\u0434\u0435\u043b\u044f):", None))
        self.l_income_last_week_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_run_out.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u043b\u043e\u0441\u044c:", None))
        self.l_total_price.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0441\u043a\u043b\u0430\u0434\u0430:                        ", None))
        self.l_total_price_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_run_out_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_income_last_week.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u043e\u0437 (\u043d\u0435\u0434\u0435\u043b\u044f):", None))
        self.l_products_count.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432:", None))
        self.l_inventory_count.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435:", None))
        self.tb_add_product.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tb_remove_product.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.l_products.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0448\u0430 \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f", None))
        ___qtablewidgetitem = self.tw_products.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem1 = self.tw_products.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None));
        ___qtablewidgetitem2 = self.tw_products.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem3 = self.tw_products.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None));
        ___qtablewidgetitem4 = self.tw_products.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435", None));
        ___qtablewidgetitem5 = self.tw_products.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0441 (\u0433\u0440.)", None));
        ___qtablewidgetitem6 = self.tw_products.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 (\u20bd)", None));
        ___qtablewidgetitem7 = self.tw_products.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None));
        self.tb_add_category.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tb_remove_category.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(tooltip)
        self.pb_income.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0437\u0442\u0438 \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044e", None))
#endif // QT_CONFIG(tooltip)
        self.pb_income.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0437", None))
        self.pb_income_outcome.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0432\u0432\u043e\u0437\u0430 \u0438 \u0432\u044b\u0432\u043e\u0437\u0430", None))
        self.l_analytics_by_categories.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c:", None))
        self.l_analytics.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.l_analytics_by_price.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0446\u0435\u043d\u0435:", None))
        self.pb_abc_average_price.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0446\u0435\u043d\u0430", None))
        self.pb_abc_product_count.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432", None))
        self.pb_abc_total_weight.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0439 \u0432\u0435\u0441", None))
        self.pb_abp_product_distribution.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0446\u0435\u043d \u043d\u0430 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
    # retranslateUi

