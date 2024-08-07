# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_widget(object):
    def setupUi(self, settings_widget):
        settings_widget.setObjectName("settings_widget")
        settings_widget.resize(795, 507)
        font = QtGui.QFont()
        font.setPointSize(12)
        settings_widget.setFont(font)
        self.confirm_button = QtWidgets.QPushButton(settings_widget)
        self.confirm_button.setGeometry(QtCore.QRect(310, 440, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirm_button.setFont(font)
        self.confirm_button.setObjectName("confirm_button")
        self.label_polling = QtWidgets.QLabel(settings_widget)
        self.label_polling.setGeometry(QtCore.QRect(10, 40, 241, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_polling.setFont(font)
        self.label_polling.setObjectName("label_polling")
        self.polling_edit = QtWidgets.QLineEdit(settings_widget)
        self.polling_edit.setGeometry(QtCore.QRect(270, 50, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.polling_edit.setFont(font)
        self.polling_edit.setObjectName("polling_edit")
        self.label_time_after_start = QtWidgets.QLabel(settings_widget)
        self.label_time_after_start.setGeometry(QtCore.QRect(10, 100, 391, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_time_after_start.setFont(font)
        self.label_time_after_start.setObjectName("label_time_after_start")
        self.time_after_start_edit = QtWidgets.QLineEdit(settings_widget)
        self.time_after_start_edit.setGeometry(QtCore.QRect(410, 120, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.time_after_start_edit.setFont(font)
        self.time_after_start_edit.setObjectName("time_after_start_edit")
        self.label_time_after_end = QtWidgets.QLabel(settings_widget)
        self.label_time_after_end.setGeometry(QtCore.QRect(10, 170, 471, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_time_after_end.setFont(font)
        self.label_time_after_end.setObjectName("label_time_after_end")
        self.time_after_end_edit = QtWidgets.QLineEdit(settings_widget)
        self.time_after_end_edit.setGeometry(QtCore.QRect(410, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.time_after_end_edit.setFont(font)
        self.time_after_end_edit.setObjectName("time_after_end_edit")
        self.label_select_audio = QtWidgets.QLabel(settings_widget)
        self.label_select_audio.setGeometry(QtCore.QRect(10, 230, 391, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_select_audio.setFont(font)
        self.label_select_audio.setObjectName("label_select_audio")
        self.select_audio_box = QtWidgets.QComboBox(settings_widget)
        self.select_audio_box.setGeometry(QtCore.QRect(410, 250, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_audio_box.setFont(font)
        self.select_audio_box.setObjectName("select_audio_box")
        self.pushButton = QtWidgets.QPushButton(settings_widget)
        self.pushButton.setGeometry(QtCore.QRect(660, 300, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.check_box_auto_close = QtWidgets.QCheckBox(settings_widget)
        self.check_box_auto_close.setGeometry(QtCore.QRect(10, 300, 431, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.check_box_auto_close.setFont(font)
        self.check_box_auto_close.setObjectName("check_box_auto_close")
        self.check_box_auto_mini = QtWidgets.QCheckBox(settings_widget)
        self.check_box_auto_mini.setGeometry(QtCore.QRect(10, 360, 461, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.check_box_auto_mini.setFont(font)
        self.check_box_auto_mini.setObjectName("check_box_auto_mini")

        self.retranslateUi(settings_widget)
        QtCore.QMetaObject.connectSlotsByName(settings_widget)

    def retranslateUi(self, settings_widget):
        _translate = QtCore.QCoreApplication.translate
        settings_widget.setWindowTitle(_translate("settings_widget", "Form"))
        self.confirm_button.setText(_translate("settings_widget", "确定"))
        self.label_polling.setText(_translate("settings_widget", "轮询间隔(s):"))
        self.label_time_after_start.setText(_translate("settings_widget", "修改分辨率后多久启动游戏(s):"))
        self.label_time_after_end.setText(_translate("settings_widget", "游戏结束后多久恢复分辨率(s):"))
        self.label_select_audio.setText(_translate("settings_widget", "通知音效选择(仅限右下角通知):"))
        self.pushButton.setText(_translate("settings_widget", "试听"))
        self.check_box_auto_close.setText(_translate("settings_widget", "在恢复分辨率后自动关闭"))
        self.check_box_auto_mini.setText(_translate("settings_widget", "在游戏启动后自动最小化程序"))
