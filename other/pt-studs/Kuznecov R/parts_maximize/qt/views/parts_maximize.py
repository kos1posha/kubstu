# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parts_maximize.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PartsMaximizeWindow(object):
    def setupUi(self, PartsMaximizeWindow):
        if not PartsMaximizeWindow.objectName():
            PartsMaximizeWindow.setObjectName(u"PartsMaximizeWindow")
        PartsMaximizeWindow.resize(500, 510)
        PartsMaximizeWindow.setMinimumSize(QSize(500, 510))
        PartsMaximizeWindow.setMaximumSize(QSize(500, 510))
        self.gl_main = QGridLayout(PartsMaximizeWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setContentsMargins(0, 0, 0, 0)
        self.tabw_steps = QTabWidget(PartsMaximizeWindow)
        self.tabw_steps.setObjectName(u"tabw_steps")
        self.tabw_steps.setMinimumSize(QSize(500, 510))
        self.tabw_steps.setMaximumSize(QSize(500, 510))
        self.tabw_steps.setTabPosition(QTabWidget.TabPosition.North)
        self.tabw_steps.setDocumentMode(True)
        self.tab_task = QWidget()
        self.tab_task.setObjectName(u"tab_task")
        self.vl_task = QVBoxLayout(self.tab_task)
        self.vl_task.setObjectName(u"vl_task")
        self.l_task_title = QLabel(self.tab_task)
        self.l_task_title.setObjectName(u"l_task_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_task_title.sizePolicy().hasHeightForWidth())
        self.l_task_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.l_task_title.setFont(font)
        self.l_task_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.vl_task.addWidget(self.l_task_title)

        self.l_task_text_1 = QLabel(self.tab_task)
        self.l_task_text_1.setObjectName(u"l_task_text_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_task_text_1.sizePolicy().hasHeightForWidth())
        self.l_task_text_1.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        self.l_task_text_1.setFont(font1)
        self.l_task_text_1.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_task_text_1.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_task_text_1.setWordWrap(True)
        self.l_task_text_1.setMargin(6)

        self.vl_task.addWidget(self.l_task_text_1)

        self.tw_task_args = QTableWidget(self.tab_task)
        if (self.tw_task_args.columnCount() < 6):
            self.tw_task_args.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_task_args.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_task_args.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_task_args.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_task_args.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_task_args.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_task_args.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tw_task_args.rowCount() < 7):
            self.tw_task_args.setRowCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_task_args.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_task_args.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_task_args.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_task_args.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_task_args.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_task_args.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_task_args.setVerticalHeaderItem(6, __qtablewidgetitem12)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font2);
        __qtablewidgetitem13.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font2);
        __qtablewidgetitem14.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(0, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_task_args.setItem(0, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font2);
        __qtablewidgetitem16.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(0, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font2);
        __qtablewidgetitem17.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(1, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font2);
        __qtablewidgetitem18.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(2, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font2);
        __qtablewidgetitem19.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(2, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font2);
        __qtablewidgetitem20.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(2, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font2);
        __qtablewidgetitem21.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(2, 4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font2);
        __qtablewidgetitem22.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(2, 5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font2);
        __qtablewidgetitem23.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(3, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFont(font2);
        __qtablewidgetitem24.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(4, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(4, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(4, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(4, 3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(4, 4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(4, 5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFont(font2);
        __qtablewidgetitem30.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(5, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(5, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(5, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(5, 3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(5, 4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(5, 5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font2);
        __qtablewidgetitem36.setFlags(Qt.ItemIsEnabled);
        self.tw_task_args.setItem(6, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(6, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(6, 2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(6, 3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(6, 4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tw_task_args.setItem(6, 5, __qtablewidgetitem41)
        self.tw_task_args.setObjectName(u"tw_task_args")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tw_task_args.sizePolicy().hasHeightForWidth())
        self.tw_task_args.setSizePolicy(sizePolicy2)
        self.tw_task_args.horizontalHeader().setVisible(False)
        self.tw_task_args.verticalHeader().setVisible(False)

        self.vl_task.addWidget(self.tw_task_args)

        self.l_task_text_2 = QLabel(self.tab_task)
        self.l_task_text_2.setObjectName(u"l_task_text_2")
        sizePolicy1.setHeightForWidth(self.l_task_text_2.sizePolicy().hasHeightForWidth())
        self.l_task_text_2.setSizePolicy(sizePolicy1)
        self.l_task_text_2.setFont(font1)
        self.l_task_text_2.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_task_text_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_task_text_2.setWordWrap(True)
        self.l_task_text_2.setMargin(6)

        self.vl_task.addWidget(self.l_task_text_2)

        self.tabw_steps.addTab(self.tab_task, "")
        self.tab_obj_func = QWidget()
        self.tab_obj_func.setObjectName(u"tab_obj_func")
        self.vl_obj_func = QVBoxLayout(self.tab_obj_func)
        self.vl_obj_func.setObjectName(u"vl_obj_func")
        self.l_obj_func_title = QLabel(self.tab_obj_func)
        self.l_obj_func_title.setObjectName(u"l_obj_func_title")
        sizePolicy.setHeightForWidth(self.l_obj_func_title.sizePolicy().hasHeightForWidth())
        self.l_obj_func_title.setSizePolicy(sizePolicy)
        self.l_obj_func_title.setFont(font)
        self.l_obj_func_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.vl_obj_func.addWidget(self.l_obj_func_title)

        self.l_obj_func_text_1 = QLabel(self.tab_obj_func)
        self.l_obj_func_text_1.setObjectName(u"l_obj_func_text_1")
        sizePolicy1.setHeightForWidth(self.l_obj_func_text_1.sizePolicy().hasHeightForWidth())
        self.l_obj_func_text_1.setSizePolicy(sizePolicy1)
        self.l_obj_func_text_1.setFont(font1)
        self.l_obj_func_text_1.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_obj_func_text_1.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_obj_func_text_1.setWordWrap(True)
        self.l_obj_func_text_1.setMargin(6)

        self.vl_obj_func.addWidget(self.l_obj_func_text_1)

        self.l_obj_func_def_1 = QLabel(self.tab_obj_func)
        self.l_obj_func_def_1.setObjectName(u"l_obj_func_def_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.l_obj_func_def_1.sizePolicy().hasHeightForWidth())
        self.l_obj_func_def_1.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.l_obj_func_def_1.setFont(font3)
        self.l_obj_func_def_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_obj_func_def_1.setMargin(4)

        self.vl_obj_func.addWidget(self.l_obj_func_def_1)

        self.l_obj_func_def_2 = QLabel(self.tab_obj_func)
        self.l_obj_func_def_2.setObjectName(u"l_obj_func_def_2")
        sizePolicy3.setHeightForWidth(self.l_obj_func_def_2.sizePolicy().hasHeightForWidth())
        self.l_obj_func_def_2.setSizePolicy(sizePolicy3)
        self.l_obj_func_def_2.setFont(font3)
        self.l_obj_func_def_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_obj_func_def_2.setMargin(4)

        self.vl_obj_func.addWidget(self.l_obj_func_def_2)

        self.l_obj_func_def_3 = QLabel(self.tab_obj_func)
        self.l_obj_func_def_3.setObjectName(u"l_obj_func_def_3")
        sizePolicy3.setHeightForWidth(self.l_obj_func_def_3.sizePolicy().hasHeightForWidth())
        self.l_obj_func_def_3.setSizePolicy(sizePolicy3)
        self.l_obj_func_def_3.setFont(font3)
        self.l_obj_func_def_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_obj_func_def_3.setMargin(4)

        self.vl_obj_func.addWidget(self.l_obj_func_def_3)

        self.l_obj_func_text_2 = QLabel(self.tab_obj_func)
        self.l_obj_func_text_2.setObjectName(u"l_obj_func_text_2")
        sizePolicy1.setHeightForWidth(self.l_obj_func_text_2.sizePolicy().hasHeightForWidth())
        self.l_obj_func_text_2.setSizePolicy(sizePolicy1)
        self.l_obj_func_text_2.setFont(font1)
        self.l_obj_func_text_2.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_obj_func_text_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_obj_func_text_2.setWordWrap(True)
        self.l_obj_func_text_2.setMargin(6)

        self.vl_obj_func.addWidget(self.l_obj_func_text_2)

        self.tabw_steps.addTab(self.tab_obj_func, "")
        self.tab_constraints = QWidget()
        self.tab_constraints.setObjectName(u"tab_constraints")
        self.vl_constraints = QVBoxLayout(self.tab_constraints)
        self.vl_constraints.setObjectName(u"vl_constraints")
        self.l_constraints_title = QLabel(self.tab_constraints)
        self.l_constraints_title.setObjectName(u"l_constraints_title")
        sizePolicy.setHeightForWidth(self.l_constraints_title.sizePolicy().hasHeightForWidth())
        self.l_constraints_title.setSizePolicy(sizePolicy)
        self.l_constraints_title.setFont(font)
        self.l_constraints_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.vl_constraints.addWidget(self.l_constraints_title)

        self.l_constraints_text_1 = QLabel(self.tab_constraints)
        self.l_constraints_text_1.setObjectName(u"l_constraints_text_1")
        sizePolicy1.setHeightForWidth(self.l_constraints_text_1.sizePolicy().hasHeightForWidth())
        self.l_constraints_text_1.setSizePolicy(sizePolicy1)
        self.l_constraints_text_1.setFont(font1)
        self.l_constraints_text_1.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_constraints_text_1.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_constraints_text_1.setWordWrap(True)
        self.l_constraints_text_1.setMargin(6)

        self.vl_constraints.addWidget(self.l_constraints_text_1)

        self.l_constraints_default = QLabel(self.tab_constraints)
        self.l_constraints_default.setObjectName(u"l_constraints_default")
        sizePolicy3.setHeightForWidth(self.l_constraints_default.sizePolicy().hasHeightForWidth())
        self.l_constraints_default.setSizePolicy(sizePolicy3)
        self.l_constraints_default.setFont(font3)
        self.l_constraints_default.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_constraints_default.setMargin(4)

        self.vl_constraints.addWidget(self.l_constraints_default)

        self.l_constraints_text_2 = QLabel(self.tab_constraints)
        self.l_constraints_text_2.setObjectName(u"l_constraints_text_2")
        sizePolicy1.setHeightForWidth(self.l_constraints_text_2.sizePolicy().hasHeightForWidth())
        self.l_constraints_text_2.setSizePolicy(sizePolicy1)
        self.l_constraints_text_2.setFont(font1)
        self.l_constraints_text_2.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_constraints_text_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_constraints_text_2.setWordWrap(True)
        self.l_constraints_text_2.setMargin(6)

        self.vl_constraints.addWidget(self.l_constraints_text_2)

        self.l_constraints_details_1 = QLabel(self.tab_constraints)
        self.l_constraints_details_1.setObjectName(u"l_constraints_details_1")
        sizePolicy3.setHeightForWidth(self.l_constraints_details_1.sizePolicy().hasHeightForWidth())
        self.l_constraints_details_1.setSizePolicy(sizePolicy3)
        self.l_constraints_details_1.setFont(font3)
        self.l_constraints_details_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_constraints_details_1.setMargin(4)

        self.vl_constraints.addWidget(self.l_constraints_details_1)

        self.l_constraints_details_2 = QLabel(self.tab_constraints)
        self.l_constraints_details_2.setObjectName(u"l_constraints_details_2")
        sizePolicy3.setHeightForWidth(self.l_constraints_details_2.sizePolicy().hasHeightForWidth())
        self.l_constraints_details_2.setSizePolicy(sizePolicy3)
        self.l_constraints_details_2.setFont(font3)
        self.l_constraints_details_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_constraints_details_2.setMargin(4)

        self.vl_constraints.addWidget(self.l_constraints_details_2)

        self.l_constraints_details_3 = QLabel(self.tab_constraints)
        self.l_constraints_details_3.setObjectName(u"l_constraints_details_3")
        sizePolicy3.setHeightForWidth(self.l_constraints_details_3.sizePolicy().hasHeightForWidth())
        self.l_constraints_details_3.setSizePolicy(sizePolicy3)
        self.l_constraints_details_3.setFont(font3)
        self.l_constraints_details_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_constraints_details_3.setMargin(4)

        self.vl_constraints.addWidget(self.l_constraints_details_3)

        self.tabw_steps.addTab(self.tab_constraints, "")
        self.tab_lp = QWidget()
        self.tab_lp.setObjectName(u"tab_lp")
        self.vl_lp = QVBoxLayout(self.tab_lp)
        self.vl_lp.setObjectName(u"vl_lp")
        self.l_lp_title = QLabel(self.tab_lp)
        self.l_lp_title.setObjectName(u"l_lp_title")
        sizePolicy.setHeightForWidth(self.l_lp_title.sizePolicy().hasHeightForWidth())
        self.l_lp_title.setSizePolicy(sizePolicy)
        self.l_lp_title.setFont(font)
        self.l_lp_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.vl_lp.addWidget(self.l_lp_title)

        self.l_lp_text_1 = QLabel(self.tab_lp)
        self.l_lp_text_1.setObjectName(u"l_lp_text_1")
        sizePolicy1.setHeightForWidth(self.l_lp_text_1.sizePolicy().hasHeightForWidth())
        self.l_lp_text_1.setSizePolicy(sizePolicy1)
        self.l_lp_text_1.setFont(font1)
        self.l_lp_text_1.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_lp_text_1.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_text_1.setWordWrap(True)
        self.l_lp_text_1.setMargin(6)

        self.vl_lp.addWidget(self.l_lp_text_1)

        self.l_lp_sense = QLabel(self.tab_lp)
        self.l_lp_sense.setObjectName(u"l_lp_sense")
        sizePolicy.setHeightForWidth(self.l_lp_sense.sizePolicy().hasHeightForWidth())
        self.l_lp_sense.setSizePolicy(sizePolicy)
        self.l_lp_sense.setFont(font3)
        self.l_lp_sense.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_sense.setMargin(4)

        self.vl_lp.addWidget(self.l_lp_sense)

        self.l_lp_text_4 = QLabel(self.tab_lp)
        self.l_lp_text_4.setObjectName(u"l_lp_text_4")
        sizePolicy1.setHeightForWidth(self.l_lp_text_4.sizePolicy().hasHeightForWidth())
        self.l_lp_text_4.setSizePolicy(sizePolicy1)
        self.l_lp_text_4.setFont(font1)
        self.l_lp_text_4.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_lp_text_4.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_text_4.setWordWrap(True)
        self.l_lp_text_4.setMargin(6)

        self.vl_lp.addWidget(self.l_lp_text_4)

        self.l_lp_details_set = QLabel(self.tab_lp)
        self.l_lp_details_set.setObjectName(u"l_lp_details_set")
        sizePolicy3.setHeightForWidth(self.l_lp_details_set.sizePolicy().hasHeightForWidth())
        self.l_lp_details_set.setSizePolicy(sizePolicy3)
        self.l_lp_details_set.setFont(font3)
        self.l_lp_details_set.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_details_set.setMargin(4)

        self.vl_lp.addWidget(self.l_lp_details_set)

        self.l_lp_text_2 = QLabel(self.tab_lp)
        self.l_lp_text_2.setObjectName(u"l_lp_text_2")
        sizePolicy1.setHeightForWidth(self.l_lp_text_2.sizePolicy().hasHeightForWidth())
        self.l_lp_text_2.setSizePolicy(sizePolicy1)
        self.l_lp_text_2.setFont(font1)
        self.l_lp_text_2.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_lp_text_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_text_2.setWordWrap(True)
        self.l_lp_text_2.setMargin(6)

        self.vl_lp.addWidget(self.l_lp_text_2)

        self.l_lp_obj_func = QLabel(self.tab_lp)
        self.l_lp_obj_func.setObjectName(u"l_lp_obj_func")
        sizePolicy3.setHeightForWidth(self.l_lp_obj_func.sizePolicy().hasHeightForWidth())
        self.l_lp_obj_func.setSizePolicy(sizePolicy3)
        self.l_lp_obj_func.setFont(font3)
        self.l_lp_obj_func.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_obj_func.setMargin(4)

        self.vl_lp.addWidget(self.l_lp_obj_func)

        self.l_lp_text_3 = QLabel(self.tab_lp)
        self.l_lp_text_3.setObjectName(u"l_lp_text_3")
        sizePolicy1.setHeightForWidth(self.l_lp_text_3.sizePolicy().hasHeightForWidth())
        self.l_lp_text_3.setSizePolicy(sizePolicy1)
        self.l_lp_text_3.setFont(font1)
        self.l_lp_text_3.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_lp_text_3.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_text_3.setWordWrap(True)
        self.l_lp_text_3.setMargin(6)

        self.vl_lp.addWidget(self.l_lp_text_3)

        self.l_lp_constraints_details_1 = QLabel(self.tab_lp)
        self.l_lp_constraints_details_1.setObjectName(u"l_lp_constraints_details_1")
        sizePolicy3.setHeightForWidth(self.l_lp_constraints_details_1.sizePolicy().hasHeightForWidth())
        self.l_lp_constraints_details_1.setSizePolicy(sizePolicy3)
        self.l_lp_constraints_details_1.setFont(font3)
        self.l_lp_constraints_details_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_constraints_details_1.setMargin(4)

        self.vl_lp.addWidget(self.l_lp_constraints_details_1)

        self.l_lp_constraints_details_2 = QLabel(self.tab_lp)
        self.l_lp_constraints_details_2.setObjectName(u"l_lp_constraints_details_2")
        sizePolicy3.setHeightForWidth(self.l_lp_constraints_details_2.sizePolicy().hasHeightForWidth())
        self.l_lp_constraints_details_2.setSizePolicy(sizePolicy3)
        self.l_lp_constraints_details_2.setFont(font3)
        self.l_lp_constraints_details_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_constraints_details_2.setMargin(4)

        self.vl_lp.addWidget(self.l_lp_constraints_details_2)

        self.l_lp_constraints_details_3 = QLabel(self.tab_lp)
        self.l_lp_constraints_details_3.setObjectName(u"l_lp_constraints_details_3")
        sizePolicy3.setHeightForWidth(self.l_lp_constraints_details_3.sizePolicy().hasHeightForWidth())
        self.l_lp_constraints_details_3.setSizePolicy(sizePolicy3)
        self.l_lp_constraints_details_3.setFont(font3)
        self.l_lp_constraints_details_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_constraints_details_3.setMargin(4)

        self.vl_lp.addWidget(self.l_lp_constraints_details_3)

        self.l_lp_constraints_default_1 = QLabel(self.tab_lp)
        self.l_lp_constraints_default_1.setObjectName(u"l_lp_constraints_default_1")
        sizePolicy3.setHeightForWidth(self.l_lp_constraints_default_1.sizePolicy().hasHeightForWidth())
        self.l_lp_constraints_default_1.setSizePolicy(sizePolicy3)
        self.l_lp_constraints_default_1.setFont(font3)
        self.l_lp_constraints_default_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_constraints_default_1.setMargin(4)

        self.vl_lp.addWidget(self.l_lp_constraints_default_1)

        self.l_lp_constraints_default_2 = QLabel(self.tab_lp)
        self.l_lp_constraints_default_2.setObjectName(u"l_lp_constraints_default_2")
        sizePolicy3.setHeightForWidth(self.l_lp_constraints_default_2.sizePolicy().hasHeightForWidth())
        self.l_lp_constraints_default_2.setSizePolicy(sizePolicy3)
        self.l_lp_constraints_default_2.setFont(font3)
        self.l_lp_constraints_default_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_constraints_default_2.setMargin(4)

        self.vl_lp.addWidget(self.l_lp_constraints_default_2)

        self.pb_lp_solve = QPushButton(self.tab_lp)
        self.pb_lp_solve.setObjectName(u"pb_lp_solve")

        self.vl_lp.addWidget(self.pb_lp_solve)

        self.tabw_steps.addTab(self.tab_lp, "")
        self.tab_lp_additional = QWidget()
        self.tab_lp_additional.setObjectName(u"tab_lp_additional")
        self.vl_lpa = QVBoxLayout(self.tab_lp_additional)
        self.vl_lpa.setObjectName(u"vl_lpa")
        self.l_lpa_title = QLabel(self.tab_lp_additional)
        self.l_lpa_title.setObjectName(u"l_lpa_title")
        sizePolicy.setHeightForWidth(self.l_lpa_title.sizePolicy().hasHeightForWidth())
        self.l_lpa_title.setSizePolicy(sizePolicy)
        self.l_lpa_title.setFont(font)
        self.l_lpa_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.vl_lpa.addWidget(self.l_lpa_title)

        self.l_lpa_text_1 = QLabel(self.tab_lp_additional)
        self.l_lpa_text_1.setObjectName(u"l_lpa_text_1")
        sizePolicy1.setHeightForWidth(self.l_lpa_text_1.sizePolicy().hasHeightForWidth())
        self.l_lpa_text_1.setSizePolicy(sizePolicy1)
        self.l_lpa_text_1.setFont(font1)
        self.l_lpa_text_1.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_lpa_text_1.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_text_1.setWordWrap(True)
        self.l_lpa_text_1.setMargin(6)

        self.vl_lpa.addWidget(self.l_lpa_text_1)

        self.l_lpa_sense = QLabel(self.tab_lp_additional)
        self.l_lpa_sense.setObjectName(u"l_lpa_sense")
        sizePolicy.setHeightForWidth(self.l_lpa_sense.sizePolicy().hasHeightForWidth())
        self.l_lpa_sense.setSizePolicy(sizePolicy)
        self.l_lpa_sense.setFont(font3)
        self.l_lpa_sense.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_sense.setMargin(4)

        self.vl_lpa.addWidget(self.l_lpa_sense)

        self.l_lpa_text_2 = QLabel(self.tab_lp_additional)
        self.l_lpa_text_2.setObjectName(u"l_lpa_text_2")
        sizePolicy1.setHeightForWidth(self.l_lpa_text_2.sizePolicy().hasHeightForWidth())
        self.l_lpa_text_2.setSizePolicy(sizePolicy1)
        self.l_lpa_text_2.setFont(font1)
        self.l_lpa_text_2.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_lpa_text_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_text_2.setWordWrap(True)
        self.l_lpa_text_2.setMargin(6)

        self.vl_lpa.addWidget(self.l_lpa_text_2)

        self.l_lpa_details_set = QLabel(self.tab_lp_additional)
        self.l_lpa_details_set.setObjectName(u"l_lpa_details_set")
        sizePolicy3.setHeightForWidth(self.l_lpa_details_set.sizePolicy().hasHeightForWidth())
        self.l_lpa_details_set.setSizePolicy(sizePolicy3)
        self.l_lpa_details_set.setFont(font3)
        self.l_lpa_details_set.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_details_set.setMargin(4)

        self.vl_lpa.addWidget(self.l_lpa_details_set)

        self.l_lpa_text_3 = QLabel(self.tab_lp_additional)
        self.l_lpa_text_3.setObjectName(u"l_lpa_text_3")
        sizePolicy1.setHeightForWidth(self.l_lpa_text_3.sizePolicy().hasHeightForWidth())
        self.l_lpa_text_3.setSizePolicy(sizePolicy1)
        self.l_lpa_text_3.setFont(font1)
        self.l_lpa_text_3.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_lpa_text_3.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_text_3.setWordWrap(True)
        self.l_lpa_text_3.setMargin(6)

        self.vl_lpa.addWidget(self.l_lpa_text_3)

        self.l_lpa_obj_func = QLabel(self.tab_lp_additional)
        self.l_lpa_obj_func.setObjectName(u"l_lpa_obj_func")
        sizePolicy3.setHeightForWidth(self.l_lpa_obj_func.sizePolicy().hasHeightForWidth())
        self.l_lpa_obj_func.setSizePolicy(sizePolicy3)
        self.l_lpa_obj_func.setFont(font3)
        self.l_lpa_obj_func.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_obj_func.setMargin(4)

        self.vl_lpa.addWidget(self.l_lpa_obj_func)

        self.l_lpa_text_4 = QLabel(self.tab_lp_additional)
        self.l_lpa_text_4.setObjectName(u"l_lpa_text_4")
        sizePolicy1.setHeightForWidth(self.l_lpa_text_4.sizePolicy().hasHeightForWidth())
        self.l_lpa_text_4.setSizePolicy(sizePolicy1)
        self.l_lpa_text_4.setFont(font1)
        self.l_lpa_text_4.setStyleSheet(u"border:1px solid rgb(60,60,60);border-radius:5px;background:rgb(40,40,40)")
        self.l_lpa_text_4.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_text_4.setWordWrap(True)
        self.l_lpa_text_4.setMargin(6)

        self.vl_lpa.addWidget(self.l_lpa_text_4)

        self.l_lpa_constraints_details_1 = QLabel(self.tab_lp_additional)
        self.l_lpa_constraints_details_1.setObjectName(u"l_lpa_constraints_details_1")
        sizePolicy3.setHeightForWidth(self.l_lpa_constraints_details_1.sizePolicy().hasHeightForWidth())
        self.l_lpa_constraints_details_1.setSizePolicy(sizePolicy3)
        self.l_lpa_constraints_details_1.setFont(font3)
        self.l_lpa_constraints_details_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_constraints_details_1.setMargin(4)

        self.vl_lpa.addWidget(self.l_lpa_constraints_details_1)

        self.l_lpa_constraints_details_2 = QLabel(self.tab_lp_additional)
        self.l_lpa_constraints_details_2.setObjectName(u"l_lpa_constraints_details_2")
        sizePolicy3.setHeightForWidth(self.l_lpa_constraints_details_2.sizePolicy().hasHeightForWidth())
        self.l_lpa_constraints_details_2.setSizePolicy(sizePolicy3)
        self.l_lpa_constraints_details_2.setFont(font3)
        self.l_lpa_constraints_details_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_constraints_details_2.setMargin(4)

        self.vl_lpa.addWidget(self.l_lpa_constraints_details_2)

        self.l_lpa_constraints_details_3 = QLabel(self.tab_lp_additional)
        self.l_lpa_constraints_details_3.setObjectName(u"l_lpa_constraints_details_3")
        sizePolicy3.setHeightForWidth(self.l_lpa_constraints_details_3.sizePolicy().hasHeightForWidth())
        self.l_lpa_constraints_details_3.setSizePolicy(sizePolicy3)
        self.l_lpa_constraints_details_3.setFont(font3)
        self.l_lpa_constraints_details_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lpa_constraints_details_3.setMargin(4)

        self.vl_lpa.addWidget(self.l_lpa_constraints_details_3)

        self.l_lp_constraints_default_4 = QLabel(self.tab_lp_additional)
        self.l_lp_constraints_default_4.setObjectName(u"l_lp_constraints_default_4")
        sizePolicy3.setHeightForWidth(self.l_lp_constraints_default_4.sizePolicy().hasHeightForWidth())
        self.l_lp_constraints_default_4.setSizePolicy(sizePolicy3)
        self.l_lp_constraints_default_4.setFont(font3)
        self.l_lp_constraints_default_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_constraints_default_4.setMargin(4)

        self.vl_lpa.addWidget(self.l_lp_constraints_default_4)

        self.l_lp_constraints_default_3 = QLabel(self.tab_lp_additional)
        self.l_lp_constraints_default_3.setObjectName(u"l_lp_constraints_default_3")
        sizePolicy3.setHeightForWidth(self.l_lp_constraints_default_3.sizePolicy().hasHeightForWidth())
        self.l_lp_constraints_default_3.setSizePolicy(sizePolicy3)
        self.l_lp_constraints_default_3.setFont(font3)
        self.l_lp_constraints_default_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_lp_constraints_default_3.setMargin(4)

        self.vl_lpa.addWidget(self.l_lp_constraints_default_3)

        self.pb_lp_solve_2 = QPushButton(self.tab_lp_additional)
        self.pb_lp_solve_2.setObjectName(u"pb_lp_solve_2")

        self.vl_lpa.addWidget(self.pb_lp_solve_2)

        self.tabw_steps.addTab(self.tab_lp_additional, "")

        self.gl_main.addWidget(self.tabw_steps, 0, 0, 1, 1)


        self.retranslateUi(PartsMaximizeWindow)

        self.tabw_steps.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PartsMaximizeWindow)
    # setupUi

    def retranslateUi(self, PartsMaximizeWindow):
        PartsMaximizeWindow.setWindowTitle(QCoreApplication.translate("PartsMaximizeWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f \u0447\u0438\u0441\u043b\u0430 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432 \u0434\u0435\u0442\u0430\u043b\u0435\u0439", None))
        self.l_task_title.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 - \u0412\u0430\u0440\u0438\u0430\u043d\u0442 6", None))
        self.l_task_text_1.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0418\u0437 500 \u043b\u0438\u0441\u0442\u043e\u0432 \u0436\u0435\u043b\u0435\u0437\u0430 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0438 300 \u043b\u0438\u0441\u0442\u043e\u0432 \u0436\u0435\u043b\u0435\u0437\u0430 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u043c\u0438 \u0441\u043f\u043e\u0441\u043e\u0431\u0430\u043c\u0438 \u0432\u044b\u043a\u0440\u0430\u0438\u0432\u0430\u044e\u0442\u0441\u044f \u0442\u0440\u0438 \u0432\u0438\u0434\u0430 \u0434\u0435\u0442\u0430\u043b\u0435\u0439. \u0414\u0430\u043d\u044b \u043d\u043e\u0440\u043c\u044b \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u0432\u044b\u0445\u043e\u0434\u0430 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u043f\u043e \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u043c \u0441\u043f\u043e\u0441\u043e\u0431\u0430\u043c.", None))

        __sortingEnabled = self.tw_task_args.isSortingEnabled()
        self.tw_task_args.setSortingEnabled(False)
        ___qtablewidgetitem = self.tw_task_args.item(0, 0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0412\u0438\u0434 \u0434\u0435\u0442\u0430\u043b\u0438", None));
        ___qtablewidgetitem1 = self.tw_task_args.item(0, 1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041b\u0438\u0441\u0442\u044b \u0440\u0430\u0437\u043c\u0435\u0440\u0430 1", None));
        ___qtablewidgetitem2 = self.tw_task_args.item(0, 4)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041b\u0438\u0441\u0442 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 2", None));
        ___qtablewidgetitem3 = self.tw_task_args.item(1, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431\u044b \u0440\u0430\u0441\u043a\u0440\u043e\u044f", None));
        ___qtablewidgetitem4 = self.tw_task_args.item(2, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PartsMaximizeWindow", u"1", None));
        ___qtablewidgetitem5 = self.tw_task_args.item(2, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PartsMaximizeWindow", u"2", None));
        ___qtablewidgetitem6 = self.tw_task_args.item(2, 3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PartsMaximizeWindow", u"3", None));
        ___qtablewidgetitem7 = self.tw_task_args.item(2, 4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PartsMaximizeWindow", u"4", None));
        ___qtablewidgetitem8 = self.tw_task_args.item(2, 5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PartsMaximizeWindow", u"5", None));
        ___qtablewidgetitem9 = self.tw_task_args.item(3, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0442\u0430\u043b\u0435\u0439", None));
        ___qtablewidgetitem10 = self.tw_task_args.item(4, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PartsMaximizeWindow", u"1", None));
        ___qtablewidgetitem11 = self.tw_task_args.item(4, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PartsMaximizeWindow", u"0", None));
        ___qtablewidgetitem12 = self.tw_task_args.item(4, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PartsMaximizeWindow", u"2", None));
        ___qtablewidgetitem13 = self.tw_task_args.item(4, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PartsMaximizeWindow", u"9", None));
        ___qtablewidgetitem14 = self.tw_task_args.item(4, 4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("PartsMaximizeWindow", u"6", None));
        ___qtablewidgetitem15 = self.tw_task_args.item(4, 5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("PartsMaximizeWindow", u"5", None));
        ___qtablewidgetitem16 = self.tw_task_args.item(5, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("PartsMaximizeWindow", u"2", None));
        ___qtablewidgetitem17 = self.tw_task_args.item(5, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("PartsMaximizeWindow", u"4", None));
        ___qtablewidgetitem18 = self.tw_task_args.item(5, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("PartsMaximizeWindow", u"3", None));
        ___qtablewidgetitem19 = self.tw_task_args.item(5, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("PartsMaximizeWindow", u"4", None));
        ___qtablewidgetitem20 = self.tw_task_args.item(5, 4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("PartsMaximizeWindow", u"5", None));
        ___qtablewidgetitem21 = self.tw_task_args.item(5, 5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("PartsMaximizeWindow", u"4", None));
        ___qtablewidgetitem22 = self.tw_task_args.item(6, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("PartsMaximizeWindow", u"3", None));
        ___qtablewidgetitem23 = self.tw_task_args.item(6, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("PartsMaximizeWindow", u"10", None));
        ___qtablewidgetitem24 = self.tw_task_args.item(6, 2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("PartsMaximizeWindow", u"16", None));
        ___qtablewidgetitem25 = self.tw_task_args.item(6, 3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("PartsMaximizeWindow", u"0", None));
        ___qtablewidgetitem26 = self.tw_task_args.item(6, 4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("PartsMaximizeWindow", u"8", None));
        ___qtablewidgetitem27 = self.tw_task_args.item(6, 5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("PartsMaximizeWindow", u"0", None));
        self.tw_task_args.setSortingEnabled(__sortingEnabled)

        self.l_task_text_2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432 \u0434\u0435\u0442\u0430\u043b\u0435\u0439, \u0435\u0441\u043b\u0438 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442 \u0441\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 \u0447\u0435\u0442\u044b\u0440\u0435\u0445 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u0432\u0438\u0434\u0430 1, \u0442\u0440\u0435\u0445 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u0432\u0438\u0434\u0430 2 \u0438 \u0434\u0432\u0443\u0445 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u0432\u0438\u0434\u0430 3. \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c, \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043b\u0438\u0441\u0442\u043e\u0432 \u0436\u0435\u043b\u0435\u0437\u0430 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 2 \u0440\u0430\u0441\u043a\u0440\u0430\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043f\u043e"
                        " \u043f\u0435\u0440\u0432\u043e\u043c\u0443 \u0441\u043f\u043e\u0441\u043e\u0431\u0443, \u043a\u0430\u043a\u043e\u0432\u043e \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432, \u043d\u0430 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u0441\u044f \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432, \u0435\u0441\u043b\u0438 \u0432 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442 \u0440\u0435\u0448\u0435\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0440\u0435\u0442\u044c\u044e \u0434\u0435\u0442\u0430\u043b\u044c \u0432\u0438\u0434\u0430 3?", None))
        self.tabw_steps.setTabText(self.tabw_steps.indexOf(self.tab_task), QCoreApplication.translate("PartsMaximizeWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.l_obj_func_title.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.l_obj_func_text_1.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>\u0414\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0446\u0435\u043b\u0435\u0432\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0442\u0432\u0435\u0442\u0438\u0442\u044c \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u044b:</p><p>* \u0427\u0442\u043e \u043c\u044b \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0438\u0440\u0443\u0435\u043c? <br/>** \u041c\u0430\u043a\u0441\u0438\u043c\u0438\u0437\u0438\u0440\u0443\u0435\u043c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432 \u0434\u0435\u0442\u0430\u043b\u0435\u0439<br/>* \u0427\u0442\u043e \u043c\u044b \u0438\u0449\u0435\u043c? <br/>** \u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0440\u0430\u0437 \u0438 \u043a\u0430\u043a\u0438\u043c\u0438 \u0441\u043f\u043e\u0441\u043e\u0431\u043e\u043c \u043d\u0430\u043c \u043d\u0430\u0434\u043e \u0440"
                        "\u0430\u0441\u043a\u0440\u043e\u0438\u0442\u044c \u043b\u0438\u0441\u0442\u044b \u043c\u0435\u0442\u0430\u043b\u043b\u0430</p><p>\u0412\u0441\u0435\u0433\u043e \u0438\u043c\u0435\u0435\u0442\u0441\u044f 5 \u0441\u043f\u043e\u0441\u043e\u0431\u043e\u0432 \u0440\u0430\u0441\u043a\u0440\u043e\u0438\u0442\u044c \u043b\u0438\u0441\u0442 \u043c\u0435\u0442\u0430\u043b\u043b\u0430. \u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0442 \u0441\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 4 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 1-\u0433\u043e \u0432\u0438\u0434\u0430, 3 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 2-\u0433\u043e \u0432\u0438\u0434\u0430 \u0438 2 \u0434\u0435\u0442\u0430\u043b\u0435\u0439 3-\u0433\u043e \u0432\u0438\u0434\u0430. \u0421\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e, \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u043e\u0432 \u0431\u0443\u0434\u0435\u0442 \u0432\u043e \u0441\u0442\u043e\u043b\u044c\u043a"
                        "\u043e \u0440\u0430\u0437 \u043c\u0435\u043d\u044c\u0448\u0435 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0432\u0438\u0434\u0430 \u0434\u0435\u0442\u0430\u043b\u0435\u0439, \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u044d\u0442\u043e \u0432\u0438\u0434\u0430 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0434\u043b\u044f \u0441\u0431\u043e\u0440\u0430 1 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0430. \u0422\u0430\u043a\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c, \u043c\u044b \u0438\u043c\u0435\u0435\u043c 3 \u0442\u043e\u0436\u0434\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u043f\u043e\u0441\u043e\u0431\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0446\u0435\u043b\u0435\u0432\u0443\u044e \u0444\u0443\u043d\u043a\u0446\u0438\u044e:</p></body></html>", None))
        self.l_obj_func_text_2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>\u0413\u0434\u0435 x<span style=\" vertical-align:sub;\">1</span>, x<span style=\" vertical-align:sub;\">2</span>, x<span style=\" vertical-align:sub;\">3</span>, x<span style=\" vertical-align:sub;\">4</span> \u0438 x<span style=\" vertical-align:sub;\">5</span> - \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435, \u043e\u0442\u0440\u0430\u0436\u0430\u044e\u0449\u0438\u0435 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043b\u0438\u0441\u0442\u043e\u0432 \u043c\u0435\u0442\u0430\u043b\u043b\u0430 \u043c\u044b \u0440\u0430\u0441\u043a\u0440\u043e\u0438\u043b\u0438 1-\u044b\u043c, 2-\u044b\u043c, 3-\u0438\u043c, 4-\u044b\u043c \u0438 5-\u044b\u043c \u0441\u043f\u043e\u0441\u043e\u0431\u0430\u043c\u0438 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e.</p></body></html>", None))
        self.tabw_steps.setTabText(self.tabw_steps.indexOf(self.tab_obj_func), QCoreApplication.translate("PartsMaximizeWindow", u"\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.l_constraints_title.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f", None))
        self.l_constraints_text_1.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>\u041b\u0438\u0441\u0442\u044b \u0440\u0430\u0437\u043c\u0435\u0440\u0430 1 \u043f\u0440\u0438\u0433\u043e\u0434\u043d\u044b \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f 1-\u0433\u043e, 2-\u0433\u043e \u0438 3-\u0433\u043e \u0441\u043f\u043e\u0441\u043e\u0431\u043e\u0432 \u0440\u0430\u0441\u043a\u0440\u043e\u0439\u043a\u0438. \u0410\u043d\u0430\u043b\u043e\u0433\u0438\u0447\u043d\u043e \u043b\u0438\u0441\u0442\u044b \u0440\u0430\u0437\u043c\u0435\u0440\u0430 2 - \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f 4-\u0433\u043e \u0438 5-\u0433\u043e \u0441\u043f\u043e\u0441\u043e\u0431\u043e\u0432. \u0423 \u043d\u0430\u0441 \u043b\u0438\u0448\u044c 500 \u043b\u0438\u0441\u0442\u043e\u0432 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 1 \u0438 300 \u043b\u0438\u0441\u0442\u043e\u0432 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 2, \u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e, \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f \u043a"
                        "\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u043b\u0438\u0441\u0442\u043e\u0432 \u043c\u043e\u0436\u043d\u043e \u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c:</p></body></html>", None))
        self.l_constraints_default.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>&nbsp;  x<span style=\" vertical-align:sub;\">1</span> + x<span style=\" vertical-align:sub;\">2</span> + x<span style=\" vertical-align:sub;\">3</span> \u2264 500</p><p>&nbsp;  x<span style=\" vertical-align:sub;\">4</span> + x<span style=\" vertical-align:sub;\">5</span> \u2264 300</p></body></html>", None))
        self.l_constraints_text_2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>\u0422\u0430\u043a\u0436\u0435 \u043d\u0430\u043c \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0435\u0449\u0435 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439, \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0445 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u0432 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0435. \u0414\u0435\u043b\u043e \u0432 \u0442\u043e\u043c, \u0447\u0442\u043e \u043d\u0430\u0448\u0430 \u0446\u0435\u043b\u0435\u0432\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u043d\u0435 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u0442 \u0442\u043e\u0433\u043e, \u0447\u0442\u043e \u0434\u043b\u044f \u0441\u0431\u043e\u0440\u0430 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0430 \u043d\u0443\u0436\u043d\u043e 3 \u0432\u0438\u0434\u0430 \u0434\u0435\u0442\u0430"
                        "\u043b\u0435\u0439, \u0430 \u043d\u0435 \u0442\u043e\u043b\u044c\u043a\u043e 1. \u041c\u044b \u043c\u043e\u0436\u0435\u043c \u0438\u0441\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u044d\u0442\u043e, \u0432\u0432\u0435\u0434\u044f \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f, \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0435 \u043d\u0430 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0442\u0430\u043b\u0435\u0439 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0434\u0440\u0443\u0433 \u0434\u0440\u0443\u0433\u0430.</p><p>\u0423\u043a\u0430\u0436\u0435\u043c \u044d\u0442\u043e \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u043f\u043e\u043f\u0430\u0440\u043d\u043e \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u0432\u0438\u0434\u043e\u0432 \u0434\u0435\u0442\u0430\u043b\u0435\u0439:</p></body></html>", None))
        self.tabw_steps.setTabText(self.tabw_steps.indexOf(self.tab_constraints), QCoreApplication.translate("PartsMaximizeWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f", None))
        self.l_lp_title.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0420\u0435\u0448\u0438\u043c \u0437\u0430\u0434\u0430\u0447\u0443 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.l_lp_text_1.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438:", None))
        self.l_lp_sense.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>&nbsp; \u041c\u0430\u043a\u0441\u0438\u043c\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c</p></body></html>", None))
        self.l_lp_text_4.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0421\u043e\u0441\u0442\u0430\u0432 \u043d\u0430\u0431\u043e\u0440\u0430 (\u0441\u043e\u0433\u043b\u0430\u0441\u043d\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044f\u043c \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0437\u0430\u0434\u0430\u0447\u0438):", None))
        self.l_lp_details_set.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>&nbsp; 4 \u0434\u0435\u0442\u0430\u043b\u0438 1-\u0433\u043e \u0432\u0438\u0434\u0430, 3 \u0434\u0435\u0442\u0430\u043b\u0438 2-\u0433\u043e \u0432\u0438\u0434\u0430, 2 \u0434\u0435\u0442\u0430\u043b\u0438 3-\u0433\u043e \u0432\u0438\u0434\u0430</p></body></html>", None))
        self.l_lp_text_2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f (\u0438\u0437 3 \u0442\u043e\u0436\u0434\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0432\u044b\u0431\u0440\u0430\u043d\u0430 \u043f\u0435\u0440\u0432\u0430\u044f):", None))
        self.l_lp_obj_func.setText("")
        self.l_lp_text_3.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f:", None))
        self.l_lp_constraints_default_1.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>\u00a0 x<span style=\" vertical-align:sub;\">1</span> + x<span style=\" vertical-align:sub;\">2</span> + x<span style=\" vertical-align:sub;\">3</span> \u2264 500</p></body></html>", None))
        self.l_lp_constraints_default_2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>\u00a0 x<span style=\" vertical-align:sub;\">4</span> + x<span style=\" vertical-align:sub;\">5</span> \u2264 300</p></body></html>", None))
        self.pb_lp_solve.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.tabw_steps.setTabText(self.tabw_steps.indexOf(self.tab_lp), QCoreApplication.translate("PartsMaximizeWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.l_lpa_title.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0420\u0435\u0448\u0438\u043c \u0437\u0430\u0434\u0430\u0447\u0443 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.l_lpa_text_1.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438:", None))
        self.l_lpa_sense.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>&nbsp; \u041c\u0430\u043a\u0441\u0438\u043c\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c</p></body></html>", None))
        self.l_lpa_text_2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0421\u043e\u0441\u0442\u0430\u0432 \u043d\u0430\u0431\u043e\u0440\u0430 (\u0441\u043e\u0433\u043b\u0430\u0441\u043d\u043e \u0443\u0441\u043b\u043e\u0432\u0438\u044f\u043c \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0437\u0430\u0434\u0430\u0447\u0438):", None))
        self.l_lpa_details_set.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>\u00a0 4 \u0434\u0435\u0442\u0430\u043b\u0438 1-\u0433\u043e \u0432\u0438\u0434\u0430, 3 \u0434\u0435\u0442\u0430\u043b\u0438 2-\u0433\u043e \u0432\u0438\u0434\u0430, 3 \u0434\u0435\u0442\u0430\u043b\u0438 3-\u0433\u043e \u0432\u0438\u0434\u0430</p></body></html>", None))
        self.l_lpa_text_3.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f (\u0438\u0437 3 \u0442\u043e\u0436\u0434\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0432\u044b\u0431\u0440\u0430\u043d\u0430 \u043f\u0435\u0440\u0432\u0430\u044f):", None))
        self.l_lpa_obj_func.setText("")
        self.l_lpa_text_4.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f:", None))
        self.l_lp_constraints_default_4.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>\u00a0 x<span style=\" vertical-align:sub;\">1</span> + x<span style=\" vertical-align:sub;\">2</span> + x<span style=\" vertical-align:sub;\">3</span> \u2264 500</p></body></html>", None))
        self.l_lp_constraints_default_3.setText(QCoreApplication.translate("PartsMaximizeWindow", u"<html><head/><body><p>\u00a0 x<span style=\" vertical-align:sub;\">4</span> + x<span style=\" vertical-align:sub;\">5</span> \u2264 300</p></body></html>", None))
        self.pb_lp_solve_2.setText(QCoreApplication.translate("PartsMaximizeWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.tabw_steps.setTabText(self.tabw_steps.indexOf(self.tab_lp_additional), QCoreApplication.translate("PartsMaximizeWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e", None))
    # retranslateUi

