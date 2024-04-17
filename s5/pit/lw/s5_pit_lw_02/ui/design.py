# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QWidget)

class Ui_ImageEditorWindow(object):
    def setupUi(self, ImageEditorWindow):
        if not ImageEditorWindow.objectName():
            ImageEditorWindow.setObjectName(u"ImageEditorWindow")
        ImageEditorWindow.resize(400, 400)
        ImageEditorWindow.setMinimumSize(QSize(400, 400))
        self.a_open = QAction(ImageEditorWindow)
        self.a_open.setObjectName(u"a_open")
        self.a_close = QAction(ImageEditorWindow)
        self.a_close.setObjectName(u"a_close")
        self.a_save = QAction(ImageEditorWindow)
        self.a_save.setObjectName(u"a_save")
        self.a_save_as = QAction(ImageEditorWindow)
        self.a_save_as.setObjectName(u"a_save_as")
        self.a_gs_simple = QAction(ImageEditorWindow)
        self.a_gs_simple.setObjectName(u"a_gs_simple")
        self.a_gs_ntscrgb = QAction(ImageEditorWindow)
        self.a_gs_ntscrgb.setObjectName(u"a_gs_ntscrgb")
        self.a_gs_histogram = QAction(ImageEditorWindow)
        self.a_gs_histogram.setObjectName(u"a_gs_histogram")
        self.a_rgb_red = QAction(ImageEditorWindow)
        self.a_rgb_red.setObjectName(u"a_rgb_red")
        self.a_rgb_green = QAction(ImageEditorWindow)
        self.a_rgb_green.setObjectName(u"a_rgb_green")
        self.a_rgb_blue = QAction(ImageEditorWindow)
        self.a_rgb_blue.setObjectName(u"a_rgb_blue")
        self.a_rgb_histogram = QAction(ImageEditorWindow)
        self.a_rgb_histogram.setObjectName(u"a_rgb_histogram")
        self.a_gs_difference = QAction(ImageEditorWindow)
        self.a_gs_difference.setObjectName(u"a_gs_difference")
        self.a_gs_srgb = QAction(ImageEditorWindow)
        self.a_gs_srgb.setObjectName(u"a_gs_srgb")
        self.a_hsv_edit = QAction(ImageEditorWindow)
        self.a_hsv_edit.setObjectName(u"a_hsv_edit")
        self.a_hsv_return = QAction(ImageEditorWindow)
        self.a_hsv_return.setObjectName(u"a_hsv_return")
        self.a_return = QAction(ImageEditorWindow)
        self.a_return.setObjectName(u"a_return")
        self.w_main = QWidget(ImageEditorWindow)
        self.w_main.setObjectName(u"w_main")
        self.gl_main = QGridLayout(self.w_main)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setContentsMargins(0, 0, 0, 0)
        self.i = QLabel(self.w_main)
        self.i.setObjectName(u"i")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.i.sizePolicy().hasHeightForWidth())
        self.i.setSizePolicy(sizePolicy)
        self.i.setMaximumSize(QSize(800, 800))
        self.i.setScaledContents(True)
        self.i.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.i, 0, 0, 1, 1)

        ImageEditorWindow.setCentralWidget(self.w_main)
        self.mb_main = QMenuBar(ImageEditorWindow)
        self.mb_main.setObjectName(u"mb_main")
        self.mb_main.setGeometry(QRect(0, 0, 400, 18))
        self.m_file = QMenu(self.mb_main)
        self.m_file.setObjectName(u"m_file")
        self.m_convert = QMenu(self.mb_main)
        self.m_convert.setObjectName(u"m_convert")
        self.m_gs = QMenu(self.m_convert)
        self.m_gs.setObjectName(u"m_gs")
        self.m_rgb = QMenu(self.m_convert)
        self.m_rgb.setObjectName(u"m_rgb")
        self.m_hsv = QMenu(self.mb_main)
        self.m_hsv.setObjectName(u"m_hsv")
        ImageEditorWindow.setMenuBar(self.mb_main)

        self.mb_main.addAction(self.m_file.menuAction())
        self.mb_main.addAction(self.m_convert.menuAction())
        self.mb_main.addAction(self.m_hsv.menuAction())
        self.m_file.addAction(self.a_open)
        self.m_file.addAction(self.a_close)
        self.m_file.addSeparator()
        self.m_file.addAction(self.a_save)
        self.m_file.addAction(self.a_save_as)
        self.m_file.addSeparator()
        self.m_file.addAction(self.a_return)
        self.m_convert.addAction(self.m_gs.menuAction())
        self.m_convert.addAction(self.m_rgb.menuAction())
        self.m_gs.addAction(self.a_gs_simple)
        self.m_gs.addSeparator()
        self.m_gs.addAction(self.a_gs_ntscrgb)
        self.m_gs.addAction(self.a_gs_srgb)
        self.m_gs.addAction(self.a_gs_difference)
        self.m_gs.addSeparator()
        self.m_gs.addAction(self.a_gs_histogram)
        self.m_rgb.addAction(self.a_rgb_red)
        self.m_rgb.addAction(self.a_rgb_green)
        self.m_rgb.addAction(self.a_rgb_blue)
        self.m_rgb.addSeparator()
        self.m_rgb.addAction(self.a_rgb_histogram)
        self.m_hsv.addAction(self.a_hsv_edit)

        self.retranslateUi(ImageEditorWindow)

        QMetaObject.connectSlotsByName(ImageEditorWindow)
    # setupUi

    def retranslateUi(self, ImageEditorWindow):
        ImageEditorWindow.setWindowTitle(QCoreApplication.translate("ImageEditorWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.a_open.setText(QCoreApplication.translate("ImageEditorWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.a_close.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.a_save.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.a_save_as.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.a_gs_simple.setText(QCoreApplication.translate("ImageEditorWindow", u"\u041e\u0431\u044b\u0447\u043d\u044b\u0439", None))
        self.a_gs_ntscrgb.setText(QCoreApplication.translate("ImageEditorWindow", u"NTSC RGB", None))
        self.a_gs_histogram.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0413\u0438\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u043c\u0430...", None))
        self.a_rgb_red.setText(QCoreApplication.translate("ImageEditorWindow", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.a_rgb_green.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.a_rgb_blue.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.a_rgb_histogram.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0413\u0438\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u043c\u0430...", None))
        self.a_gs_difference.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0420\u0430\u0437\u043d\u0438\u0446\u0430", None))
        self.a_gs_srgb.setText(QCoreApplication.translate("ImageEditorWindow", u"sRGB", None))
        self.a_hsv_edit.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c...", None))
        self.a_hsv_return.setText(QCoreApplication.translate("ImageEditorWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c ", None))
        self.a_return.setText(QCoreApplication.translate("ImageEditorWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.m_file.setTitle(QCoreApplication.translate("ImageEditorWindow", u"\u0424\u0430\u0439\u043b", None))
        self.m_convert.setTitle(QCoreApplication.translate("ImageEditorWindow", u"\u0426\u0432\u0435\u0442", None))
        self.m_gs.setTitle(QCoreApplication.translate("ImageEditorWindow", u"\u0427\u0435\u0440\u043d\u043e-\u0431\u0435\u043b\u044b\u0439", None))
        self.m_rgb.setTitle(QCoreApplication.translate("ImageEditorWindow", u"RGB", None))
        self.m_hsv.setTitle(QCoreApplication.translate("ImageEditorWindow", u"HSV", None))
    # retranslateUi

