# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)
import resources_rc

class Ui_LibArchiveWindow(object):
    def setupUi(self, LibArchiveWindow):
        if not LibArchiveWindow.objectName():
            LibArchiveWindow.setObjectName(u"LibArchiveWindow")
        LibArchiveWindow.resize(650, 300)
        LibArchiveWindow.setMinimumSize(QSize(650, 300))
        self.gl_main = QGridLayout(LibArchiveWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.hl_books_bar = QHBoxLayout()
        self.hl_books_bar.setObjectName(u"hl_books_bar")
        self.pb_books_filter = QPushButton(LibArchiveWindow)
        self.pb_books_filter.setObjectName(u"pb_books_filter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_books_filter.sizePolicy().hasHeightForWidth())
        self.pb_books_filter.setSizePolicy(sizePolicy)
        self.pb_books_filter.setMinimumSize(QSize(28, 28))
        self.pb_books_filter.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/ico/icons/filter.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_books_filter.setIcon(icon)
        self.pb_books_filter.setIconSize(QSize(16, 16))

        self.hl_books_bar.addWidget(self.pb_books_filter)

        self.l_books = QLabel(LibArchiveWindow)
        self.l_books.setObjectName(u"l_books")
        self.l_books.setMaximumSize(QSize(16777211, 16777215))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.l_books.setFont(font)

        self.hl_books_bar.addWidget(self.l_books)

        self.pb_books_add = QPushButton(LibArchiveWindow)
        self.pb_books_add.setObjectName(u"pb_books_add")
        sizePolicy.setHeightForWidth(self.pb_books_add.sizePolicy().hasHeightForWidth())
        self.pb_books_add.setSizePolicy(sizePolicy)
        self.pb_books_add.setMinimumSize(QSize(28, 28))
        self.pb_books_add.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/ico/icons/plus.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_books_add.setIcon(icon1)
        self.pb_books_add.setIconSize(QSize(16, 16))

        self.hl_books_bar.addWidget(self.pb_books_add)

        self.pb_books_remove = QPushButton(LibArchiveWindow)
        self.pb_books_remove.setObjectName(u"pb_books_remove")
        sizePolicy.setHeightForWidth(self.pb_books_remove.sizePolicy().hasHeightForWidth())
        self.pb_books_remove.setSizePolicy(sizePolicy)
        self.pb_books_remove.setMinimumSize(QSize(28, 28))
        self.pb_books_remove.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/ico/icons/minus.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_books_remove.setIcon(icon2)
        self.pb_books_remove.setIconSize(QSize(16, 16))

        self.hl_books_bar.addWidget(self.pb_books_remove)

        self.pb_books_edit = QPushButton(LibArchiveWindow)
        self.pb_books_edit.setObjectName(u"pb_books_edit")
        sizePolicy.setHeightForWidth(self.pb_books_edit.sizePolicy().hasHeightForWidth())
        self.pb_books_edit.setSizePolicy(sizePolicy)
        self.pb_books_edit.setMinimumSize(QSize(28, 28))
        self.pb_books_edit.setMaximumSize(QSize(28, 28))
        icon3 = QIcon()
        icon3.addFile(u":/ico/icons/pencil.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_books_edit.setIcon(icon3)
        self.pb_books_edit.setIconSize(QSize(16, 16))

        self.hl_books_bar.addWidget(self.pb_books_edit)


        self.gl_main.addLayout(self.hl_books_bar, 3, 1, 1, 1)

        self.tw_books = QTableWidget(LibArchiveWindow)
        self.tw_books.setObjectName(u"tw_books")

        self.gl_main.addWidget(self.tw_books, 4, 1, 4, 1)

        self.tw_subscribers = QTableWidget(LibArchiveWindow)
        self.tw_subscribers.setObjectName(u"tw_subscribers")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tw_subscribers.sizePolicy().hasHeightForWidth())
        self.tw_subscribers.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.tw_subscribers, 7, 0, 1, 1)

        self.tw_borrowers = QTableWidget(LibArchiveWindow)
        self.tw_borrowers.setObjectName(u"tw_borrowers")
        sizePolicy1.setHeightForWidth(self.tw_borrowers.sizePolicy().hasHeightForWidth())
        self.tw_borrowers.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.tw_borrowers, 4, 0, 1, 1)

        self.gl_actions = QGridLayout()
        self.gl_actions.setObjectName(u"gl_actions")
        self.pb_borrow_a_book = QPushButton(LibArchiveWindow)
        self.pb_borrow_a_book.setObjectName(u"pb_borrow_a_book")

        self.gl_actions.addWidget(self.pb_borrow_a_book, 0, 0, 1, 1)

        self.pb_return_a_book = QPushButton(LibArchiveWindow)
        self.pb_return_a_book.setObjectName(u"pb_return_a_book")

        self.gl_actions.addWidget(self.pb_return_a_book, 0, 1, 1, 1)

        self.pb_marked_lost = QPushButton(LibArchiveWindow)
        self.pb_marked_lost.setObjectName(u"pb_marked_lost")

        self.gl_actions.addWidget(self.pb_marked_lost, 1, 0, 1, 1)

        self.pb_lost_books = QPushButton(LibArchiveWindow)
        self.pb_lost_books.setObjectName(u"pb_lost_books")

        self.gl_actions.addWidget(self.pb_lost_books, 1, 1, 1, 1)


        self.gl_main.addLayout(self.gl_actions, 5, 0, 1, 1)

        self.hl_borrowers_bar = QHBoxLayout()
        self.hl_borrowers_bar.setObjectName(u"hl_borrowers_bar")
        self.pb_borrowers_filter = QPushButton(LibArchiveWindow)
        self.pb_borrowers_filter.setObjectName(u"pb_borrowers_filter")
        sizePolicy.setHeightForWidth(self.pb_borrowers_filter.sizePolicy().hasHeightForWidth())
        self.pb_borrowers_filter.setSizePolicy(sizePolicy)
        self.pb_borrowers_filter.setMinimumSize(QSize(28, 28))
        self.pb_borrowers_filter.setMaximumSize(QSize(28, 28))
        self.pb_borrowers_filter.setIcon(icon)
        self.pb_borrowers_filter.setIconSize(QSize(16, 16))

        self.hl_borrowers_bar.addWidget(self.pb_borrowers_filter)

        self.l_borrowers = QLabel(LibArchiveWindow)
        self.l_borrowers.setObjectName(u"l_borrowers")
        self.l_borrowers.setMaximumSize(QSize(16777211, 16777215))
        self.l_borrowers.setFont(font)

        self.hl_borrowers_bar.addWidget(self.l_borrowers)


        self.gl_main.addLayout(self.hl_borrowers_bar, 3, 0, 1, 1)

        self.hl_subsribers_bar = QHBoxLayout()
        self.hl_subsribers_bar.setObjectName(u"hl_subsribers_bar")
        self.pb_subsribers_filter = QPushButton(LibArchiveWindow)
        self.pb_subsribers_filter.setObjectName(u"pb_subsribers_filter")
        sizePolicy.setHeightForWidth(self.pb_subsribers_filter.sizePolicy().hasHeightForWidth())
        self.pb_subsribers_filter.setSizePolicy(sizePolicy)
        self.pb_subsribers_filter.setMinimumSize(QSize(28, 28))
        self.pb_subsribers_filter.setMaximumSize(QSize(28, 28))
        self.pb_subsribers_filter.setIcon(icon)
        self.pb_subsribers_filter.setIconSize(QSize(16, 16))

        self.hl_subsribers_bar.addWidget(self.pb_subsribers_filter)

        self.l_subsribers = QLabel(LibArchiveWindow)
        self.l_subsribers.setObjectName(u"l_subsribers")
        self.l_subsribers.setMaximumSize(QSize(16777211, 16777215))
        self.l_subsribers.setFont(font)

        self.hl_subsribers_bar.addWidget(self.l_subsribers)

        self.pb_subsribers_add = QPushButton(LibArchiveWindow)
        self.pb_subsribers_add.setObjectName(u"pb_subsribers_add")
        sizePolicy.setHeightForWidth(self.pb_subsribers_add.sizePolicy().hasHeightForWidth())
        self.pb_subsribers_add.setSizePolicy(sizePolicy)
        self.pb_subsribers_add.setMinimumSize(QSize(28, 28))
        self.pb_subsribers_add.setMaximumSize(QSize(28, 28))
        self.pb_subsribers_add.setIcon(icon1)
        self.pb_subsribers_add.setIconSize(QSize(16, 16))

        self.hl_subsribers_bar.addWidget(self.pb_subsribers_add)

        self.pb_subscribers_remove = QPushButton(LibArchiveWindow)
        self.pb_subscribers_remove.setObjectName(u"pb_subscribers_remove")
        sizePolicy.setHeightForWidth(self.pb_subscribers_remove.sizePolicy().hasHeightForWidth())
        self.pb_subscribers_remove.setSizePolicy(sizePolicy)
        self.pb_subscribers_remove.setMinimumSize(QSize(28, 28))
        self.pb_subscribers_remove.setMaximumSize(QSize(28, 28))
        self.pb_subscribers_remove.setIcon(icon2)
        self.pb_subscribers_remove.setIconSize(QSize(16, 16))

        self.hl_subsribers_bar.addWidget(self.pb_subscribers_remove)

        self.pb_subscribers_edit = QPushButton(LibArchiveWindow)
        self.pb_subscribers_edit.setObjectName(u"pb_subscribers_edit")
        sizePolicy.setHeightForWidth(self.pb_subscribers_edit.sizePolicy().hasHeightForWidth())
        self.pb_subscribers_edit.setSizePolicy(sizePolicy)
        self.pb_subscribers_edit.setMinimumSize(QSize(28, 28))
        self.pb_subscribers_edit.setMaximumSize(QSize(28, 28))
        self.pb_subscribers_edit.setIcon(icon3)
        self.pb_subscribers_edit.setIconSize(QSize(16, 16))

        self.hl_subsribers_bar.addWidget(self.pb_subscribers_edit)


        self.gl_main.addLayout(self.hl_subsribers_bar, 6, 0, 1, 1)


        self.retranslateUi(LibArchiveWindow)

        QMetaObject.connectSlotsByName(LibArchiveWindow)
    # setupUi

    def retranslateUi(self, LibArchiveWindow):
        LibArchiveWindow.setWindowTitle(QCoreApplication.translate("LibArchiveWindow", u"\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430", None))
#if QT_CONFIG(tooltip)
        self.pb_books_filter.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043a\u043d\u0438\u0433", None))
#endif // QT_CONFIG(tooltip)
        self.pb_books_filter.setText("")
        self.l_books.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041a\u043d\u0438\u0433\u0438", None))
#if QT_CONFIG(tooltip)
        self.pb_books_add.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043d\u0438\u0433\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.pb_books_add.setText("")
#if QT_CONFIG(tooltip)
        self.pb_books_remove.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u043d\u0438\u0433\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.pb_books_remove.setText("")
#if QT_CONFIG(tooltip)
        self.pb_books_edit.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043a\u043d\u0438\u0433\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.pb_books_edit.setText("")
        self.pb_borrow_a_book.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041e\u0434\u043e\u043b\u0436\u0438\u0442\u044c \u043a\u043d\u0438\u0433\u0443", None))
        self.pb_return_a_book.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c \u043a\u043d\u0438\u0433\u0443", None))
        self.pb_marked_lost.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c \u0443\u0442\u0435\u0440\u044f\u043d\u043d\u043e\u0439", None))
        self.pb_lost_books.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0423\u0442\u0435\u0440\u044f\u043d\u043d\u044b\u0435 \u043a\u043d\u0438\u0433\u0438", None))
#if QT_CONFIG(tooltip)
        self.pb_borrowers_filter.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u0434\u043e\u043b\u0436\u043d\u0438\u043a\u043e\u0432", None))
#endif // QT_CONFIG(tooltip)
        self.pb_borrowers_filter.setText("")
        self.l_borrowers.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0414\u043e\u043b\u0436\u043d\u0438\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.pb_subsribers_filter.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u043e\u0432", None))
#endif // QT_CONFIG(tooltip)
        self.pb_subsribers_filter.setText("")
        self.l_subsribers.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.pb_subsribers_add.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.pb_subsribers_add.setText("")
#if QT_CONFIG(tooltip)
        self.pb_subscribers_remove.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.pb_subscribers_remove.setText("")
#if QT_CONFIG(tooltip)
        self.pb_subscribers_edit.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.pb_subscribers_edit.setText("")
    # retranslateUi

