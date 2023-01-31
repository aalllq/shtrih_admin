# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lib_api.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(823, 677)
        self.actionprint_1 = QAction(MainWindow)
        self.actionprint_1.setObjectName(u"actionprint_1")
        self.actionprint_1.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_main = QTabWidget(self.centralwidget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        self.tabWidget_main.setIconSize(QSize(5, 5))
        self.tab_all_main = QWidget()
        self.tab_all_main.setObjectName(u"tab_all_main")
        self.verticalLayout_2 = QVBoxLayout(self.tab_all_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ALL_textEdit = QTextEdit(self.tab_all_main)
        self.ALL_textEdit.setObjectName(u"ALL_textEdit")

        self.verticalLayout_2.addWidget(self.ALL_textEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.btn_all_device_info = QPushButton(self.tab_all_main)
        self.btn_all_device_info.setObjectName(u"btn_all_device_info")

        self.gridLayout.addWidget(self.btn_all_device_info, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.tab_all_main)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.tabWidget_main.addTab(self.tab_all_main, "")
        self.tab_fiscalizations_main = QWidget()
        self.tab_fiscalizations_main.setObjectName(u"tab_fiscalizations_main")
        self.tabWidget_main.addTab(self.tab_fiscalizations_main, "")

        self.verticalLayout.addWidget(self.tabWidget_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionprint_1.setText(QCoreApplication.translate("MainWindow", u"print(\"1\")", None))
#if QT_CONFIG(tooltip)
        self.tab_all_main.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>hgjgh</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tab_all_main.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>m,</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_all_device_info.setText(QCoreApplication.translate("MainWindow", u"ALL_device_info", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_all_main), QCoreApplication.translate("MainWindow", u"ALL", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_fiscalizations_main), QCoreApplication.translate("MainWindow", u"Fiscalize", None))
    # retranslateUi

