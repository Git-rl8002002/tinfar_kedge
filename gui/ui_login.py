# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(736, 521)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/icons8-write-60.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#login_user:hover , #login_pwd:hover , #btn_submit:hover , #btn_cancel:hover{\n"
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 291, 481))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 30, 421, 481))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.login_user = QtWidgets.QLineEdit(Form)
        self.login_user.setGeometry(QtCore.QRect(360, 120, 281, 31))
        self.login_user.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_user.setObjectName("login_user")
        self.login_pwd = QtWidgets.QLineEdit(Form)
        self.login_pwd.setGeometry(QtCore.QRect(360, 160, 281, 31))
        self.login_pwd.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_pwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.login_pwd.setObjectName("login_pwd")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 210, 228, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_submit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_submit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/bullet-list2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_submit.setIcon(icon1)
        self.btn_submit.setObjectName("btn_submit")
        self.horizontalLayout.addWidget(self.btn_submit)
        self.btn_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/icons8-close-window-94.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.login_msg = QtWidgets.QLabel(Form)
        self.login_msg.setGeometry(QtCore.QRect(360, 300, 301, 91))
        self.login_msg.setText("")
        self.login_msg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.login_msg.setObjectName("login_msg")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 180, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "根基營造"))
        Form.setToolTip(_translate("Form", "根基營造感測器監控"))
        self.login_user.setPlaceholderText(_translate("Form", "帳號"))
        self.login_pwd.setPlaceholderText(_translate("Form", "密碼"))
        self.btn_submit.setText(_translate("Form", "登入"))
        self.btn_cancel.setText(_translate("Form", "取消"))
        self.label_3.setText(_translate("Form", "感測器監控"))
        self.label_4.setText(_translate("Form", "根基營造"))
