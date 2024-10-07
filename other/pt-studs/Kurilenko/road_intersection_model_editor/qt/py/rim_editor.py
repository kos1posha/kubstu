# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rim_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_RIMEditor(object):
    def setupUi(self, RIMEditor):
        if not RIMEditor.objectName():
            RIMEditor.setObjectName(u"RIMEditor")
        RIMEditor.resize(500, 400)
        RIMEditor.setMinimumSize(QSize(500, 400))
        self.a_load_image = QAction(RIMEditor)
        self.a_load_image.setObjectName(u"a_load_image")
        self.a_clear_image = QAction(RIMEditor)
        self.a_clear_image.setObjectName(u"a_clear_image")
        self.a_clear_model = QAction(RIMEditor)
        self.a_clear_model.setObjectName(u"a_clear_model")
        self.w_main = QWidget(RIMEditor)
        self.w_main.setObjectName(u"w_main")
        self.gl_main = QGridLayout(self.w_main)
        self.gl_main.setObjectName(u"gl_main")
        self.hl_toolbar = QHBoxLayout()
        self.hl_toolbar.setSpacing(6)
        self.hl_toolbar.setObjectName(u"hl_toolbar")
        self.w_road = QWidget(self.w_main)
        self.w_road.setObjectName(u"w_road")
        self.w_road.setMaximumSize(QSize(16777215, 90))
        self.w_road.setStyleSheet(u"QRadioButton {\n"
"  padding: 4px;\n"
"  border: 1px solid #1e62d0;\n"
"  font-weight:bold;\n"
"  border-radius: 6px;\n"
"  background: #ffffff;\n"
"  color:#3d94f6;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"  background: #3d94f6;\n"
"  color:#ffffff;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"  background: #337fed;\n"
"  color:#ffffff;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"  width: 0px;\n"
"}")
        self.gl_road = QGridLayout(self.w_road)
        self.gl_road.setObjectName(u"gl_road")
        self.l_road = QLabel(self.w_road)
        self.l_road.setObjectName(u"l_road")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_road.sizePolicy().hasHeightForWidth())
        self.l_road.setSizePolicy(sizePolicy)
        self.l_road.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gl_road.addWidget(self.l_road, 1, 0, 1, 1)

        self.w_road_actions = QWidget(self.w_road)
        self.w_road_actions.setObjectName(u"w_road_actions")
        self.vl_road_actions = QVBoxLayout(self.w_road_actions)
        self.vl_road_actions.setObjectName(u"vl_road_actions")
        self.vl_road_actions.setContentsMargins(-1, 0, -1, 0)
        self.rb_road_add = QRadioButton(self.w_road_actions)
        self.rb_road_add.setObjectName(u"rb_road_add")
        self.rb_road_add.setStyleSheet(u"padding-left:3px;")

        self.vl_road_actions.addWidget(self.rb_road_add)

        self.rb_road_do_nothing = QRadioButton(self.w_road_actions)
        self.rb_road_do_nothing.setObjectName(u"rb_road_do_nothing")
        self.rb_road_do_nothing.setStyleSheet(u"padding-left: 5px;")

        self.vl_road_actions.addWidget(self.rb_road_do_nothing)

        self.vs_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_road_actions.addItem(self.vs_1)


        self.gl_road.addWidget(self.w_road_actions, 0, 0, 1, 1)


        self.hl_toolbar.addWidget(self.w_road)

        self.line_toolbar_1 = QFrame(self.w_main)
        self.line_toolbar_1.setObjectName(u"line_toolbar_1")
        self.line_toolbar_1.setMaximumSize(QSize(16777215, 80))
        self.line_toolbar_1.setFrameShape(QFrame.Shape.VLine)
        self.line_toolbar_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.hl_toolbar.addWidget(self.line_toolbar_1)

        self.w_road_color = QWidget(self.w_main)
        self.w_road_color.setObjectName(u"w_road_color")
        self.w_road_color.setMaximumSize(QSize(16777215, 90))
        self.w_road_color.setStyleSheet(u"QRadioButton {\n"
"  padding: 4px;\n"
"  border: 1px solid #1e62d0;\n"
"  font-weight:bold;\n"
"  border-radius: 6px;\n"
"  background: #ffffff;\n"
"  color:#3d94f6;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"  background: #3d94f6;\n"
"  color:#ffffff;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"  background: #337fed;\n"
"  color:#ffffff;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"  width: 0px;\n"
"}")
        self.gl_road_color = QGridLayout(self.w_road_color)
        self.gl_road_color.setObjectName(u"gl_road_color")
        self.w_road_color_inter = QWidget(self.w_road_color)
        self.w_road_color_inter.setObjectName(u"w_road_color_inter")
        self.hl_road_color_inter = QHBoxLayout(self.w_road_color_inter)
        self.hl_road_color_inter.setObjectName(u"hl_road_color_inter")
        self.hl_road_color_inter.setContentsMargins(0, 8, 0, -1)
        self.w_road_primary_color = QWidget(self.w_road_color_inter)
        self.w_road_primary_color.setObjectName(u"w_road_primary_color")
        self.w_road_primary_color.setMinimumSize(QSize(40, 40))
        self.w_road_primary_color.setMaximumSize(QSize(40, 40))
        self.w_road_primary_color.setStyleSheet(u"background-color: #0000ff;\n"
"border: 1px solid lightgrey;\n"
"border-radius: 20px;")

        self.hl_road_color_inter.addWidget(self.w_road_primary_color)

        self.w_road_secondary_color = QWidget(self.w_road_color_inter)
        self.w_road_secondary_color.setObjectName(u"w_road_secondary_color")
        self.w_road_secondary_color.setMinimumSize(QSize(40, 40))
        self.w_road_secondary_color.setMaximumSize(QSize(40, 40))
        self.w_road_secondary_color.setStyleSheet(u"background-color: #00ff00;\n"
"border: 1px solid lightgrey;\n"
"border-radius: 20px;")

        self.hl_road_color_inter.addWidget(self.w_road_secondary_color)


        self.gl_road_color.addWidget(self.w_road_color_inter, 0, 1, 1, 1)

        self.l_road_color = QLabel(self.w_road_color)
        self.l_road_color.setObjectName(u"l_road_color")
        sizePolicy.setHeightForWidth(self.l_road_color.sizePolicy().hasHeightForWidth())
        self.l_road_color.setSizePolicy(sizePolicy)
        self.l_road_color.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gl_road_color.addWidget(self.l_road_color, 2, 1, 1, 1)

        self.vs_ = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gl_road_color.addItem(self.vs_, 1, 1, 1, 1)


        self.hl_toolbar.addWidget(self.w_road_color)

        self.line_toolbar_2 = QFrame(self.w_main)
        self.line_toolbar_2.setObjectName(u"line_toolbar_2")
        self.line_toolbar_2.setMaximumSize(QSize(16777215, 80))
        self.line_toolbar_2.setFrameShape(QFrame.Shape.VLine)
        self.line_toolbar_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.hl_toolbar.addWidget(self.line_toolbar_2)

        self.hs_toolbar = QSpacerItem(40, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_toolbar.addItem(self.hs_toolbar)


        self.gl_main.addLayout(self.hl_toolbar, 0, 0, 1, 1)

        self.line_main = QFrame(self.w_main)
        self.line_main.setObjectName(u"line_main")
        self.line_main.setFrameShape(QFrame.Shape.HLine)
        self.line_main.setFrameShadow(QFrame.Shadow.Sunken)

        self.gl_main.addWidget(self.line_main, 1, 0, 1, 1)

        self.l_rim = QLabel(self.w_main)
        self.l_rim.setObjectName(u"l_rim")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_rim.sizePolicy().hasHeightForWidth())
        self.l_rim.setSizePolicy(sizePolicy1)
        self.l_rim.setFrameShape(QFrame.Panel)
        self.l_rim.setFrameShadow(QFrame.Sunken)
        self.l_rim.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.l_rim, 2, 0, 1, 1)

        RIMEditor.setCentralWidget(self.w_main)
        self.menu_bar = QMenuBar(RIMEditor)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 500, 18))
        self.m_file = QMenu(self.menu_bar)
        self.m_file.setObjectName(u"m_file")
        self.m_about = QMenu(self.menu_bar)
        self.m_about.setObjectName(u"m_about")
        RIMEditor.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(RIMEditor)
        self.status_bar.setObjectName(u"status_bar")
        RIMEditor.setStatusBar(self.status_bar)

        self.menu_bar.addAction(self.m_file.menuAction())
        self.menu_bar.addAction(self.m_about.menuAction())
        self.m_file.addAction(self.a_load_image)
        self.m_file.addAction(self.a_clear_image)
        self.m_file.addAction(self.a_clear_model)

        self.retranslateUi(RIMEditor)

        QMetaObject.connectSlotsByName(RIMEditor)
    # setupUi

    def retranslateUi(self, RIMEditor):
        RIMEditor.setWindowTitle(QCoreApplication.translate("RIMEditor", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u041c\u0414\u041f", None))
        self.a_load_image.setText(QCoreApplication.translate("RIMEditor", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.a_clear_image.setText(QCoreApplication.translate("RIMEditor", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.a_clear_model.setText(QCoreApplication.translate("RIMEditor", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043c\u043e\u0434\u0435\u043b\u044c", None))
        self.l_road.setText(QCoreApplication.translate("RIMEditor", u"\u0414\u043e\u0440\u043e\u0433\u0430", None))
#if QT_CONFIG(tooltip)
        self.rb_road_add.setToolTip(QCoreApplication.translate("RIMEditor", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u043e\u0440\u043e\u0433\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.rb_road_add.setText(QCoreApplication.translate("RIMEditor", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.rb_road_do_nothing.setToolTip(QCoreApplication.translate("RIMEditor", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u043e\u0440\u043e\u0433\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.rb_road_do_nothing.setText(QCoreApplication.translate("RIMEditor", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.l_road_color.setText(QCoreApplication.translate("RIMEditor", u"\u0426\u0432\u0435\u0442", None))
        self.l_rim.setText("")
        self.m_file.setTitle(QCoreApplication.translate("RIMEditor", u"\u0424\u0430\u0439\u043b", None))
        self.m_about.setTitle(QCoreApplication.translate("RIMEditor", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

