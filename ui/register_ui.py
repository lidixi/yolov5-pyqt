# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_img/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 120, 181, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.edit_username = QtWidgets.QLineEdit(self.layoutWidget)
        self.edit_username.setObjectName("edit_username")
        self.horizontalLayout.addWidget(self.edit_username)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(220, 260, 176, 32))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_regiser = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_regiser.setObjectName("pushButton_regiser")
        self.horizontalLayout_3.addWidget(self.pushButton_regiser)
        self.pushButton_cancer = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_cancer.setObjectName("pushButton_cancer")
        self.horizontalLayout_3.addWidget(self.pushButton_cancer)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 71, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ui_img/small_log.jpg"))
        self.label_4.setObjectName("label_4")
        self.layoutWidget_3 = QtWidgets.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(120, 170, 181, 24))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.edit_password = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.edit_password.setObjectName("edit_password")
        self.horizontalLayout_2.addWidget(self.edit_password)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Account Register"))
        self.label.setText(_translate("Form", "Account Register"))
        self.label_2.setText(_translate("Form", "Username"))
        self.pushButton_regiser.setText(_translate("Form", "Register"))
        self.pushButton_cancer.setText(_translate("Form", "Cancel"))
        self.label_3.setText(_translate("Form", "Password"))
