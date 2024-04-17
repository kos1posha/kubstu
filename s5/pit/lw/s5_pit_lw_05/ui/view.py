# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_GeometricWindow(object):
    def setupUi(self, GeometricWindow):
        if not GeometricWindow.objectName():
            GeometricWindow.setObjectName(u"GeometricWindow")
        GeometricWindow.resize(800, 600)
        GeometricWindow.setMinimumSize(QSize(600, 500))
        self.w_main = QWidget(GeometricWindow)
        self.w_main.setObjectName(u"w_main")
        self.gl_main = QGridLayout(self.w_main)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setVerticalSpacing(0)
        self.gl_main.setContentsMargins(0, 0, 0, 0)
        self.w_ps = QWidget(self.w_main)
        self.w_ps.setObjectName(u"w_ps")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_ps.sizePolicy().hasHeightForWidth())
        self.w_ps.setSizePolicy(sizePolicy)
        self.vl_ps = QVBoxLayout(self.w_ps)
        self.vl_ps.setSpacing(0)
        self.vl_ps.setObjectName(u"vl_ps")
        self.vl_ps.setContentsMargins(0, 0, 0, 0)

        self.gl_main.addWidget(self.w_ps, 2, 0, 2, 2)

        self.w_primivitives = QWidget(self.w_main)
        self.w_primivitives.setObjectName(u"w_primivitives")
        self.w_primivitives.setMaximumSize(QSize(300, 16777215))
        self.vl_primitives = QVBoxLayout(self.w_primivitives)
        self.vl_primitives.setObjectName(u"vl_primitives")
        self.vl_primitives.setContentsMargins(0, 0, 6, 0)
        self.label = QLabel(self.w_primivitives)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.vl_primitives.addWidget(self.label)

        self.tw_primitives = QTableWidget(self.w_primivitives)
        if (self.tw_primitives.columnCount() < 4):
            self.tw_primitives.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_primitives.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_primitives.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_primitives.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_primitives.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tw_primitives.setObjectName(u"tw_primitives")
        self.tw_primitives.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_primitives.setProperty("showDropIndicator", False)
        self.tw_primitives.setDragDropOverwriteMode(False)
        self.tw_primitives.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_primitives.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tw_primitives.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tw_primitives.horizontalHeader().setDefaultSectionSize(65)
        self.tw_primitives.horizontalHeader().setStretchLastSection(True)
        self.tw_primitives.verticalHeader().setVisible(False)
        self.tw_primitives.verticalHeader().setMinimumSectionSize(16)
        self.tw_primitives.verticalHeader().setDefaultSectionSize(16)
        self.tw_primitives.verticalHeader().setHighlightSections(False)

        self.vl_primitives.addWidget(self.tw_primitives)

        self.pb_remove_primitive = QPushButton(self.w_primivitives)
        self.pb_remove_primitive.setObjectName(u"pb_remove_primitive")

        self.vl_primitives.addWidget(self.pb_remove_primitive)


        self.gl_main.addWidget(self.w_primivitives, 2, 2, 1, 1)

        self.w_toolbar = QWidget(self.w_main)
        self.w_toolbar.setObjectName(u"w_toolbar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.w_toolbar.sizePolicy().hasHeightForWidth())
        self.w_toolbar.setSizePolicy(sizePolicy1)
        self.w_toolbar.setMaximumSize(QSize(16777215, 110))
        self.hl_toolbar = QHBoxLayout(self.w_toolbar)
        self.hl_toolbar.setSpacing(6)
        self.hl_toolbar.setObjectName(u"hl_toolbar")
        self.w_tool_actions = QWidget(self.w_toolbar)
        self.w_tool_actions.setObjectName(u"w_tool_actions")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.w_tool_actions.sizePolicy().hasHeightForWidth())
        self.w_tool_actions.setSizePolicy(sizePolicy2)
        self.vl_action = QVBoxLayout(self.w_tool_actions)
        self.vl_action.setSpacing(2)
        self.vl_action.setObjectName(u"vl_action")
        self.vl_action.setContentsMargins(0, 0, 0, 0)
        self.vs_action_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action.addItem(self.vs_action_1)

        self.rb_point = QRadioButton(self.w_tool_actions)
        self.rb_point.setObjectName(u"rb_point")

        self.vl_action.addWidget(self.rb_point)

        self.rb_line = QRadioButton(self.w_tool_actions)
        self.rb_line.setObjectName(u"rb_line")

        self.vl_action.addWidget(self.rb_line)

        self.rb_polygon = QRadioButton(self.w_tool_actions)
        self.rb_polygon.setObjectName(u"rb_polygon")

        self.vl_action.addWidget(self.rb_polygon)

        self.vs_action_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action.addItem(self.vs_action_2)

        self.l_actions = QLabel(self.w_tool_actions)
        self.l_actions.setObjectName(u"l_actions")
        sizePolicy1.setHeightForWidth(self.l_actions.sizePolicy().hasHeightForWidth())
        self.l_actions.setSizePolicy(sizePolicy1)
        self.l_actions.setMinimumSize(QSize(0, 14))
        self.l_actions.setMaximumSize(QSize(16777215, 14))
        self.l_actions.setAlignment(Qt.AlignCenter)

        self.vl_action.addWidget(self.l_actions)


        self.hl_toolbar.addWidget(self.w_tool_actions)

        self.line_1 = QFrame(self.w_toolbar)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShape(QFrame.VLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_1)

        self.w_tool_size = QWidget(self.w_toolbar)
        self.w_tool_size.setObjectName(u"w_tool_size")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.w_tool_size.sizePolicy().hasHeightForWidth())
        self.w_tool_size.setSizePolicy(sizePolicy3)
        self.vl_size = QVBoxLayout(self.w_tool_size)
        self.vl_size.setSpacing(2)
        self.vl_size.setObjectName(u"vl_size")
        self.vl_size.setContentsMargins(0, 0, 0, 0)
        self.vs_size_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_size.addItem(self.vs_size_1)

        self.cmb_size_choose = QComboBox(self.w_tool_size)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cmb_size_choose.sizePolicy().hasHeightForWidth())
        self.cmb_size_choose.setSizePolicy(sizePolicy4)

        self.vl_size.addWidget(self.cmb_size_choose)

        self.vs_size_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_size.addItem(self.vs_size_2)

        self.pb_size_default = QPushButton(self.w_tool_size)
        self.pb_size_default.setObjectName(u"pb_size_default")
        self.pb_size_default.setMinimumSize(QSize(0, 20))
        self.pb_size_default.setMaximumSize(QSize(16777215, 20))

        self.vl_size.addWidget(self.pb_size_default)

        self.l_size = QLabel(self.w_tool_size)
        self.l_size.setObjectName(u"l_size")
        sizePolicy1.setHeightForWidth(self.l_size.sizePolicy().hasHeightForWidth())
        self.l_size.setSizePolicy(sizePolicy1)
        self.l_size.setMinimumSize(QSize(0, 14))
        self.l_size.setMaximumSize(QSize(16777215, 14))
        self.l_size.setAlignment(Qt.AlignCenter)

        self.vl_size.addWidget(self.l_size)


        self.hl_toolbar.addWidget(self.w_tool_size)

        self.line_2 = QFrame(self.w_toolbar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_2)

        self.w_tool_color = QWidget(self.w_toolbar)
        self.w_tool_color.setObjectName(u"w_tool_color")
        sizePolicy2.setHeightForWidth(self.w_tool_color.sizePolicy().hasHeightForWidth())
        self.w_tool_color.setSizePolicy(sizePolicy2)
        self.vl_color_2 = QVBoxLayout(self.w_tool_color)
        self.vl_color_2.setSpacing(2)
        self.vl_color_2.setObjectName(u"vl_color_2")
        self.vl_color_2.setContentsMargins(4, 0, 4, 0)
        self.vs_color_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_color_2.addItem(self.vs_color_1)

        self.w_current_color = QWidget(self.w_tool_color)
        self.w_current_color.setObjectName(u"w_current_color")
        self.horizontalLayout = QHBoxLayout(self.w_current_color)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.hs_color_1 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.hs_color_1)

        self.w_color_preview = QWidget(self.w_current_color)
        self.w_color_preview.setObjectName(u"w_color_preview")
        sizePolicy.setHeightForWidth(self.w_color_preview.sizePolicy().hasHeightForWidth())
        self.w_color_preview.setSizePolicy(sizePolicy)
        self.w_color_preview.setMinimumSize(QSize(40, 40))
        self.w_color_preview.setMaximumSize(QSize(40, 40))
        self.w_color_preview.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.w_color_preview)

        self.hs_color_2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.hs_color_2)


        self.vl_color_2.addWidget(self.w_current_color)

        self.vs_color_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_color_2.addItem(self.vs_color_2)

        self.pb_switch_color = QPushButton(self.w_tool_color)
        self.pb_switch_color.setObjectName(u"pb_switch_color")
        self.pb_switch_color.setMinimumSize(QSize(0, 20))
        self.pb_switch_color.setMaximumSize(QSize(16777215, 20))

        self.vl_color_2.addWidget(self.pb_switch_color)

        self.l_color = QLabel(self.w_tool_color)
        self.l_color.setObjectName(u"l_color")
        sizePolicy1.setHeightForWidth(self.l_color.sizePolicy().hasHeightForWidth())
        self.l_color.setSizePolicy(sizePolicy1)
        self.l_color.setMinimumSize(QSize(0, 14))
        self.l_color.setMaximumSize(QSize(16777215, 14))
        self.l_color.setAlignment(Qt.AlignCenter)

        self.vl_color_2.addWidget(self.l_color)


        self.hl_toolbar.addWidget(self.w_tool_color)

        self.line_3 = QFrame(self.w_toolbar)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_3)

        self.w_tool_transform = QWidget(self.w_toolbar)
        self.w_tool_transform.setObjectName(u"w_tool_transform")
        sizePolicy2.setHeightForWidth(self.w_tool_transform.sizePolicy().hasHeightForWidth())
        self.w_tool_transform.setSizePolicy(sizePolicy2)
        self.vl_action_6 = QVBoxLayout(self.w_tool_transform)
        self.vl_action_6.setSpacing(2)
        self.vl_action_6.setObjectName(u"vl_action_6")
        self.vl_action_6.setContentsMargins(0, 0, 0, 0)
        self.vs_transform_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action_6.addItem(self.vs_transform_1)

        self.sb_rotate_angle = QSpinBox(self.w_tool_transform)
        self.sb_rotate_angle.setObjectName(u"sb_rotate_angle")
        self.sb_rotate_angle.setMinimum(1)
        self.sb_rotate_angle.setMaximum(359)
        self.sb_rotate_angle.setValue(90)

        self.vl_action_6.addWidget(self.sb_rotate_angle)

        self.vs_transform_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action_6.addItem(self.vs_transform_2)

        self.pb_rotate = QPushButton(self.w_tool_transform)
        self.pb_rotate.setObjectName(u"pb_rotate")

        self.vl_action_6.addWidget(self.pb_rotate)

        self.l_transform = QLabel(self.w_tool_transform)
        self.l_transform.setObjectName(u"l_transform")
        sizePolicy1.setHeightForWidth(self.l_transform.sizePolicy().hasHeightForWidth())
        self.l_transform.setSizePolicy(sizePolicy1)
        self.l_transform.setMinimumSize(QSize(0, 14))
        self.l_transform.setMaximumSize(QSize(16777215, 14))
        self.l_transform.setAlignment(Qt.AlignCenter)

        self.vl_action_6.addWidget(self.l_transform)


        self.hl_toolbar.addWidget(self.w_tool_transform)

        self.line_4 = QFrame(self.w_toolbar)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_4)

        self.w_tool_find = QWidget(self.w_toolbar)
        self.w_tool_find.setObjectName(u"w_tool_find")
        sizePolicy2.setHeightForWidth(self.w_tool_find.sizePolicy().hasHeightForWidth())
        self.w_tool_find.setSizePolicy(sizePolicy2)
        self.vl_action_3 = QVBoxLayout(self.w_tool_find)
        self.vl_action_3.setSpacing(2)
        self.vl_action_3.setObjectName(u"vl_action_3")
        self.vl_action_3.setContentsMargins(0, 0, 0, 0)
        self.vs_find_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action_3.addItem(self.vs_find_1)

        self.pb_include = QPushButton(self.w_tool_find)
        self.pb_include.setObjectName(u"pb_include")

        self.vl_action_3.addWidget(self.pb_include)

        self.pb_instersection = QPushButton(self.w_tool_find)
        self.pb_instersection.setObjectName(u"pb_instersection")

        self.vl_action_3.addWidget(self.pb_instersection)

        self.l_find = QLabel(self.w_tool_find)
        self.l_find.setObjectName(u"l_find")
        sizePolicy1.setHeightForWidth(self.l_find.sizePolicy().hasHeightForWidth())
        self.l_find.setSizePolicy(sizePolicy1)
        self.l_find.setMinimumSize(QSize(0, 14))
        self.l_find.setMaximumSize(QSize(16777215, 14))
        self.l_find.setAlignment(Qt.AlignCenter)

        self.vl_action_3.addWidget(self.l_find)


        self.hl_toolbar.addWidget(self.w_tool_find)

        self.line_5 = QFrame(self.w_toolbar)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_5)

        self.w_tool__1 = QWidget(self.w_toolbar)
        self.w_tool__1.setObjectName(u"w_tool__1")
        sizePolicy2.setHeightForWidth(self.w_tool__1.sizePolicy().hasHeightForWidth())
        self.w_tool__1.setSizePolicy(sizePolicy2)
        self.vl_action_4 = QVBoxLayout(self.w_tool__1)
        self.vl_action_4.setSpacing(2)
        self.vl_action_4.setObjectName(u"vl_action_4")
        self.vl_action_4.setContentsMargins(0, 0, 0, 0)
        self.vs__1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action_4.addItem(self.vs__1)

        self.vs__2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action_4.addItem(self.vs__2)

        self.l__1 = QLabel(self.w_tool__1)
        self.l__1.setObjectName(u"l__1")
        sizePolicy1.setHeightForWidth(self.l__1.sizePolicy().hasHeightForWidth())
        self.l__1.setSizePolicy(sizePolicy1)
        self.l__1.setMinimumSize(QSize(0, 14))
        self.l__1.setMaximumSize(QSize(16777215, 14))
        self.l__1.setAlignment(Qt.AlignCenter)

        self.vl_action_4.addWidget(self.l__1)


        self.hl_toolbar.addWidget(self.w_tool__1)

        self.line_6 = QFrame(self.w_toolbar)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_6)

        self.w_tool_additional = QWidget(self.w_toolbar)
        self.w_tool_additional.setObjectName(u"w_tool_additional")
        sizePolicy2.setHeightForWidth(self.w_tool_additional.sizePolicy().hasHeightForWidth())
        self.w_tool_additional.setSizePolicy(sizePolicy2)
        self.vl_action_2 = QVBoxLayout(self.w_tool_additional)
        self.vl_action_2.setSpacing(2)
        self.vl_action_2.setObjectName(u"vl_action_2")
        self.vl_action_2.setContentsMargins(0, 0, 0, 0)
        self.vs_additional_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_action_2.addItem(self.vs_additional_1)

        self.pb_clear = QPushButton(self.w_tool_additional)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setMinimumSize(QSize(0, 20))
        self.pb_clear.setMaximumSize(QSize(16777215, 20))

        self.vl_action_2.addWidget(self.pb_clear)

        self.l_additional = QLabel(self.w_tool_additional)
        self.l_additional.setObjectName(u"l_additional")
        sizePolicy1.setHeightForWidth(self.l_additional.sizePolicy().hasHeightForWidth())
        self.l_additional.setSizePolicy(sizePolicy1)
        self.l_additional.setMinimumSize(QSize(0, 14))
        self.l_additional.setMaximumSize(QSize(16777215, 14))
        self.l_additional.setAlignment(Qt.AlignCenter)

        self.vl_action_2.addWidget(self.l_additional)


        self.hl_toolbar.addWidget(self.w_tool_additional)

        self.line_7 = QFrame(self.w_toolbar)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_7)

        self.hs_toolbar = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_toolbar.addItem(self.hs_toolbar)


        self.gl_main.addWidget(self.w_toolbar, 0, 0, 1, 3)

        self.line = QFrame(self.w_main)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gl_main.addWidget(self.line, 1, 0, 1, 3)

        GeometricWindow.setCentralWidget(self.w_main)
        self.stb_main = QStatusBar(GeometricWindow)
        self.stb_main.setObjectName(u"stb_main")
        GeometricWindow.setStatusBar(self.stb_main)

        self.retranslateUi(GeometricWindow)

        self.cmb_size_choose.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(GeometricWindow)
    # setupUi

    def retranslateUi(self, GeometricWindow):
        GeometricWindow.setWindowTitle(QCoreApplication.translate("GeometricWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("GeometricWindow", u"\u041f\u0440\u0438\u043c\u0438\u0442\u0438\u0432\u044b", None))
        ___qtablewidgetitem = self.tw_primitives.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("GeometricWindow", u"\u041f\u0440\u0438\u043c\u0438\u0442\u0438\u0432", None));
        ___qtablewidgetitem1 = self.tw_primitives.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("GeometricWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None));
        ___qtablewidgetitem2 = self.tw_primitives.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("GeometricWindow", u"\u0426\u0432\u0435\u0442", None));
        ___qtablewidgetitem3 = self.tw_primitives.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("GeometricWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None));
        self.pb_remove_primitive.setText(QCoreApplication.translate("GeometricWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.rb_point.setText(QCoreApplication.translate("GeometricWindow", u"\u0422\u043e\u0447\u043a\u0430", None))
        self.rb_line.setText(QCoreApplication.translate("GeometricWindow", u"\u041e\u0442\u0440\u0435\u0437\u043e\u043a", None))
        self.rb_polygon.setText(QCoreApplication.translate("GeometricWindow", u"\u041c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a", None))
        self.l_actions.setText(QCoreApplication.translate("GeometricWindow", u"\u041f\u0440\u0438\u043c\u0438\u0442\u0438\u0432", None))
        self.cmb_size_choose.setItemText(0, QCoreApplication.translate("GeometricWindow", u"1", None))
        self.cmb_size_choose.setItemText(1, QCoreApplication.translate("GeometricWindow", u"2", None))
        self.cmb_size_choose.setItemText(2, QCoreApplication.translate("GeometricWindow", u"3", None))
        self.cmb_size_choose.setItemText(3, QCoreApplication.translate("GeometricWindow", u"4", None))
        self.cmb_size_choose.setItemText(4, QCoreApplication.translate("GeometricWindow", u"8", None))
        self.cmb_size_choose.setItemText(5, QCoreApplication.translate("GeometricWindow", u"12", None))
        self.cmb_size_choose.setItemText(6, QCoreApplication.translate("GeometricWindow", u"16", None))
        self.cmb_size_choose.setItemText(7, QCoreApplication.translate("GeometricWindow", u"20", None))
        self.cmb_size_choose.setItemText(8, QCoreApplication.translate("GeometricWindow", u"24", None))

        self.pb_size_default.setText(QCoreApplication.translate("GeometricWindow", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u0439", None))
        self.l_size.setText(QCoreApplication.translate("GeometricWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440", None))
        self.pb_switch_color.setText(QCoreApplication.translate("GeometricWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.l_color.setText(QCoreApplication.translate("GeometricWindow", u"\u0426\u0432\u0435\u0442", None))
        self.pb_rotate.setText(QCoreApplication.translate("GeometricWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
        self.l_transform.setText(QCoreApplication.translate("GeometricWindow", u"\u0422\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.pb_include.setText(QCoreApplication.translate("GeometricWindow", u"\u0412\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435", None))
        self.pb_instersection.setText(QCoreApplication.translate("GeometricWindow", u"\u041f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435", None))
        self.l_find.setText(QCoreApplication.translate("GeometricWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.l__1.setText(QCoreApplication.translate("GeometricWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d", None))
        self.pb_clear.setText(QCoreApplication.translate("GeometricWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.l_additional.setText(QCoreApplication.translate("GeometricWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e", None))
    # retranslateUi

