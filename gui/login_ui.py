# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(736, 521)
        icon = QIcon()
        icon.addFile(u"../icon/icons8-write-60.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"#login_user:hover , #login_pwd:hover , #btn_submit:hover , #btn_cancel:hover{\n"
"border-radius:5px;\n"
"background-color:gray;\n"
"color:white;\n"
"}\n"
"\n"
"#login_user , #login_pwd , #btn_submit , #btn_cancel{\n"
"border-radius:5px;\n"
"background-color:#cccccc;\n"
"padding:5px 5px;\n"
"}\n"
"\n"
"#label_2{\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"background-color:white;\n"
"}\n"
"#label{\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"background-color:#cccccc;\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 291, 481))
        font = QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 30, 421, 481))
        self.login_user = QLineEdit(Form)
        self.login_user.setObjectName(u"login_user")
        self.login_user.setGeometry(QRect(360, 120, 281, 31))
        self.login_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_pwd = QLineEdit(Form)
        self.login_pwd.setObjectName(u"login_pwd")
        self.login_pwd.setGeometry(QRect(360, 160, 281, 31))
        self.login_pwd.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_pwd.setEchoMode(QLineEdit.Password)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(390, 210, 228, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_submit = QPushButton(self.horizontalLayoutWidget)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../icon/bullet-list2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_submit.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_submit)

        self.btn_cancel = QPushButton(self.horizontalLayoutWidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../icon/icons8-close-window-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.login_msg = QLabel(Form)
        self.login_msg.setObjectName(u"login_msg")
        self.login_msg.setGeometry(QRect(360, 300, 301, 91))
        self.login_msg.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 180, 171, 41))
        font1 = QFont()
        font1.setPointSize(24)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 201, 41))
        font2 = QFont()
        font2.setPointSize(36)
        self.label_4.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6839\u57fa\u71df\u9020", None))
#if QT_CONFIG(tooltip)
        Form.setToolTip(QCoreApplication.translate("Form", u"\u6839\u57fa\u71df\u9020\u611f\u6e2c\u5668\u76e3\u63a7", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText("")
        self.label_2.setText("")
        self.login_user.setPlaceholderText(QCoreApplication.translate("Form", u"\u5e33\u865f", None))
        self.login_pwd.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u78bc", None))
        self.btn_submit.setText(QCoreApplication.translate("Form", u"\u767b\u5165", None))
        self.btn_cancel.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
        self.login_msg.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u611f\u6e2c\u5668\u76e3\u63a7", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6839\u57fa\u71df\u9020", None))
    # retranslateUi

