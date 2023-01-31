# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLayout, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(606, 534)
        self.actionprint_1 = QAction(MainWindow)
        self.actionprint_1.setObjectName(u"actionprint_1")
        self.actionprint_1.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(16777215, 200))
        self.tab_api = QWidget()
        self.tab_api.setObjectName(u"tab_api")
        self.horizontalLayout = QHBoxLayout(self.tab_api)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.pushButton_7 = QPushButton(self.tab_api)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.tab_api)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.tab_api)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.tab_api)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.tab_api)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.tab_api)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.tab_api)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.tab_api)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.tab_api)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_1 = QPushButton(self.tab_api)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.tab_api)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.tab_api)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab_api, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.tab_3)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.plainTextEdit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionprint_1.setText(QCoreApplication.translate("MainWindow", u"print(\"1\")", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_api), QCoreApplication.translate("MainWindow", u"API", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column3", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"111", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"112", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"113", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"221", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"222", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"223", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"331", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"332", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"333", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

