# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'browser.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1063, 710)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 1061, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_7 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.gotoURL_b = QPushButton(self.horizontalLayoutWidget_2)
        self.gotoURL_b.setText("Go to URL")
        self.horizontalLayout_2.addWidget(self.gotoURL_b)

        self.newtab_b = QPushButton(self.horizontalLayoutWidget_2)
        self.newtab_b.setText("New Tab")
        self.horizontalLayout_2.addWidget(self.newtab_b)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, 39, 1061, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

       
        #self.webEngineView = QWebEngineView(self.centralwidget)
        #self.webEngineView.setObjectName(u"webEngineView")
        #self.webEngineView.setGeometry(QRect(0, 80, 1071, 631))
        #self.webEngineView.setUrl(QUrl(u"https://www.google.com/"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.lineEdit.setText("")
    # retranslateUi
