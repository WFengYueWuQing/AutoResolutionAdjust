# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_try_widget(object):
    def setupUi(self, try_widget):
        try_widget.setObjectName("try_widget")
        try_widget.resize(576, 237)
        self.change_resolution = QtWidgets.QPushButton(try_widget)
        self.change_resolution.setGeometry(QtCore.QRect(140, 40, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.change_resolution.setFont(font)
        self.change_resolution.setObjectName("change_resolution")
        self.game_start_button = QtWidgets.QPushButton(try_widget)
        self.game_start_button.setGeometry(QtCore.QRect(140, 140, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.game_start_button.setFont(font)
        self.game_start_button.setObjectName("game_start_button")

        self.retranslateUi(try_widget)
        QtCore.QMetaObject.connectSlotsByName(try_widget)

    def retranslateUi(self, try_widget):
        _translate = QtCore.QCoreApplication.translate
        try_widget.setWindowTitle(_translate("try_widget", "Form"))
        self.change_resolution.setText(_translate("try_widget", "尝试更改分辨率"))
        self.game_start_button.setText(_translate("try_widget", "尝试打开游戏文件"))