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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QToolButton, QWidget)
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
        self.pb_books_filter = QToolButton(LibArchiveWindow)
        self.pb_books_filter.setObjectName(u"pb_books_filter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_books_filter.sizePolicy().hasHeightForWidth())
        self.pb_books_filter.setSizePolicy(sizePolicy)
        self.pb_books_filter.setMinimumSize(QSize(26, 26))
        self.pb_books_filter.setMaximumSize(QSize(26, 26))
        icon = QIcon()
        icon.addFile(u":/ico/icons/filter.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_books_filter.setIcon(icon)
        self.pb_books_filter.setIconSize(QSize(14, 14))

        self.hl_books_bar.addWidget(self.pb_books_filter)

        self.l_books = QLabel(LibArchiveWindow)
        self.l_books.setObjectName(u"l_books")
        self.l_books.setMaximumSize(QSize(16777211, 16777215))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.l_books.setFont(font)

        self.hl_books_bar.addWidget(self.l_books)

        self.pb_books_add = QToolButton(LibArchiveWindow)
        self.pb_books_add.setObjectName(u"pb_books_add")
        sizePolicy.setHeightForWidth(self.pb_books_add.sizePolicy().hasHeightForWidth())
        self.pb_books_add.setSizePolicy(sizePolicy)
        self.pb_books_add.setMinimumSize(QSize(26, 26))
        self.pb_books_add.setMaximumSize(QSize(26, 26))
        icon1 = QIcon()
        icon1.addFile(u":/ico/icons/plus.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_books_add.setIcon(icon1)
        self.pb_books_add.setIconSize(QSize(14, 14))

        self.hl_books_bar.addWidget(self.pb_books_add)

        self.pb_books_remove = QToolButton(LibArchiveWindow)
        self.pb_books_remove.setObjectName(u"pb_books_remove")
        sizePolicy.setHeightForWidth(self.pb_books_remove.sizePolicy().hasHeightForWidth())
        self.pb_books_remove.setSizePolicy(sizePolicy)
        self.pb_books_remove.setMinimumSize(QSize(26, 26))
        self.pb_books_remove.setMaximumSize(QSize(26, 26))
        icon2 = QIcon()
        icon2.addFile(u":/ico/icons/minus.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_books_remove.setIcon(icon2)
        self.pb_books_remove.setIconSize(QSize(14, 14))

        self.hl_books_bar.addWidget(self.pb_books_remove)

        self.pb_books_edit = QToolButton(LibArchiveWindow)
        self.pb_books_edit.setObjectName(u"pb_books_edit")
        sizePolicy.setHeightForWidth(self.pb_books_edit.sizePolicy().hasHeightForWidth())
        self.pb_books_edit.setSizePolicy(sizePolicy)
        self.pb_books_edit.setMinimumSize(QSize(26, 26))
        self.pb_books_edit.setMaximumSize(QSize(26, 26))
        icon3 = QIcon()
        icon3.addFile(u":/ico/icons/pencil.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_books_edit.setIcon(icon3)
        self.pb_books_edit.setIconSize(QSize(14, 14))

        self.hl_books_bar.addWidget(self.pb_books_edit)


        self.gl_main.addLayout(self.hl_books_bar, 2, 1, 1, 1)

        self.tw_books = QTableWidget(LibArchiveWindow)
        if (self.tw_books.columnCount() < 6):
            self.tw_books.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_books.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_books.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_books.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_books.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_books.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_books.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tw_books.setObjectName(u"tw_books")
        self.tw_books.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_books.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_books.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_books.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tw_books.setSortingEnabled(True)
        self.tw_books.verticalHeader().setVisible(False)

        self.gl_main.addWidget(self.tw_books, 3, 1, 4, 1)

        self.tw_subscribers = QTableWidget(LibArchiveWindow)
        if (self.tw_subscribers.columnCount() < 5):
            self.tw_subscribers.setColumnCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_subscribers.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_subscribers.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_subscribers.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_subscribers.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_subscribers.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        self.tw_subscribers.setObjectName(u"tw_subscribers")
        self.tw_subscribers.setMaximumSize(QSize(470, 16777215))
        self.tw_subscribers.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_subscribers.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_subscribers.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_subscribers.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tw_subscribers.setSortingEnabled(True)
        self.tw_subscribers.verticalHeader().setVisible(False)

        self.gl_main.addWidget(self.tw_subscribers, 6, 0, 1, 1)

        self.tw_borrowers = QTableWidget(LibArchiveWindow)
        if (self.tw_borrowers.columnCount() < 5):
            self.tw_borrowers.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_borrowers.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_borrowers.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_borrowers.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_borrowers.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_borrowers.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.tw_borrowers.setObjectName(u"tw_borrowers")
        self.tw_borrowers.setMaximumSize(QSize(470, 16777215))
        self.tw_borrowers.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_borrowers.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_borrowers.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_borrowers.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tw_borrowers.setSortingEnabled(True)
        self.tw_borrowers.verticalHeader().setVisible(False)

        self.gl_main.addWidget(self.tw_borrowers, 3, 0, 1, 1)

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


        self.gl_main.addLayout(self.gl_actions, 4, 0, 1, 1)

        self.hl_borrowers_bar = QHBoxLayout()
        self.hl_borrowers_bar.setObjectName(u"hl_borrowers_bar")
        self.pb_borrowers_filter = QToolButton(LibArchiveWindow)
        self.pb_borrowers_filter.setObjectName(u"pb_borrowers_filter")
        sizePolicy.setHeightForWidth(self.pb_borrowers_filter.sizePolicy().hasHeightForWidth())
        self.pb_borrowers_filter.setSizePolicy(sizePolicy)
        self.pb_borrowers_filter.setMinimumSize(QSize(26, 26))
        self.pb_borrowers_filter.setMaximumSize(QSize(26, 26))
        self.pb_borrowers_filter.setIcon(icon)
        self.pb_borrowers_filter.setIconSize(QSize(14, 14))

        self.hl_borrowers_bar.addWidget(self.pb_borrowers_filter)

        self.l_borrowers = QLabel(LibArchiveWindow)
        self.l_borrowers.setObjectName(u"l_borrowers")
        self.l_borrowers.setMaximumSize(QSize(16777211, 16777215))
        self.l_borrowers.setFont(font)

        self.hl_borrowers_bar.addWidget(self.l_borrowers)

        self.pb_borrowing_history = QPushButton(LibArchiveWindow)
        self.pb_borrowing_history.setObjectName(u"pb_borrowing_history")
        sizePolicy.setHeightForWidth(self.pb_borrowing_history.sizePolicy().hasHeightForWidth())
        self.pb_borrowing_history.setSizePolicy(sizePolicy)
        self.pb_borrowing_history.setMinimumSize(QSize(86, 26))
        self.pb_borrowing_history.setMaximumSize(QSize(86, 26))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.pb_borrowing_history.setFont(font1)

        self.hl_borrowers_bar.addWidget(self.pb_borrowing_history)


        self.gl_main.addLayout(self.hl_borrowers_bar, 2, 0, 1, 1)

        self.hl_subsribers_bar = QHBoxLayout()
        self.hl_subsribers_bar.setObjectName(u"hl_subsribers_bar")
        self.pb_subsribers_filter = QToolButton(LibArchiveWindow)
        self.pb_subsribers_filter.setObjectName(u"pb_subsribers_filter")
        sizePolicy.setHeightForWidth(self.pb_subsribers_filter.sizePolicy().hasHeightForWidth())
        self.pb_subsribers_filter.setSizePolicy(sizePolicy)
        self.pb_subsribers_filter.setMinimumSize(QSize(26, 26))
        self.pb_subsribers_filter.setMaximumSize(QSize(26, 26))
        self.pb_subsribers_filter.setIcon(icon)
        self.pb_subsribers_filter.setIconSize(QSize(14, 14))

        self.hl_subsribers_bar.addWidget(self.pb_subsribers_filter)

        self.l_subsribers = QLabel(LibArchiveWindow)
        self.l_subsribers.setObjectName(u"l_subsribers")
        self.l_subsribers.setMaximumSize(QSize(16777211, 16777215))
        self.l_subsribers.setFont(font)

        self.hl_subsribers_bar.addWidget(self.l_subsribers)

        self.pb_subsribers_add = QToolButton(LibArchiveWindow)
        self.pb_subsribers_add.setObjectName(u"pb_subsribers_add")
        sizePolicy.setHeightForWidth(self.pb_subsribers_add.sizePolicy().hasHeightForWidth())
        self.pb_subsribers_add.setSizePolicy(sizePolicy)
        self.pb_subsribers_add.setMinimumSize(QSize(26, 26))
        self.pb_subsribers_add.setMaximumSize(QSize(26, 26))
        self.pb_subsribers_add.setIcon(icon1)
        self.pb_subsribers_add.setIconSize(QSize(14, 14))

        self.hl_subsribers_bar.addWidget(self.pb_subsribers_add)

        self.pb_subscribers_remove = QToolButton(LibArchiveWindow)
        self.pb_subscribers_remove.setObjectName(u"pb_subscribers_remove")
        sizePolicy.setHeightForWidth(self.pb_subscribers_remove.sizePolicy().hasHeightForWidth())
        self.pb_subscribers_remove.setSizePolicy(sizePolicy)
        self.pb_subscribers_remove.setMinimumSize(QSize(26, 26))
        self.pb_subscribers_remove.setMaximumSize(QSize(26, 26))
        self.pb_subscribers_remove.setIcon(icon2)
        self.pb_subscribers_remove.setIconSize(QSize(14, 14))

        self.hl_subsribers_bar.addWidget(self.pb_subscribers_remove)

        self.pb_subscribers_edit = QToolButton(LibArchiveWindow)
        self.pb_subscribers_edit.setObjectName(u"pb_subscribers_edit")
        sizePolicy.setHeightForWidth(self.pb_subscribers_edit.sizePolicy().hasHeightForWidth())
        self.pb_subscribers_edit.setSizePolicy(sizePolicy)
        self.pb_subscribers_edit.setMinimumSize(QSize(26, 26))
        self.pb_subscribers_edit.setMaximumSize(QSize(26, 26))
        self.pb_subscribers_edit.setIcon(icon3)
        self.pb_subscribers_edit.setIconSize(QSize(14, 14))

        self.hl_subsribers_bar.addWidget(self.pb_subscribers_edit)


        self.gl_main.addLayout(self.hl_subsribers_bar, 5, 0, 1, 1)


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
        ___qtablewidgetitem = self.tw_books.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LibArchiveWindow", u"#", None));
        ___qtablewidgetitem1 = self.tw_books.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tw_books.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0410\u0432\u0442\u043e\u0440", None));
        ___qtablewidgetitem3 = self.tw_books.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0418\u0437\u0434\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem4 = self.tw_books.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f", None));
        ___qtablewidgetitem5 = self.tw_books.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0416\u0430\u043d\u0440\u044b", None));
        ___qtablewidgetitem6 = self.tw_subscribers.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("LibArchiveWindow", u"#", None));
        ___qtablewidgetitem7 = self.tw_subscribers.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem8 = self.tw_subscribers.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None));
        ___qtablewidgetitem9 = self.tw_subscribers.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d", None));
        ___qtablewidgetitem10 = self.tw_subscribers.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b", None));
        ___qtablewidgetitem11 = self.tw_borrowers.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("LibArchiveWindow", u"#", None));
        ___qtablewidgetitem12 = self.tw_borrowers.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a", None));
        ___qtablewidgetitem13 = self.tw_borrowers.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041a\u043d\u0438\u0433\u0430", None));
        ___qtablewidgetitem14 = self.tw_borrowers.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem15 = self.tw_borrowers.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041e\u0436\u0438\u0434\u0430\u0435\u0442\u0441\u044f", None));
        self.pb_borrow_a_book.setText(QCoreApplication.translate("LibArchiveWindow", u"\u041e\u0434\u043e\u043b\u0436\u0438\u0442\u044c \u043a\u043d\u0438\u0433\u0443", None))
        self.pb_return_a_book.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c \u043a\u043d\u0438\u0433\u0443", None))
        self.pb_marked_lost.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c \u0443\u0442\u0435\u0440\u044f\u043d\u043d\u043e\u0439", None))
        self.pb_lost_books.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0423\u0442\u0435\u0440\u044f\u043d\u043d\u044b\u0435 \u043a\u043d\u0438\u0433\u0438", None))
#if QT_CONFIG(tooltip)
        self.pb_borrowers_filter.setToolTip(QCoreApplication.translate("LibArchiveWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u0434\u043e\u043b\u0436\u043d\u0438\u043a\u043e\u0432", None))
#endif // QT_CONFIG(tooltip)
        self.pb_borrowers_filter.setText("")
        self.l_borrowers.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0414\u043e\u043b\u0436\u043d\u0438\u043a\u0438", None))
        self.pb_borrowing_history.setText(QCoreApplication.translate("LibArchiveWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
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

