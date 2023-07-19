# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"../icon/icons8-write-60.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#b_account_date:hover , #b_account_date2:hover , #account_user:hover , #account_pwd:hover , #account_lv:hover , #account_lv2:hover , #account_position:hover , #account_position2:hover , #account_comment:hover{\n"
"border-radius:5px;\n"
"background-color:#cccccc;\n"
"padding:5px 5px;\n"
"}\n"
"\n"
"#b_account_date , #b_account_date2 , #account_user , #account_pwd , #account_lv , #account_lv2 , #account_position , #account_position2 , #account_comment{\n"
"border-radius:5px;\n"
"border-color:#cccccc;\n"
"padding:5px 5px;\n"
"}\n"
"\n"
"\n"
"#btn_account_add:hover , #btn_account_alter:hover , #btn_account_cancel:hover , #btn_account_del:hover{\n"
"border-radius:5px;\n"
"background-color:gray;\n"
"color:white;\n"
"}\n"
"\n"
"#btn_account_add , #btn_account_alter , #btn_account_cancel , #btn_account_del{\n"
"border-radius:5px;\n"
"background-color:#cccccc;\n"
"padding:5px 5px;\n"
"}")
        self.action_account = QAction(MainWindow)
        self.action_account.setObjectName(u"action_account")
        icon1 = QIcon()
        icon1.addFile(u"../icon/bullet-list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_account.setIcon(icon1)
        self.action_logout = QAction(MainWindow)
        self.action_logout.setObjectName(u"action_logout")
        icon2 = QIcon()
        icon2.addFile(u"../icon/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_logout.setIcon(icon2)
        self.action_sensor = QAction(MainWindow)
        self.action_sensor.setObjectName(u"action_sensor")
        icon3 = QIcon()
        icon3.addFile(u"../icon/icons8-backup-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_sensor.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_account = QWidget()
        self.page_account.setObjectName(u"page_account")
        self.gridLayout_2 = QGridLayout(self.page_account)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.page_account)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.b_account_date = QLineEdit(self.groupBox)
        self.b_account_date.setObjectName(u"b_account_date")
        self.b_account_date.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.b_account_date)

        self.b_account_date2 = QDateEdit(self.groupBox)
        self.b_account_date2.setObjectName(u"b_account_date2")
        self.b_account_date2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.b_account_date2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.account_user = QLineEdit(self.groupBox)
        self.account_user.setObjectName(u"account_user")
        self.account_user.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.account_user)

        self.account_pwd = QLineEdit(self.groupBox)
        self.account_pwd.setObjectName(u"account_pwd")
        self.account_pwd.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.account_pwd)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.account_position = QLineEdit(self.groupBox)
        self.account_position.setObjectName(u"account_position")
        self.account_position.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.account_position)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.account_position2 = QComboBox(self.groupBox)
        self.account_position2.setObjectName(u"account_position2")
        self.account_position2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.account_position2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.account_lv = QLineEdit(self.groupBox)
        self.account_lv.setObjectName(u"account_lv")
        self.account_lv.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.account_lv)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.account_lv2 = QComboBox(self.groupBox)
        self.account_lv2.setObjectName(u"account_lv2")
        self.account_lv2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.account_lv2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.account_comment = QTextEdit(self.groupBox)
        self.account_comment.setObjectName(u"account_comment")
        self.account_comment.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.account_comment)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_account_add = QPushButton(self.groupBox)
        self.btn_account_add.setObjectName(u"btn_account_add")
        self.btn_account_add.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_account_add)

        self.btn_account_cancel = QPushButton(self.groupBox)
        self.btn_account_cancel.setObjectName(u"btn_account_cancel")
        self.btn_account_cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_account_cancel)

        self.btn_account_alter = QPushButton(self.groupBox)
        self.btn_account_alter.setObjectName(u"btn_account_alter")
        self.btn_account_alter.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_account_alter)

        self.btn_account_del = QPushButton(self.groupBox)
        self.btn_account_del.setObjectName(u"btn_account_del")
        self.btn_account_del.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_account_del)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.page_account)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.account_list = QTreeWidget(self.groupBox_4)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.account_list.setHeaderItem(__qtreewidgetitem)
        self.account_list.setObjectName(u"account_list")

        self.verticalLayout.addWidget(self.account_list)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.account_list2 = QTreeWidget(self.groupBox_4)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.account_list2.setHeaderItem(__qtreewidgetitem1)
        self.account_list2.setObjectName(u"account_list2")

        self.verticalLayout.addWidget(self.account_list2)


        self.gridLayout_2.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_account)
        self.page_sensor = QWidget()
        self.page_sensor.setObjectName(u"page_sensor")
        self.verticalLayout_4 = QVBoxLayout(self.page_sensor)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.page_sensor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.kedge_cb_list_11 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.kedge_cb_list_11.setHeaderItem(__qtreewidgetitem2)
        self.kedge_cb_list_11.setObjectName(u"kedge_cb_list_11")

        self.gridLayout_3.addWidget(self.kedge_cb_list_11, 3, 1, 1, 1)

        self.kedge_cb_list_7 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, u"1");
        self.kedge_cb_list_7.setHeaderItem(__qtreewidgetitem3)
        self.kedge_cb_list_7.setObjectName(u"kedge_cb_list_7")

        self.gridLayout_3.addWidget(self.kedge_cb_list_7, 2, 0, 1, 1)

        self.kedge_cb_list_3 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setText(0, u"1");
        self.kedge_cb_list_3.setHeaderItem(__qtreewidgetitem4)
        self.kedge_cb_list_3.setObjectName(u"kedge_cb_list_3")

        self.gridLayout_3.addWidget(self.kedge_cb_list_3, 0, 2, 1, 1)

        self.kedge_cb_list_8 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem5 = QTreeWidgetItem()
        __qtreewidgetitem5.setText(0, u"1");
        self.kedge_cb_list_8.setHeaderItem(__qtreewidgetitem5)
        self.kedge_cb_list_8.setObjectName(u"kedge_cb_list_8")

        self.gridLayout_3.addWidget(self.kedge_cb_list_8, 2, 1, 1, 1)

        self.kedge_cb_list_10 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem6 = QTreeWidgetItem()
        __qtreewidgetitem6.setText(0, u"1");
        self.kedge_cb_list_10.setHeaderItem(__qtreewidgetitem6)
        self.kedge_cb_list_10.setObjectName(u"kedge_cb_list_10")

        self.gridLayout_3.addWidget(self.kedge_cb_list_10, 3, 0, 1, 1)

        self.kedge_cb_list_2 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem7 = QTreeWidgetItem()
        __qtreewidgetitem7.setText(0, u"1");
        self.kedge_cb_list_2.setHeaderItem(__qtreewidgetitem7)
        self.kedge_cb_list_2.setObjectName(u"kedge_cb_list_2")

        self.gridLayout_3.addWidget(self.kedge_cb_list_2, 0, 1, 1, 1)

        self.kedge_cb_list_6 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem8 = QTreeWidgetItem()
        __qtreewidgetitem8.setText(0, u"1");
        self.kedge_cb_list_6.setHeaderItem(__qtreewidgetitem8)
        self.kedge_cb_list_6.setObjectName(u"kedge_cb_list_6")

        self.gridLayout_3.addWidget(self.kedge_cb_list_6, 1, 2, 1, 1)

        self.kedge_cb_list_5 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem9 = QTreeWidgetItem()
        __qtreewidgetitem9.setText(0, u"1");
        self.kedge_cb_list_5.setHeaderItem(__qtreewidgetitem9)
        self.kedge_cb_list_5.setObjectName(u"kedge_cb_list_5")

        self.gridLayout_3.addWidget(self.kedge_cb_list_5, 1, 1, 1, 1)

        self.kedge_cb_list_1 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem10 = QTreeWidgetItem()
        __qtreewidgetitem10.setText(0, u"1");
        self.kedge_cb_list_1.setHeaderItem(__qtreewidgetitem10)
        self.kedge_cb_list_1.setObjectName(u"kedge_cb_list_1")

        self.gridLayout_3.addWidget(self.kedge_cb_list_1, 0, 0, 1, 1)

        self.kedge_cb_list_12 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem11 = QTreeWidgetItem()
        __qtreewidgetitem11.setText(0, u"1");
        self.kedge_cb_list_12.setHeaderItem(__qtreewidgetitem11)
        self.kedge_cb_list_12.setObjectName(u"kedge_cb_list_12")

        self.gridLayout_3.addWidget(self.kedge_cb_list_12, 3, 2, 1, 1)

        self.kedge_cb_list_4 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem12 = QTreeWidgetItem()
        __qtreewidgetitem12.setText(0, u"1");
        self.kedge_cb_list_4.setHeaderItem(__qtreewidgetitem12)
        self.kedge_cb_list_4.setObjectName(u"kedge_cb_list_4")

        self.gridLayout_3.addWidget(self.kedge_cb_list_4, 1, 0, 1, 1)

        self.kedge_cb_list_9 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem13 = QTreeWidgetItem()
        __qtreewidgetitem13.setText(0, u"1");
        self.kedge_cb_list_9.setHeaderItem(__qtreewidgetitem13)
        self.kedge_cb_list_9.setObjectName(u"kedge_cb_list_9")

        self.gridLayout_3.addWidget(self.kedge_cb_list_9, 2, 2, 1, 1)

        self.kedge_cb_list_13 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem14 = QTreeWidgetItem()
        __qtreewidgetitem14.setText(0, u"1");
        self.kedge_cb_list_13.setHeaderItem(__qtreewidgetitem14)
        self.kedge_cb_list_13.setObjectName(u"kedge_cb_list_13")

        self.gridLayout_3.addWidget(self.kedge_cb_list_13, 4, 0, 1, 1)

        self.kedge_cb_list_14 = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem15 = QTreeWidgetItem()
        __qtreewidgetitem15.setText(0, u"1");
        self.kedge_cb_list_14.setHeaderItem(__qtreewidgetitem15)
        self.kedge_cb_list_14.setObjectName(u"kedge_cb_list_14")

        self.gridLayout_3.addWidget(self.kedge_cb_list_14, 4, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.page_sensor)
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.verticalLayout_3 = QVBoxLayout(self.page_welcome)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page_welcome)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_welcome)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_account)
        self.menu.addSeparator()
        self.menu.addAction(self.action_logout)
        self.menu_2.addAction(self.action_sensor)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6839\u57fa\u71df\u9020", None))
        self.action_account.setText(QCoreApplication.translate("MainWindow", u"\u5e33\u865f\u7ba1\u7406", None))
#if QT_CONFIG(tooltip)
        self.action_account.setToolTip(QCoreApplication.translate("MainWindow", u"\u5e33\u865f\u7ba1\u7406", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_account.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_logout.setText(QCoreApplication.translate("MainWindow", u"\u767b\u51fa", None))
#if QT_CONFIG(tooltip)
        self.action_logout.setToolTip(QCoreApplication.translate("MainWindow", u"\u767b\u51fa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_logout.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_sensor.setText(QCoreApplication.translate("MainWindow", u"\u611f\u6e2c\u5668\u9ede\u4f4d", None))
#if QT_CONFIG(tooltip)
        self.action_sensor.setToolTip(QCoreApplication.translate("MainWindow", u"\u611f\u6e2c\u5668\u9ede\u4f4d", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_sensor.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5e33\u865f\u7ba1\u7406", None))
        self.b_account_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6642\u9593", None))
        self.account_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5e33\u865f", None))
        self.account_pwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u78bc", None))
        self.account_position.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None))
        self.account_lv.setText("")
        self.account_lv.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7b49\u7d1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u7d1a", None))
        self.account_comment.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5099\u8a3b", None))
        self.btn_account_add.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e", None))
        self.btn_account_cancel.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.btn_account_alter.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.btn_account_del.setText(QCoreApplication.translate("MainWindow", u"\u522a\u9664", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e33\u865f\u6e05\u55ae", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u5e33\u865f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u822c\u5e33\u865f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u611f\u6e2c\u5668\u9ede\u4f4d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6839\u57fa\u71df\u9020 \u611f\u6e2c\u5668\u76e3\u63a7", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e33\u865f", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u611f\u6e2c\u5668\u76e3\u63a7", None))
    # retranslateUi

