# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'given.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_GivenWindow(object):
    def setupUi(self, GivenWindow):
        if not GivenWindow.objectName():
            GivenWindow.setObjectName(u"GivenWindow")
        GivenWindow.resize(533, 332)
        self.a_put_task = QAction(GivenWindow)
        self.a_put_task.setObjectName(u"a_put_task")
        self.a_show_task = QAction(GivenWindow)
        self.a_show_task.setObjectName(u"a_show_task")
        self.a_find_solution = QAction(GivenWindow)
        self.a_find_solution.setObjectName(u"a_find_solution")
        self.centralwidget = QWidget(GivenWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gl_main = QGridLayout(self.centralwidget)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setVerticalSpacing(0)
        self.l_t2 = QLabel(self.centralwidget)
        self.l_t2.setObjectName(u"l_t2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_t2.sizePolicy().hasHeightForWidth())
        self.l_t2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.l_t2.setFont(font)
        self.l_t2.setStyleSheet(u"color:red")

        self.gl_main.addWidget(self.l_t2, 6, 0, 1, 17)

        self.hl_t2 = QHBoxLayout()
        self.hl_t2.setSpacing(6)
        self.hl_t2.setObjectName(u"hl_t2")
        self.l_t2_x4 = QLabel(self.centralwidget)
        self.l_t2_x4.setObjectName(u"l_t2_x4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_t2_x4.sizePolicy().hasHeightForWidth())
        self.l_t2_x4.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        self.l_t2_x4.setFont(font1)
        self.l_t2_x4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t2.addWidget(self.l_t2_x4)

        self.l_t2_x4_plus = QLabel(self.centralwidget)
        self.l_t2_x4_plus.setObjectName(u"l_t2_x4_plus")
        sizePolicy1.setHeightForWidth(self.l_t2_x4_plus.sizePolicy().hasHeightForWidth())
        self.l_t2_x4_plus.setSizePolicy(sizePolicy1)
        self.l_t2_x4_plus.setFont(font1)
        self.l_t2_x4_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t2.addWidget(self.l_t2_x4_plus)

        self.l_t2_x5 = QLabel(self.centralwidget)
        self.l_t2_x5.setObjectName(u"l_t2_x5")
        sizePolicy1.setHeightForWidth(self.l_t2_x5.sizePolicy().hasHeightForWidth())
        self.l_t2_x5.setSizePolicy(sizePolicy1)
        self.l_t2_x5.setFont(font1)
        self.l_t2_x5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t2.addWidget(self.l_t2_x5)

        self.l_t2_x5_plus = QLabel(self.centralwidget)
        self.l_t2_x5_plus.setObjectName(u"l_t2_x5_plus")
        sizePolicy1.setHeightForWidth(self.l_t2_x5_plus.sizePolicy().hasHeightForWidth())
        self.l_t2_x5_plus.setSizePolicy(sizePolicy1)
        self.l_t2_x5_plus.setFont(font1)
        self.l_t2_x5_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t2.addWidget(self.l_t2_x5_plus)

        self.l_t2_x6 = QLabel(self.centralwidget)
        self.l_t2_x6.setObjectName(u"l_t2_x6")
        sizePolicy1.setHeightForWidth(self.l_t2_x6.sizePolicy().hasHeightForWidth())
        self.l_t2_x6.setSizePolicy(sizePolicy1)
        self.l_t2_x6.setFont(font1)
        self.l_t2_x6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t2.addWidget(self.l_t2_x6)

        self.l_t2_le = QLabel(self.centralwidget)
        self.l_t2_le.setObjectName(u"l_t2_le")
        sizePolicy1.setHeightForWidth(self.l_t2_le.sizePolicy().hasHeightForWidth())
        self.l_t2_le.setSizePolicy(sizePolicy1)
        self.l_t2_le.setFont(font1)
        self.l_t2_le.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t2.addWidget(self.l_t2_le)

        self.le_t2_rhs = QLineEdit(self.centralwidget)
        self.le_t2_rhs.setObjectName(u"le_t2_rhs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_t2_rhs.sizePolicy().hasHeightForWidth())
        self.le_t2_rhs.setSizePolicy(sizePolicy2)
        self.le_t2_rhs.setMaximumSize(QSize(66, 16777215))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.le_t2_rhs.setFont(font2)
        self.le_t2_rhs.setMaxLength(5)
        self.le_t2_rhs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t2.addWidget(self.le_t2_rhs)

        self.hs_t2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_t2.addItem(self.hs_t2)


        self.gl_main.addLayout(self.hl_t2, 7, 0, 1, 17)

        self.l_d2 = QLabel(self.centralwidget)
        self.l_d2.setObjectName(u"l_d2")
        sizePolicy.setHeightForWidth(self.l_d2.sizePolicy().hasHeightForWidth())
        self.l_d2.setSizePolicy(sizePolicy)
        self.l_d2.setFont(font)
        self.l_d2.setStyleSheet(u"color:red")

        self.gl_main.addWidget(self.l_d2, 2, 0, 1, 17)

        self.hl_d1 = QHBoxLayout()
        self.hl_d1.setSpacing(3)
        self.hl_d1.setObjectName(u"hl_d1")
        self.le_d1_x1 = QLineEdit(self.centralwidget)
        self.le_d1_x1.setObjectName(u"le_d1_x1")
        sizePolicy1.setHeightForWidth(self.le_d1_x1.sizePolicy().hasHeightForWidth())
        self.le_d1_x1.setSizePolicy(sizePolicy1)
        self.le_d1_x1.setMaximumSize(QSize(44, 16777215))
        self.le_d1_x1.setFont(font2)
        self.le_d1_x1.setMaxLength(3)
        self.le_d1_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.le_d1_x1)

        self.l_d1_x1 = QLabel(self.centralwidget)
        self.l_d1_x1.setObjectName(u"l_d1_x1")
        sizePolicy1.setHeightForWidth(self.l_d1_x1.sizePolicy().hasHeightForWidth())
        self.l_d1_x1.setSizePolicy(sizePolicy1)
        self.l_d1_x1.setFont(font1)
        self.l_d1_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x1)

        self.l_d1_x1_plus = QLabel(self.centralwidget)
        self.l_d1_x1_plus.setObjectName(u"l_d1_x1_plus")
        sizePolicy1.setHeightForWidth(self.l_d1_x1_plus.sizePolicy().hasHeightForWidth())
        self.l_d1_x1_plus.setSizePolicy(sizePolicy1)
        self.l_d1_x1_plus.setFont(font1)
        self.l_d1_x1_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x1_plus)

        self.le_d1_x2 = QLineEdit(self.centralwidget)
        self.le_d1_x2.setObjectName(u"le_d1_x2")
        sizePolicy1.setHeightForWidth(self.le_d1_x2.sizePolicy().hasHeightForWidth())
        self.le_d1_x2.setSizePolicy(sizePolicy1)
        self.le_d1_x2.setMaximumSize(QSize(44, 16777215))
        self.le_d1_x2.setFont(font2)
        self.le_d1_x2.setMaxLength(3)
        self.le_d1_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.le_d1_x2)

        self.l_d1_x2 = QLabel(self.centralwidget)
        self.l_d1_x2.setObjectName(u"l_d1_x2")
        sizePolicy1.setHeightForWidth(self.l_d1_x2.sizePolicy().hasHeightForWidth())
        self.l_d1_x2.setSizePolicy(sizePolicy1)
        self.l_d1_x2.setFont(font1)
        self.l_d1_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x2)

        self.l_d1_x2_plus = QLabel(self.centralwidget)
        self.l_d1_x2_plus.setObjectName(u"l_d1_x2_plus")
        sizePolicy1.setHeightForWidth(self.l_d1_x2_plus.sizePolicy().hasHeightForWidth())
        self.l_d1_x2_plus.setSizePolicy(sizePolicy1)
        self.l_d1_x2_plus.setFont(font1)
        self.l_d1_x2_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x2_plus)

        self.le_d1_x3 = QLineEdit(self.centralwidget)
        self.le_d1_x3.setObjectName(u"le_d1_x3")
        sizePolicy1.setHeightForWidth(self.le_d1_x3.sizePolicy().hasHeightForWidth())
        self.le_d1_x3.setSizePolicy(sizePolicy1)
        self.le_d1_x3.setMaximumSize(QSize(44, 16777215))
        self.le_d1_x3.setFont(font2)
        self.le_d1_x3.setMaxLength(3)
        self.le_d1_x3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.le_d1_x3)

        self.l_d1_x3 = QLabel(self.centralwidget)
        self.l_d1_x3.setObjectName(u"l_d1_x3")
        sizePolicy1.setHeightForWidth(self.l_d1_x3.sizePolicy().hasHeightForWidth())
        self.l_d1_x3.setSizePolicy(sizePolicy1)
        self.l_d1_x3.setFont(font1)
        self.l_d1_x3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x3)

        self.l_d1_x3_plus = QLabel(self.centralwidget)
        self.l_d1_x3_plus.setObjectName(u"l_d1_x3_plus")
        sizePolicy1.setHeightForWidth(self.l_d1_x3_plus.sizePolicy().hasHeightForWidth())
        self.l_d1_x3_plus.setSizePolicy(sizePolicy1)
        self.l_d1_x3_plus.setFont(font1)
        self.l_d1_x3_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x3_plus)

        self.le_d1_x4 = QLineEdit(self.centralwidget)
        self.le_d1_x4.setObjectName(u"le_d1_x4")
        sizePolicy1.setHeightForWidth(self.le_d1_x4.sizePolicy().hasHeightForWidth())
        self.le_d1_x4.setSizePolicy(sizePolicy1)
        self.le_d1_x4.setMaximumSize(QSize(44, 16777215))
        self.le_d1_x4.setFont(font2)
        self.le_d1_x4.setMaxLength(3)
        self.le_d1_x4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.le_d1_x4)

        self.l_d1_x4 = QLabel(self.centralwidget)
        self.l_d1_x4.setObjectName(u"l_d1_x4")
        sizePolicy1.setHeightForWidth(self.l_d1_x4.sizePolicy().hasHeightForWidth())
        self.l_d1_x4.setSizePolicy(sizePolicy1)
        self.l_d1_x4.setFont(font1)
        self.l_d1_x4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x4)

        self.l_d1_x4_plus = QLabel(self.centralwidget)
        self.l_d1_x4_plus.setObjectName(u"l_d1_x4_plus")
        sizePolicy1.setHeightForWidth(self.l_d1_x4_plus.sizePolicy().hasHeightForWidth())
        self.l_d1_x4_plus.setSizePolicy(sizePolicy1)
        self.l_d1_x4_plus.setFont(font1)
        self.l_d1_x4_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x4_plus)

        self.le_d1_x5 = QLineEdit(self.centralwidget)
        self.le_d1_x5.setObjectName(u"le_d1_x5")
        sizePolicy1.setHeightForWidth(self.le_d1_x5.sizePolicy().hasHeightForWidth())
        self.le_d1_x5.setSizePolicy(sizePolicy1)
        self.le_d1_x5.setMaximumSize(QSize(44, 16777215))
        self.le_d1_x5.setFont(font2)
        self.le_d1_x5.setMaxLength(3)
        self.le_d1_x5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.le_d1_x5)

        self.l_d1_x5 = QLabel(self.centralwidget)
        self.l_d1_x5.setObjectName(u"l_d1_x5")
        sizePolicy1.setHeightForWidth(self.l_d1_x5.sizePolicy().hasHeightForWidth())
        self.l_d1_x5.setSizePolicy(sizePolicy1)
        self.l_d1_x5.setFont(font1)
        self.l_d1_x5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x5)

        self.l_d1_x5_plus = QLabel(self.centralwidget)
        self.l_d1_x5_plus.setObjectName(u"l_d1_x5_plus")
        sizePolicy1.setHeightForWidth(self.l_d1_x5_plus.sizePolicy().hasHeightForWidth())
        self.l_d1_x5_plus.setSizePolicy(sizePolicy1)
        self.l_d1_x5_plus.setFont(font1)
        self.l_d1_x5_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x5_plus)

        self.le_d1_x6 = QLineEdit(self.centralwidget)
        self.le_d1_x6.setObjectName(u"le_d1_x6")
        sizePolicy1.setHeightForWidth(self.le_d1_x6.sizePolicy().hasHeightForWidth())
        self.le_d1_x6.setSizePolicy(sizePolicy1)
        self.le_d1_x6.setMaximumSize(QSize(44, 16777215))
        self.le_d1_x6.setFont(font2)
        self.le_d1_x6.setMaxLength(3)
        self.le_d1_x6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.le_d1_x6)

        self.l_d1_x6 = QLabel(self.centralwidget)
        self.l_d1_x6.setObjectName(u"l_d1_x6")
        sizePolicy1.setHeightForWidth(self.l_d1_x6.sizePolicy().hasHeightForWidth())
        self.l_d1_x6.setSizePolicy(sizePolicy1)
        self.l_d1_x6.setFont(font1)
        self.l_d1_x6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d1.addWidget(self.l_d1_x6)


        self.gl_main.addLayout(self.hl_d1, 1, 0, 1, 17)

        self.hl_d2 = QHBoxLayout()
        self.hl_d2.setSpacing(3)
        self.hl_d2.setObjectName(u"hl_d2")
        self.le_d2_x1 = QLineEdit(self.centralwidget)
        self.le_d2_x1.setObjectName(u"le_d2_x1")
        sizePolicy1.setHeightForWidth(self.le_d2_x1.sizePolicy().hasHeightForWidth())
        self.le_d2_x1.setSizePolicy(sizePolicy1)
        self.le_d2_x1.setMaximumSize(QSize(44, 16777215))
        self.le_d2_x1.setFont(font2)
        self.le_d2_x1.setMaxLength(3)
        self.le_d2_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.le_d2_x1)

        self.l_d2_x1 = QLabel(self.centralwidget)
        self.l_d2_x1.setObjectName(u"l_d2_x1")
        sizePolicy1.setHeightForWidth(self.l_d2_x1.sizePolicy().hasHeightForWidth())
        self.l_d2_x1.setSizePolicy(sizePolicy1)
        self.l_d2_x1.setFont(font1)
        self.l_d2_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x1)

        self.l_d2_x1_plus = QLabel(self.centralwidget)
        self.l_d2_x1_plus.setObjectName(u"l_d2_x1_plus")
        sizePolicy1.setHeightForWidth(self.l_d2_x1_plus.sizePolicy().hasHeightForWidth())
        self.l_d2_x1_plus.setSizePolicy(sizePolicy1)
        self.l_d2_x1_plus.setFont(font1)
        self.l_d2_x1_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x1_plus)

        self.le_d2_x2 = QLineEdit(self.centralwidget)
        self.le_d2_x2.setObjectName(u"le_d2_x2")
        sizePolicy1.setHeightForWidth(self.le_d2_x2.sizePolicy().hasHeightForWidth())
        self.le_d2_x2.setSizePolicy(sizePolicy1)
        self.le_d2_x2.setMaximumSize(QSize(44, 16777215))
        self.le_d2_x2.setFont(font2)
        self.le_d2_x2.setMaxLength(3)
        self.le_d2_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.le_d2_x2)

        self.l_d2_x2 = QLabel(self.centralwidget)
        self.l_d2_x2.setObjectName(u"l_d2_x2")
        sizePolicy1.setHeightForWidth(self.l_d2_x2.sizePolicy().hasHeightForWidth())
        self.l_d2_x2.setSizePolicy(sizePolicy1)
        self.l_d2_x2.setFont(font1)
        self.l_d2_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x2)

        self.l_d2_x2_plus = QLabel(self.centralwidget)
        self.l_d2_x2_plus.setObjectName(u"l_d2_x2_plus")
        sizePolicy1.setHeightForWidth(self.l_d2_x2_plus.sizePolicy().hasHeightForWidth())
        self.l_d2_x2_plus.setSizePolicy(sizePolicy1)
        self.l_d2_x2_plus.setFont(font1)
        self.l_d2_x2_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x2_plus)

        self.le_d2_x3 = QLineEdit(self.centralwidget)
        self.le_d2_x3.setObjectName(u"le_d2_x3")
        sizePolicy1.setHeightForWidth(self.le_d2_x3.sizePolicy().hasHeightForWidth())
        self.le_d2_x3.setSizePolicy(sizePolicy1)
        self.le_d2_x3.setMaximumSize(QSize(44, 16777215))
        self.le_d2_x3.setFont(font2)
        self.le_d2_x3.setMaxLength(3)
        self.le_d2_x3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.le_d2_x3)

        self.l_d2_x3 = QLabel(self.centralwidget)
        self.l_d2_x3.setObjectName(u"l_d2_x3")
        sizePolicy1.setHeightForWidth(self.l_d2_x3.sizePolicy().hasHeightForWidth())
        self.l_d2_x3.setSizePolicy(sizePolicy1)
        self.l_d2_x3.setFont(font1)
        self.l_d2_x3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x3)

        self.l_d2_x3_plus = QLabel(self.centralwidget)
        self.l_d2_x3_plus.setObjectName(u"l_d2_x3_plus")
        sizePolicy1.setHeightForWidth(self.l_d2_x3_plus.sizePolicy().hasHeightForWidth())
        self.l_d2_x3_plus.setSizePolicy(sizePolicy1)
        self.l_d2_x3_plus.setFont(font1)
        self.l_d2_x3_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x3_plus)

        self.le_d2_x4 = QLineEdit(self.centralwidget)
        self.le_d2_x4.setObjectName(u"le_d2_x4")
        sizePolicy1.setHeightForWidth(self.le_d2_x4.sizePolicy().hasHeightForWidth())
        self.le_d2_x4.setSizePolicy(sizePolicy1)
        self.le_d2_x4.setMaximumSize(QSize(44, 16777215))
        self.le_d2_x4.setFont(font2)
        self.le_d2_x4.setMaxLength(3)
        self.le_d2_x4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.le_d2_x4)

        self.l_d2_x4 = QLabel(self.centralwidget)
        self.l_d2_x4.setObjectName(u"l_d2_x4")
        sizePolicy1.setHeightForWidth(self.l_d2_x4.sizePolicy().hasHeightForWidth())
        self.l_d2_x4.setSizePolicy(sizePolicy1)
        self.l_d2_x4.setFont(font1)
        self.l_d2_x4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x4)

        self.l_d2_x4_plus = QLabel(self.centralwidget)
        self.l_d2_x4_plus.setObjectName(u"l_d2_x4_plus")
        sizePolicy1.setHeightForWidth(self.l_d2_x4_plus.sizePolicy().hasHeightForWidth())
        self.l_d2_x4_plus.setSizePolicy(sizePolicy1)
        self.l_d2_x4_plus.setFont(font1)
        self.l_d2_x4_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x4_plus)

        self.le_d2_x5 = QLineEdit(self.centralwidget)
        self.le_d2_x5.setObjectName(u"le_d2_x5")
        sizePolicy1.setHeightForWidth(self.le_d2_x5.sizePolicy().hasHeightForWidth())
        self.le_d2_x5.setSizePolicy(sizePolicy1)
        self.le_d2_x5.setMaximumSize(QSize(44, 16777215))
        self.le_d2_x5.setFont(font2)
        self.le_d2_x5.setMaxLength(3)
        self.le_d2_x5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.le_d2_x5)

        self.l_d2_x5 = QLabel(self.centralwidget)
        self.l_d2_x5.setObjectName(u"l_d2_x5")
        sizePolicy1.setHeightForWidth(self.l_d2_x5.sizePolicy().hasHeightForWidth())
        self.l_d2_x5.setSizePolicy(sizePolicy1)
        self.l_d2_x5.setFont(font1)
        self.l_d2_x5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x5)

        self.l_d2_x5_plus = QLabel(self.centralwidget)
        self.l_d2_x5_plus.setObjectName(u"l_d2_x5_plus")
        sizePolicy1.setHeightForWidth(self.l_d2_x5_plus.sizePolicy().hasHeightForWidth())
        self.l_d2_x5_plus.setSizePolicy(sizePolicy1)
        self.l_d2_x5_plus.setFont(font1)
        self.l_d2_x5_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x5_plus)

        self.le_d2_x6 = QLineEdit(self.centralwidget)
        self.le_d2_x6.setObjectName(u"le_d2_x6")
        sizePolicy1.setHeightForWidth(self.le_d2_x6.sizePolicy().hasHeightForWidth())
        self.le_d2_x6.setSizePolicy(sizePolicy1)
        self.le_d2_x6.setMaximumSize(QSize(44, 16777215))
        self.le_d2_x6.setFont(font2)
        self.le_d2_x6.setMaxLength(3)
        self.le_d2_x6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.le_d2_x6)

        self.l_d2_x6 = QLabel(self.centralwidget)
        self.l_d2_x6.setObjectName(u"l_d2_x6")
        sizePolicy1.setHeightForWidth(self.l_d2_x6.sizePolicy().hasHeightForWidth())
        self.l_d2_x6.setSizePolicy(sizePolicy1)
        self.l_d2_x6.setFont(font1)
        self.l_d2_x6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_d2.addWidget(self.l_d2_x6)


        self.gl_main.addLayout(self.hl_d2, 3, 0, 1, 17)

        self.l_d1 = QLabel(self.centralwidget)
        self.l_d1.setObjectName(u"l_d1")
        sizePolicy.setHeightForWidth(self.l_d1.sizePolicy().hasHeightForWidth())
        self.l_d1.setSizePolicy(sizePolicy)
        self.l_d1.setFont(font)
        self.l_d1.setStyleSheet(u"color:red")

        self.gl_main.addWidget(self.l_d1, 0, 0, 1, 17)

        self.hl_t1 = QHBoxLayout()
        self.hl_t1.setSpacing(6)
        self.hl_t1.setObjectName(u"hl_t1")
        self.l_t1_x1 = QLabel(self.centralwidget)
        self.l_t1_x1.setObjectName(u"l_t1_x1")
        sizePolicy1.setHeightForWidth(self.l_t1_x1.sizePolicy().hasHeightForWidth())
        self.l_t1_x1.setSizePolicy(sizePolicy1)
        self.l_t1_x1.setFont(font1)
        self.l_t1_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t1.addWidget(self.l_t1_x1)

        self.l_t1_x1_plus = QLabel(self.centralwidget)
        self.l_t1_x1_plus.setObjectName(u"l_t1_x1_plus")
        sizePolicy1.setHeightForWidth(self.l_t1_x1_plus.sizePolicy().hasHeightForWidth())
        self.l_t1_x1_plus.setSizePolicy(sizePolicy1)
        self.l_t1_x1_plus.setFont(font1)
        self.l_t1_x1_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t1.addWidget(self.l_t1_x1_plus)

        self.l_t1_x2 = QLabel(self.centralwidget)
        self.l_t1_x2.setObjectName(u"l_t1_x2")
        sizePolicy1.setHeightForWidth(self.l_t1_x2.sizePolicy().hasHeightForWidth())
        self.l_t1_x2.setSizePolicy(sizePolicy1)
        self.l_t1_x2.setFont(font1)
        self.l_t1_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t1.addWidget(self.l_t1_x2)

        self.l_t1_x2_plus = QLabel(self.centralwidget)
        self.l_t1_x2_plus.setObjectName(u"l_t1_x2_plus")
        sizePolicy1.setHeightForWidth(self.l_t1_x2_plus.sizePolicy().hasHeightForWidth())
        self.l_t1_x2_plus.setSizePolicy(sizePolicy1)
        self.l_t1_x2_plus.setFont(font1)
        self.l_t1_x2_plus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t1.addWidget(self.l_t1_x2_plus)

        self.l_t1_x3 = QLabel(self.centralwidget)
        self.l_t1_x3.setObjectName(u"l_t1_x3")
        sizePolicy1.setHeightForWidth(self.l_t1_x3.sizePolicy().hasHeightForWidth())
        self.l_t1_x3.setSizePolicy(sizePolicy1)
        self.l_t1_x3.setFont(font1)
        self.l_t1_x3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t1.addWidget(self.l_t1_x3)

        self.l_t1_le = QLabel(self.centralwidget)
        self.l_t1_le.setObjectName(u"l_t1_le")
        sizePolicy1.setHeightForWidth(self.l_t1_le.sizePolicy().hasHeightForWidth())
        self.l_t1_le.setSizePolicy(sizePolicy1)
        self.l_t1_le.setFont(font1)
        self.l_t1_le.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t1.addWidget(self.l_t1_le)

        self.le_t1_rhs = QLineEdit(self.centralwidget)
        self.le_t1_rhs.setObjectName(u"le_t1_rhs")
        sizePolicy2.setHeightForWidth(self.le_t1_rhs.sizePolicy().hasHeightForWidth())
        self.le_t1_rhs.setSizePolicy(sizePolicy2)
        self.le_t1_rhs.setMaximumSize(QSize(66, 16777215))
        self.le_t1_rhs.setFont(font2)
        self.le_t1_rhs.setMaxLength(5)
        self.le_t1_rhs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_t1.addWidget(self.le_t1_rhs)

        self.hs_t1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_t1.addItem(self.hs_t1)


        self.gl_main.addLayout(self.hl_t1, 5, 0, 1, 17)

        self.l_t1 = QLabel(self.centralwidget)
        self.l_t1.setObjectName(u"l_t1")
        sizePolicy.setHeightForWidth(self.l_t1.sizePolicy().hasHeightForWidth())
        self.l_t1.setSizePolicy(sizePolicy)
        self.l_t1.setFont(font)
        self.l_t1.setStyleSheet(u"color:red")

        self.gl_main.addWidget(self.l_t1, 4, 0, 1, 17)

        GivenWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GivenWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 533, 33))
        self.m_solution = QMenu(self.menubar)
        self.m_solution.setObjectName(u"m_solution")
        self.m_task = QMenu(self.menubar)
        self.m_task.setObjectName(u"m_task")
        GivenWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GivenWindow)
        self.statusbar.setObjectName(u"statusbar")
        GivenWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.le_t1_rhs, self.le_t2_rhs)
        QWidget.setTabOrder(self.le_t2_rhs, self.le_d1_x1)
        QWidget.setTabOrder(self.le_d1_x1, self.le_d1_x2)
        QWidget.setTabOrder(self.le_d1_x2, self.le_d1_x3)
        QWidget.setTabOrder(self.le_d1_x3, self.le_d1_x4)
        QWidget.setTabOrder(self.le_d1_x4, self.le_d1_x5)
        QWidget.setTabOrder(self.le_d1_x5, self.le_d1_x6)
        QWidget.setTabOrder(self.le_d1_x6, self.le_d2_x1)
        QWidget.setTabOrder(self.le_d2_x1, self.le_d2_x2)
        QWidget.setTabOrder(self.le_d2_x2, self.le_d2_x3)
        QWidget.setTabOrder(self.le_d2_x3, self.le_d2_x4)
        QWidget.setTabOrder(self.le_d2_x4, self.le_d2_x5)
        QWidget.setTabOrder(self.le_d2_x5, self.le_d2_x6)

        self.menubar.addAction(self.m_solution.menuAction())
        self.menubar.addAction(self.m_task.menuAction())
        self.m_solution.addAction(self.a_find_solution)
        self.m_task.addAction(self.a_put_task)
        self.m_task.addAction(self.a_show_task)

        self.retranslateUi(GivenWindow)

        QMetaObject.connectSlotsByName(GivenWindow)
    # setupUi

    def retranslateUi(self, GivenWindow):
        GivenWindow.setWindowTitle(QCoreApplication.translate("GivenWindow", u"\u0412\u0430\u0440\u0438\u0430\u043d\u0442 7", None))
        self.a_put_task.setText(QCoreApplication.translate("GivenWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.a_show_task.setText(QCoreApplication.translate("GivenWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c", None))
        self.a_find_solution.setText(QCoreApplication.translate("GivenWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.l_t2.setText(QCoreApplication.translate("GivenWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043a\u0430\u043d\u0438 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0442\u0438\u043f\u0430", None))
        self.l_t2_x4.setText(QCoreApplication.translate("GivenWindow", u"x4", None))
        self.l_t2_x4_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.l_t2_x5.setText(QCoreApplication.translate("GivenWindow", u"x5", None))
        self.l_t2_x5_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.l_t2_x6.setText(QCoreApplication.translate("GivenWindow", u"x6", None))
        self.l_t2_le.setText(QCoreApplication.translate("GivenWindow", u"\u2264", None))
        self.l_d2.setText(QCoreApplication.translate("GivenWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0442\u0438\u043f\u0430", None))
        self.le_d1_x1.setText("")
        self.l_d1_x1.setText(QCoreApplication.translate("GivenWindow", u"x1", None))
        self.l_d1_x1_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d1_x2.setText("")
        self.l_d1_x2.setText(QCoreApplication.translate("GivenWindow", u"x2", None))
        self.l_d1_x2_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d1_x3.setText("")
        self.l_d1_x3.setText(QCoreApplication.translate("GivenWindow", u"x3", None))
        self.l_d1_x3_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d1_x4.setText("")
        self.l_d1_x4.setText(QCoreApplication.translate("GivenWindow", u"x4", None))
        self.l_d1_x4_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d1_x5.setText("")
        self.l_d1_x5.setText(QCoreApplication.translate("GivenWindow", u"x5", None))
        self.l_d1_x5_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d1_x6.setText("")
        self.l_d1_x6.setText(QCoreApplication.translate("GivenWindow", u"x6", None))
        self.le_d2_x1.setText("")
        self.l_d2_x1.setText(QCoreApplication.translate("GivenWindow", u"x1", None))
        self.l_d2_x1_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d2_x2.setText("")
        self.l_d2_x2.setText(QCoreApplication.translate("GivenWindow", u"x2", None))
        self.l_d2_x2_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d2_x3.setText("")
        self.l_d2_x3.setText(QCoreApplication.translate("GivenWindow", u"x3", None))
        self.l_d2_x3_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d2_x4.setText("")
        self.l_d2_x4.setText(QCoreApplication.translate("GivenWindow", u"x4", None))
        self.l_d2_x4_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d2_x5.setText("")
        self.l_d2_x5.setText(QCoreApplication.translate("GivenWindow", u"x5", None))
        self.l_d2_x5_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.le_d2_x6.setText("")
        self.l_d2_x6.setText(QCoreApplication.translate("GivenWindow", u"x6", None))
        self.l_d1.setText(QCoreApplication.translate("GivenWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0442\u0438\u043f\u0430", None))
        self.l_t1_x1.setText(QCoreApplication.translate("GivenWindow", u"x1", None))
        self.l_t1_x1_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.l_t1_x2.setText(QCoreApplication.translate("GivenWindow", u"x2", None))
        self.l_t1_x2_plus.setText(QCoreApplication.translate("GivenWindow", u"+", None))
        self.l_t1_x3.setText(QCoreApplication.translate("GivenWindow", u"x3", None))
        self.l_t1_le.setText(QCoreApplication.translate("GivenWindow", u"\u2264", None))
        self.l_t1.setText(QCoreApplication.translate("GivenWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043a\u0430\u043d\u0438 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0442\u0438\u043f\u0430", None))
        self.m_solution.setTitle(QCoreApplication.translate("GivenWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.m_task.setTitle(QCoreApplication.translate("GivenWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None))
    # retranslateUi

