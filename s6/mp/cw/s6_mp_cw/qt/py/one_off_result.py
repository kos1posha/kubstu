# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_off_result.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_OneOffResultDialog(object):
    def setupUi(self, OneOffResultDialog):
        if not OneOffResultDialog.objectName():
            OneOffResultDialog.setObjectName(u"OneOffResultDialog")
        OneOffResultDialog.resize(250, 300)
        OneOffResultDialog.setMinimumSize(QSize(250, 300))
        OneOffResultDialog.setMaximumSize(QSize(250, 300))
        self.gridLayout = QGridLayout(OneOffResultDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_remains_building = QLabel(OneOffResultDialog)
        self.l_remains_building.setObjectName(u"l_remains_building")

        self.gridLayout.addWidget(self.l_remains_building, 8, 0, 1, 1)

        self.l_remains_painting_value = QLabel(OneOffResultDialog)
        self.l_remains_painting_value.setObjectName(u"l_remains_painting_value")
        self.l_remains_painting_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.l_remains_painting_value, 12, 1, 1, 1)

        self.l_remains_blank = QLabel(OneOffResultDialog)
        self.l_remains_blank.setObjectName(u"l_remains_blank")

        self.gridLayout.addWidget(self.l_remains_blank, 7, 0, 1, 1)

        self.l_remains_blank_value = QLabel(OneOffResultDialog)
        self.l_remains_blank_value.setObjectName(u"l_remains_blank_value")
        self.l_remains_blank_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.l_remains_blank_value, 7, 1, 1, 1)

        self.l_remains_painting = QLabel(OneOffResultDialog)
        self.l_remains_painting.setObjectName(u"l_remains_painting")

        self.gridLayout.addWidget(self.l_remains_painting, 12, 0, 1, 1)

        self.l_remains_building_value = QLabel(OneOffResultDialog)
        self.l_remains_building_value.setObjectName(u"l_remains_building_value")
        self.l_remains_building_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.l_remains_building_value, 8, 1, 1, 1)

        self.tw_plan = QTableWidget(OneOffResultDialog)
        if (self.tw_plan.columnCount() < 4):
            self.tw_plan.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tw_plan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tw_plan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tw_plan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tw_plan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tw_plan.rowCount() < 1):
            self.tw_plan.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_plan.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFlags(Qt.ItemIsEnabled);
        self.tw_plan.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFlags(Qt.ItemIsEnabled);
        self.tw_plan.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFlags(Qt.ItemIsEnabled);
        self.tw_plan.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFlags(Qt.ItemIsEnabled);
        self.tw_plan.setItem(0, 3, __qtablewidgetitem8)
        self.tw_plan.setObjectName(u"tw_plan")
        self.tw_plan.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tw_plan, 5, 0, 1, 2)

        self.l_remains = QLabel(OneOffResultDialog)
        self.l_remains.setObjectName(u"l_remains")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.l_remains.setFont(font)

        self.gridLayout.addWidget(self.l_remains, 6, 0, 1, 2)

        self.l_plan = QLabel(OneOffResultDialog)
        self.l_plan.setObjectName(u"l_plan")
        self.l_plan.setFont(font)

        self.gridLayout.addWidget(self.l_plan, 4, 0, 1, 2)

        self.l_stonks_value = QLabel(OneOffResultDialog)
        self.l_stonks_value.setObjectName(u"l_stonks_value")
        font1 = QFont()
        font1.setPointSize(14)
        self.l_stonks_value.setFont(font1)

        self.gridLayout.addWidget(self.l_stonks_value, 3, 0, 1, 2)

        self.l_stonks = QLabel(OneOffResultDialog)
        self.l_stonks.setObjectName(u"l_stonks")
        self.l_stonks.setFont(font)

        self.gridLayout.addWidget(self.l_stonks, 2, 0, 1, 2)

        self.le_supply = QLineEdit(OneOffResultDialog)
        self.le_supply.setObjectName(u"le_supply")
        self.le_supply.setReadOnly(True)

        self.gridLayout.addWidget(self.le_supply, 1, 0, 1, 2)

        self.l_supply = QLabel(OneOffResultDialog)
        self.l_supply.setObjectName(u"l_supply")
        self.l_supply.setFont(font)

        self.gridLayout.addWidget(self.l_supply, 0, 0, 1, 2)


        self.retranslateUi(OneOffResultDialog)

        QMetaObject.connectSlotsByName(OneOffResultDialog)
    # setupUi

    def retranslateUi(self, OneOffResultDialog):
        OneOffResultDialog.setWindowTitle(QCoreApplication.translate("OneOffResultDialog", u"\u041f\u043b\u0430\u043d \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430", None))
        self.l_remains_building.setText(QCoreApplication.translate("OneOffResultDialog", u"\u0421\u043e \u0441\u0431\u043e\u0440\u043a\u0438 \u0441\u0442\u043e\u043b\u043e\u0432", None))
        self.l_remains_painting_value.setText(QCoreApplication.translate("OneOffResultDialog", u"0", None))
        self.l_remains_blank.setText(QCoreApplication.translate("OneOffResultDialog", u"\u0421 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043e\u043a", None))
        self.l_remains_blank_value.setText(QCoreApplication.translate("OneOffResultDialog", u"0", None))
        self.l_remains_painting.setText(QCoreApplication.translate("OneOffResultDialog", u"\u0421 \u043f\u043e\u043a\u0440\u0430\u0441\u043a\u0438", None))
        self.l_remains_building_value.setText(QCoreApplication.translate("OneOffResultDialog", u"0", None))
        ___qtablewidgetitem = self.tw_plan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("OneOffResultDialog", u"\u0410", None));
        ___qtablewidgetitem1 = self.tw_plan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("OneOffResultDialog", u"\u0411", None));
        ___qtablewidgetitem2 = self.tw_plan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("OneOffResultDialog", u"\u0412", None));
        ___qtablewidgetitem3 = self.tw_plan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("OneOffResultDialog", u"\u0412(\u043d)", None));

        __sortingEnabled = self.tw_plan.isSortingEnabled()
        self.tw_plan.setSortingEnabled(False)
        self.tw_plan.setSortingEnabled(__sortingEnabled)

        self.l_remains.setText(QCoreApplication.translate("OneOffResultDialog", u"\u041e\u0441\u0442\u0430\u0442\u043a\u0438", None))
        self.l_plan.setText(QCoreApplication.translate("OneOffResultDialog", u"\u041f\u043b\u0430\u043d \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430", None))
        self.l_stonks_value.setText(QCoreApplication.translate("OneOffResultDialog", u"100 \u0442\u044b\u0441. \u0440\u0443\u0431\u043b\u0435\u0439", None))
        self.l_stonks.setText(QCoreApplication.translate("OneOffResultDialog", u"\u041f\u0440\u0435\u043f\u043e\u043b\u0430\u0433\u0430\u0435\u043c\u0430\u044f \u043f\u0440\u0438\u0431\u044b\u043b\u044c", None))
        self.l_supply.setText(QCoreApplication.translate("OneOffResultDialog", u"\u0417\u0430\u043f\u0430\u0441\u044b \u0447\u0435\u043b/\u0434\u043d\u0435\u0439", None))
    # retranslateUi

