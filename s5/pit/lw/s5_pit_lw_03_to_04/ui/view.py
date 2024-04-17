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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PainterWindow(object):
    def setupUi(self, PainterWindow):
        if not PainterWindow.objectName():
            PainterWindow.setObjectName(u"PainterWindow")
        PainterWindow.resize(600, 500)
        PainterWindow.setMinimumSize(QSize(600, 500))
        PainterWindow.setMaximumSize(QSize(600, 500))
        self.action = QAction(PainterWindow)
        self.action.setObjectName(u"action")
        self.a_toggle_dwp = QAction(PainterWindow)
        self.a_toggle_dwp.setObjectName(u"a_toggle_dwp")
        self.a_toggle_dwp.setCheckable(True)
        self.a_toggle_dwp.setChecked(True)
        self.a_allocation_fill = QAction(PainterWindow)
        self.a_allocation_fill.setObjectName(u"a_allocation_fill")
        self.a_allocation_bound = QAction(PainterWindow)
        self.a_allocation_bound.setObjectName(u"a_allocation_bound")
        self.a_allocation_fix = QAction(PainterWindow)
        self.a_allocation_fix.setObjectName(u"a_allocation_fix")
        self.a_addictions_clear = QAction(PainterWindow)
        self.a_addictions_clear.setObjectName(u"a_addictions_clear")
        self.a_file_open = QAction(PainterWindow)
        self.a_file_open.setObjectName(u"a_file_open")
        self.a_file_save = QAction(PainterWindow)
        self.a_file_save.setObjectName(u"a_file_save")
        self.a_file_save_as = QAction(PainterWindow)
        self.a_file_save_as.setObjectName(u"a_file_save_as")
        self.a_file_close = QAction(PainterWindow)
        self.a_file_close.setObjectName(u"a_file_close")
        self.w_main = QWidget(PainterWindow)
        self.w_main.setObjectName(u"w_main")
        self.vl_main = QVBoxLayout(self.w_main)
        self.vl_main.setSpacing(0)
        self.vl_main.setObjectName(u"vl_main")
        self.vl_main.setContentsMargins(0, 0, 0, 0)
        self.w_tools = QWidget(self.w_main)
        self.w_tools.setObjectName(u"w_tools")
        self.w_tools.setMinimumSize(QSize(0, 110))
        self.w_tools.setMaximumSize(QSize(16777215, 110))
        self.hl_tools = QHBoxLayout(self.w_tools)
        self.hl_tools.setObjectName(u"hl_tools")
        self.w_action = QWidget(self.w_tools)
        self.w_action.setObjectName(u"w_action")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_action.sizePolicy().hasHeightForWidth())
        self.w_action.setSizePolicy(sizePolicy)
        self.w_action.setMinimumSize(QSize(70, 0))
        self.vl_action = QVBoxLayout(self.w_action)
        self.vl_action.setSpacing(2)
        self.vl_action.setObjectName(u"vl_action")
        self.vl_action.setContentsMargins(0, 0, 0, 0)
        self.vs_action_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action.addItem(self.vs_action_1)

        self.rb_pen = QRadioButton(self.w_action)
        self.rb_pen.setObjectName(u"rb_pen")
        self.rb_pen.setChecked(True)

        self.vl_action.addWidget(self.rb_pen)

        self.rb_fill = QRadioButton(self.w_action)
        self.rb_fill.setObjectName(u"rb_fill")

        self.vl_action.addWidget(self.rb_fill)

        self.rb_bound = QRadioButton(self.w_action)
        self.rb_bound.setObjectName(u"rb_bound")

        self.vl_action.addWidget(self.rb_bound)

        self.rb_allocation = QRadioButton(self.w_action)
        self.rb_allocation.setObjectName(u"rb_allocation")

        self.vl_action.addWidget(self.rb_allocation)

        self.rb_erase = QRadioButton(self.w_action)
        self.rb_erase.setObjectName(u"rb_erase")

        self.vl_action.addWidget(self.rb_erase)

        self.vs_action_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action.addItem(self.vs_action_2)

        self.l_action = QLabel(self.w_action)
        self.l_action.setObjectName(u"l_action")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_action.sizePolicy().hasHeightForWidth())
        self.l_action.setSizePolicy(sizePolicy1)
        self.l_action.setMinimumSize(QSize(0, 14))
        self.l_action.setMaximumSize(QSize(16777215, 14))
        self.l_action.setAlignment(Qt.AlignCenter)

        self.vl_action.addWidget(self.l_action)


        self.hl_tools.addWidget(self.w_action)

        self.line_1 = QFrame(self.w_tools)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShape(QFrame.VLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.hl_tools.addWidget(self.line_1)

        self.w_size = QWidget(self.w_tools)
        self.w_size.setObjectName(u"w_size")
        sizePolicy.setHeightForWidth(self.w_size.sizePolicy().hasHeightForWidth())
        self.w_size.setSizePolicy(sizePolicy)
        self.w_size.setMinimumSize(QSize(70, 0))
        self.vl_size = QVBoxLayout(self.w_size)
        self.vl_size.setSpacing(4)
        self.vl_size.setObjectName(u"vl_size")
        self.vl_size.setContentsMargins(0, 0, 0, 0)
        self.vs_size_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_size.addItem(self.vs_size_1)

        self.cmb_size_choose = QComboBox(self.w_size)
        self.cmb_size_choose.addItem("")
        self.cmb_size_choose.addItem("")
        self.cmb_size_choose.addItem("")
        self.cmb_size_choose.addItem("")
        self.cmb_size_choose.addItem("")
        self.cmb_size_choose.addItem("")
        self.cmb_size_choose.addItem("")
        self.cmb_size_choose.addItem("")
        self.cmb_size_choose.addItem("")
        self.cmb_size_choose.setObjectName(u"cmb_size_choose")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cmb_size_choose.sizePolicy().hasHeightForWidth())
        self.cmb_size_choose.setSizePolicy(sizePolicy2)

        self.vl_size.addWidget(self.cmb_size_choose)

        self.vs_size_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_size.addItem(self.vs_size_2)

        self.pb_size_default = QPushButton(self.w_size)
        self.pb_size_default.setObjectName(u"pb_size_default")
        self.pb_size_default.setMinimumSize(QSize(0, 20))
        self.pb_size_default.setMaximumSize(QSize(16777215, 20))

        self.vl_size.addWidget(self.pb_size_default)

        self.l_size = QLabel(self.w_size)
        self.l_size.setObjectName(u"l_size")
        sizePolicy1.setHeightForWidth(self.l_size.sizePolicy().hasHeightForWidth())
        self.l_size.setSizePolicy(sizePolicy1)
        self.l_size.setMinimumSize(QSize(0, 14))
        self.l_size.setMaximumSize(QSize(16777215, 14))
        self.l_size.setAlignment(Qt.AlignCenter)

        self.vl_size.addWidget(self.l_size)


        self.hl_tools.addWidget(self.w_size)

        self.line_2 = QFrame(self.w_tools)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.hl_tools.addWidget(self.line_2)

        self.w_color = QWidget(self.w_tools)
        self.w_color.setObjectName(u"w_color")
        sizePolicy.setHeightForWidth(self.w_color.sizePolicy().hasHeightForWidth())
        self.w_color.setSizePolicy(sizePolicy)
        self.w_color.setMinimumSize(QSize(70, 0))
        self.vl_color = QVBoxLayout(self.w_color)
        self.vl_color.setSpacing(4)
        self.vl_color.setObjectName(u"vl_color")
        self.vl_color.setContentsMargins(0, 0, 0, 0)
        self.vs_color_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_color.addItem(self.vs_color_1)

        self.w_color_current = QWidget(self.w_color)
        self.w_color_current.setObjectName(u"w_color_current")
        self.horizontalLayout = QHBoxLayout(self.w_color_current)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.hs_color_1 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.hs_color_1)

        self.w_color_preview = QWidget(self.w_color_current)
        self.w_color_preview.setObjectName(u"w_color_preview")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.w_color_preview.sizePolicy().hasHeightForWidth())
        self.w_color_preview.setSizePolicy(sizePolicy3)
        self.w_color_preview.setMinimumSize(QSize(40, 40))
        self.w_color_preview.setMaximumSize(QSize(40, 40))
        self.w_color_preview.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.w_color_preview)

        self.hs_color_2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.hs_color_2)


        self.vl_color.addWidget(self.w_color_current)

        self.vs_color_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_color.addItem(self.vs_color_2)

        self.pb_color_choose = QPushButton(self.w_color)
        self.pb_color_choose.setObjectName(u"pb_color_choose")
        self.pb_color_choose.setMinimumSize(QSize(0, 20))
        self.pb_color_choose.setMaximumSize(QSize(16777215, 20))

        self.vl_color.addWidget(self.pb_color_choose)

        self.l_color = QLabel(self.w_color)
        self.l_color.setObjectName(u"l_color")
        sizePolicy1.setHeightForWidth(self.l_color.sizePolicy().hasHeightForWidth())
        self.l_color.setSizePolicy(sizePolicy1)
        self.l_color.setMinimumSize(QSize(0, 14))
        self.l_color.setMaximumSize(QSize(16777215, 14))
        self.l_color.setAlignment(Qt.AlignCenter)

        self.vl_color.addWidget(self.l_color)


        self.hl_tools.addWidget(self.w_color)

        self.line_3 = QFrame(self.w_tools)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.hl_tools.addWidget(self.line_3)

        self.w_pattern = QWidget(self.w_tools)
        self.w_pattern.setObjectName(u"w_pattern")
        sizePolicy.setHeightForWidth(self.w_pattern.sizePolicy().hasHeightForWidth())
        self.w_pattern.setSizePolicy(sizePolicy)
        self.w_pattern.setMinimumSize(QSize(70, 0))
        self.vl_pattern = QVBoxLayout(self.w_pattern)
        self.vl_pattern.setSpacing(4)
        self.vl_pattern.setObjectName(u"vl_pattern")
        self.vl_pattern.setContentsMargins(0, 0, 0, 0)
        self.vs_pattern_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_pattern.addItem(self.vs_pattern_1)

        self.w_pattern_current = QWidget(self.w_pattern)
        self.w_pattern_current.setObjectName(u"w_pattern_current")
        self.horizontalLayout_4 = QHBoxLayout(self.w_pattern_current)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.hs_pattern_1 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.hs_pattern_1)

        self.l_pattern_preview = QLabel(self.w_pattern_current)
        self.l_pattern_preview.setObjectName(u"l_pattern_preview")
        self.l_pattern_preview.setMinimumSize(QSize(40, 40))
        self.l_pattern_preview.setMaximumSize(QSize(40, 40))
        self.l_pattern_preview.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.l_pattern_preview.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.l_pattern_preview)

        self.hs_pattern_2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.hs_pattern_2)


        self.vl_pattern.addWidget(self.w_pattern_current)

        self.vs_pattern_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_pattern.addItem(self.vs_pattern_2)

        self.pb_pattern_choose = QPushButton(self.w_pattern)
        self.pb_pattern_choose.setObjectName(u"pb_pattern_choose")
        self.pb_pattern_choose.setMinimumSize(QSize(0, 20))
        self.pb_pattern_choose.setMaximumSize(QSize(16777215, 20))

        self.vl_pattern.addWidget(self.pb_pattern_choose)

        self.cb_pattern = QCheckBox(self.w_pattern)
        self.cb_pattern.setObjectName(u"cb_pattern")
        sizePolicy1.setHeightForWidth(self.cb_pattern.sizePolicy().hasHeightForWidth())
        self.cb_pattern.setSizePolicy(sizePolicy1)
        self.cb_pattern.setMinimumSize(QSize(0, 14))
        self.cb_pattern.setMaximumSize(QSize(16777215, 14))

        self.vl_pattern.addWidget(self.cb_pattern)


        self.hl_tools.addWidget(self.w_pattern)

        self.line_4 = QFrame(self.w_tools)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.hl_tools.addWidget(self.line_4)

        self.hs_tools = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_tools.addItem(self.hs_tools)


        self.vl_main.addWidget(self.w_tools)

        PainterWindow.setCentralWidget(self.w_main)
        self.mb_main = QMenuBar(PainterWindow)
        self.mb_main.setObjectName(u"mb_main")
        self.mb_main.setGeometry(QRect(0, 0, 600, 18))
        self.m_file = QMenu(self.mb_main)
        self.m_file.setObjectName(u"m_file")
        self.m_allocation = QMenu(self.mb_main)
        self.m_allocation.setObjectName(u"m_allocation")
        self.m_addictions = QMenu(self.mb_main)
        self.m_addictions.setObjectName(u"m_addictions")
        PainterWindow.setMenuBar(self.mb_main)

        self.mb_main.addAction(self.m_file.menuAction())
        self.mb_main.addAction(self.m_allocation.menuAction())
        self.mb_main.addAction(self.m_addictions.menuAction())
        self.m_file.addAction(self.a_file_open)
        self.m_file.addAction(self.a_file_close)
        self.m_file.addSeparator()
        self.m_file.addAction(self.a_file_save)
        self.m_file.addAction(self.a_file_save_as)
        self.m_allocation.addAction(self.a_allocation_fill)
        self.m_allocation.addAction(self.a_allocation_bound)
        self.m_allocation.addAction(self.a_allocation_fix)
        self.m_addictions.addAction(self.a_addictions_clear)

        self.retranslateUi(PainterWindow)

        self.cmb_size_choose.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(PainterWindow)
    # setupUi

    def retranslateUi(self, PainterWindow):
        PainterWindow.setWindowTitle(QCoreApplication.translate("PainterWindow", u"\u0420\u0438\u0441\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.action.setText(QCoreApplication.translate("PainterWindow", u"\u0421\u0443\u0441", None))
        self.a_toggle_dwp.setText(QCoreApplication.translate("PainterWindow", u"\u0420\u0438\u0441\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.a_allocation_fill.setText(QCoreApplication.translate("PainterWindow", u"\u0417\u0430\u043b\u0438\u0442\u044c", None))
        self.a_allocation_bound.setText(QCoreApplication.translate("PainterWindow", u"\u041e\u0431\u0432\u0435\u0441\u0442\u0438", None))
        self.a_allocation_fix.setText(QCoreApplication.translate("PainterWindow", u"\u0417\u0430\u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.a_addictions_clear.setText(QCoreApplication.translate("PainterWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.a_file_open.setText(QCoreApplication.translate("PainterWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.a_file_save.setText(QCoreApplication.translate("PainterWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.a_file_save_as.setText(QCoreApplication.translate("PainterWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.a_file_close.setText(QCoreApplication.translate("PainterWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.rb_pen.setText(QCoreApplication.translate("PainterWindow", u"\u041a\u0430\u0440\u0430\u043d\u0434\u0430\u0448", None))
        self.rb_fill.setText(QCoreApplication.translate("PainterWindow", u"\u0417\u0430\u043b\u0438\u0432\u043a\u0430", None))
        self.rb_bound.setText(QCoreApplication.translate("PainterWindow", u"\u041e\u0431\u0432\u043e\u0434\u043a\u0430", None))
        self.rb_allocation.setText(QCoreApplication.translate("PainterWindow", u"\u0412\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.rb_erase.setText(QCoreApplication.translate("PainterWindow", u"\u041b\u0430\u0441\u0442\u0438\u043a", None))
        self.l_action.setText(QCoreApplication.translate("PainterWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.cmb_size_choose.setItemText(0, QCoreApplication.translate("PainterWindow", u"1", None))
        self.cmb_size_choose.setItemText(1, QCoreApplication.translate("PainterWindow", u"2", None))
        self.cmb_size_choose.setItemText(2, QCoreApplication.translate("PainterWindow", u"3", None))
        self.cmb_size_choose.setItemText(3, QCoreApplication.translate("PainterWindow", u"4", None))
        self.cmb_size_choose.setItemText(4, QCoreApplication.translate("PainterWindow", u"8", None))
        self.cmb_size_choose.setItemText(5, QCoreApplication.translate("PainterWindow", u"12", None))
        self.cmb_size_choose.setItemText(6, QCoreApplication.translate("PainterWindow", u"16", None))
        self.cmb_size_choose.setItemText(7, QCoreApplication.translate("PainterWindow", u"20", None))
        self.cmb_size_choose.setItemText(8, QCoreApplication.translate("PainterWindow", u"24", None))

        self.pb_size_default.setText(QCoreApplication.translate("PainterWindow", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u0439", None))
        self.l_size.setText(QCoreApplication.translate("PainterWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440", None))
        self.pb_color_choose.setText(QCoreApplication.translate("PainterWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.l_color.setText(QCoreApplication.translate("PainterWindow", u"\u0426\u0432\u0435\u0442", None))
        self.pb_pattern_choose.setText(QCoreApplication.translate("PainterWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.cb_pattern.setText(QCoreApplication.translate("PainterWindow", u" \u041f\u0430\u0442\u0442\u0435\u0440\u043d", None))
        self.m_file.setTitle(QCoreApplication.translate("PainterWindow", u"\u0424\u0430\u0439\u043b", None))
        self.m_allocation.setTitle(QCoreApplication.translate("PainterWindow", u"\u0412\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.m_addictions.setTitle(QCoreApplication.translate("PainterWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e", None))
    # retranslateUi

