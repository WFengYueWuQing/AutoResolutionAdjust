import sys
import subprocess
import threading
import time
import ctypes
import winshell
import os
from winotify import Notification, audio

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
# from untitled import Ui_Form  # 导入生成的py文件中的Ui类
# from select import Ui_Yes_button as Ui_Form_2
from function import *
from settings import Ui_settings_widget


# from set_resolution import Ui_set_resolution
# from try_widget import Ui_try_widget


##### 调用的窗口类集合
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 331)
        self.top_label = QtWidgets.QLabel(Form)
        self.top_label.setGeometry(QtCore.QRect(190, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.top_label.setFont(font)
        self.top_label.setObjectName("top_label")
        self.bind_game_button = QtWidgets.QPushButton(Form)
        self.bind_game_button.setGeometry(QtCore.QRect(20, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.bind_game_button.setFont(font)
        self.bind_game_button.setObjectName("bind_game_button")
        self.set_resolution_button = QtWidgets.QPushButton(Form)
        self.set_resolution_button.setGeometry(QtCore.QRect(200, 40, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.set_resolution_button.setFont(font)
        self.set_resolution_button.setObjectName("set_resolution_button")
        self.test_button = QtWidgets.QPushButton(Form)
        self.test_button.setGeometry(QtCore.QRect(410, 40, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.test_button.setFont(font)
        self.test_button.setObjectName("test_button")
        self.settings_button = QtWidgets.QPushButton(Form)
        self.settings_button.setGeometry(QtCore.QRect(230, 100, 141, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.copyright_button = QtWidgets.QLabel(Form)
        self.copyright_button.setGeometry(QtCore.QRect(0, 230, 541, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.copyright_button.setFont(font)
        self.copyright_button.setObjectName("copyright_button")
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(160, 170, 291, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.version_label = QtWidgets.QLabel(Form)
        self.version_label.setGeometry(QtCore.QRect(30, 290, 261, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.top_label.setText(_translate("Form", "   简单性能优化"))
        self.bind_game_button.setText(_translate("Form", "绑定游戏路径"))
        self.set_resolution_button.setText(_translate("Form", "设置指定分辨率"))
        self.test_button.setText(_translate("Form", "可行性测试"))
        self.settings_button.setText(_translate("Form", "配置菜单"))
        self.copyright_button.setText(_translate("Form", "    软件来源:bilibili-w_风月无情,本身免费,无毒"))
        self.start_button.setText(_translate("Form", "开始监听并启动游戏"))
        self.version_label.setText(_translate("Form", "版本:1.0"))


class Ui_Form_2(object):
    def setupUi(self, Yes_button):
        Yes_button.setObjectName("Yes_button")
        Yes_button.resize(576, 237)
        self.input_label = QtWidgets.QLabel(Yes_button)
        self.input_label.setGeometry(QtCore.QRect(30, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_label.setFont(font)
        self.input_label.setObjectName("input_label")
        self.input_edit = QtWidgets.QLineEdit(Yes_button)
        self.input_edit.setGeometry(QtCore.QRect(30, 60, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.input_edit.setFont(font)
        self.input_edit.setObjectName("input_edit")
        self.input_label_2 = QtWidgets.QLabel(Yes_button)
        self.input_label_2.setGeometry(QtCore.QRect(30, 100, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_label_2.setFont(font)
        self.input_label_2.setObjectName("input_label_2")
        self.select_button = QtWidgets.QPushButton(Yes_button)
        self.select_button.setGeometry(QtCore.QRect(30, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_button.setFont(font)
        self.select_button.setObjectName("select_button")
        self.yes_button = QtWidgets.QPushButton(Yes_button)
        self.yes_button.setGeometry(QtCore.QRect(340, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yes_button.setFont(font)
        self.yes_button.setObjectName("yes_button")

        self.retranslateUi(Yes_button)
        QtCore.QMetaObject.connectSlotsByName(Yes_button)

    def retranslateUi(self, Yes_button):
        _translate = QtCore.QCoreApplication.translate
        Yes_button.setWindowTitle(_translate("Yes_button", "Form"))
        self.input_label.setText(_translate("Yes_button", "请输入:"))
        self.input_label_2.setText(_translate("Yes_button", "或者进行路径选择:"))
        self.select_button.setText(_translate("Yes_button", "选择"))
        self.yes_button.setText(_translate("Yes_button", "确定"))


class Ui_set_resolution(object):
    def setupUi(self, set_resolution):
        set_resolution.setObjectName("set_resolution")
        set_resolution.resize(576, 237)
        self.input_label_1 = QtWidgets.QLabel(set_resolution)
        self.input_label_1.setGeometry(QtCore.QRect(30, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_label_1.setFont(font)
        self.input_label_1.setObjectName("input_label_1")
        self.input_edit_1 = QtWidgets.QLineEdit(set_resolution)
        self.input_edit_1.setGeometry(QtCore.QRect(70, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.input_edit_1.setFont(font)
        self.input_edit_1.setObjectName("input_edit_1")
        self.input_label_2 = QtWidgets.QLabel(set_resolution)
        self.input_label_2.setGeometry(QtCore.QRect(20, 50, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_label_2.setFont(font)
        self.input_label_2.setObjectName("input_label_2")
        self.input_label_3 = QtWidgets.QLabel(set_resolution)
        self.input_label_3.setGeometry(QtCore.QRect(260, 50, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_label_3.setFont(font)
        self.input_label_3.setObjectName("input_label_3")
        self.input_edit_2 = QtWidgets.QLineEdit(set_resolution)
        self.input_edit_2.setGeometry(QtCore.QRect(300, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.input_edit_2.setFont(font)
        self.input_edit_2.setObjectName("input_edit_2")
        self.input_label_4 = QtWidgets.QLabel(set_resolution)
        self.input_label_4.setGeometry(QtCore.QRect(240, 150, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_label_4.setFont(font)
        self.input_label_4.setObjectName("input_label_4")
        self.input_edit_3 = QtWidgets.QLineEdit(set_resolution)
        self.input_edit_3.setGeometry(QtCore.QRect(280, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.input_edit_3.setFont(font)
        self.input_edit_3.setText("")
        self.input_edit_3.setObjectName("input_edit_3")
        self.input_label_5 = QtWidgets.QLabel(set_resolution)
        self.input_label_5.setGeometry(QtCore.QRect(10, 150, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_label_5.setFont(font)
        self.input_label_5.setObjectName("input_label_5")
        self.input_edit_4 = QtWidgets.QLineEdit(set_resolution)
        self.input_edit_4.setGeometry(QtCore.QRect(50, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.input_edit_4.setFont(font)
        self.input_edit_4.setText("")
        self.input_edit_4.setObjectName("input_edit_4")
        self.input_label_6 = QtWidgets.QLabel(set_resolution)
        self.input_label_6.setGeometry(QtCore.QRect(30, 100, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_label_6.setFont(font)
        self.input_label_6.setObjectName("input_label_6")
        self.yes_button = QtWidgets.QPushButton(set_resolution)
        self.yes_button.setGeometry(QtCore.QRect(470, 110, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.yes_button.setFont(font)
        self.yes_button.setObjectName("yes_button")

        self.retranslateUi(set_resolution)
        QtCore.QMetaObject.connectSlotsByName(set_resolution)

    def retranslateUi(self, set_resolution):
        _translate = QtCore.QCoreApplication.translate
        set_resolution.setWindowTitle(_translate("set_resolution", "Form"))
        self.input_label_1.setText(_translate("set_resolution", "请输入游戏内分辨率:"))
        self.input_label_2.setText(_translate("set_resolution", "长:"))
        self.input_label_3.setText(_translate("set_resolution", "宽:"))
        self.input_label_4.setText(_translate("set_resolution", "宽:"))
        self.input_label_5.setText(_translate("set_resolution", "长:"))
        self.input_label_6.setText(_translate("set_resolution", "请输入游戏外分辨率:"))
        self.yes_button.setText(_translate("set_resolution", "确定"))


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


#####


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("简单性能优化  By:bilibili-w_风月无情")
        self.ui.bind_game_button.clicked.connect(bind_game_path)
        self.ui.set_resolution_button.clicked.connect(bind_show_set_resolution)
        self.ui.test_button.clicked.connect(bind_show_try_widget)
        self.setFixedSize(580, 331)
        self.ui.start_button.clicked.connect(bind_start_program)
        self.ui.settings_button.clicked.connect(bind_show_settings)


# 读取窗口类
class Path_select(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_2()
        self.ui.setupUi(self)
        self.setWindowTitle("路径输入窗口")
        self.ui.select_button.clicked.connect(select_file_path)
        self.ui.yes_button.clicked.connect(write_resolution)
        self.setFixedSize(576, 237)


# 配置菜单类
class Settings_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_settings_widget()
        self.ui.setupUi(self)
        self.setWindowTitle("配置菜单窗口")
        self.setFixedSize(795, 507)
        self.ui.confirm_button.clicked.connect(bind_confirm_settings)
        # 声音字典
        audio_dict = {"Mail": audio.Mail, "IM": audio.IM, "Reminder": audio.Reminder, "SMS": audio.SMS,
                      "LoopingAlarm": audio.LoopingAlarm, "LoopingAlarm2": audio.LoopingAlarm2,
                      "LoopingAlarm3": audio.LoopingAlarm3, "LoopingAlarm4": audio.LoopingAlarm4,
                      "LoopingAlarm6": audio.LoopingAlarm6,
                      "LoopingAlarm8": audio.LoopingAlarm8
            , "LoopingAlarm9": audio.LoopingAlarm9, "LoopingAlarm10": audio.LoopingAlarm10,
                      "LoopingCall": audio.LoopingCall, "LoopingCall2": audio.LoopingCall2,
                      "LoopingCall3": audio.LoopingCall3, "LoopingCall4": audio.LoopingCall4,
                      "LoopingCall5": audio.LoopingCall5,
                      "LoopingCall6": audio.LoopingCall6, "LoopingCall7": audio.LoopingCall7,
                      "LoopingCall8": audio.LoopingCall8, "LoopingCall9": audio.LoopingCall9,
                      "LoopingCall10": audio.LoopingCall10, "Silent": audio.Silent}
        for key in audio_dict.keys():
            self.ui.select_audio_box.addItem(key)


class Set_reso(QWidget):
    """
    窗口,用于设置分辨率
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_set_resolution()
        self.ui.setupUi(self)
        self.setWindowTitle("分辨率输入窗口")
        self.ui.yes_button.clicked.connect(bind_set_resolution_yes)
        self.setFixedSize(576, 237)


class Try_widget(QWidget):
    """
    窗口,用于可行性测试
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_try_widget()
        self.ui.setupUi(self)
        self.setWindowTitle("可行性测试窗口")
        # self.ui.yes_button.clicked.connect(bind_set_resolution_yes)
        self.ui.change_resolution.clicked.connect(bind_test_resize)
        self.ui.game_start_button.clicked.connect(bind_test_game)
        self.setFixedSize(576, 237)


# 启动程序并获取其PID
def start_program():
    process = subprocess.Popen(glo_var.game_path)
    pid = process.pid
    return process, pid


# win_alarm函数
def win_alarm(title: str, text: str):
    """
    鉴于在某些时候程序内部的提示窗口不方便,特定义了这样的函数来进行系统内部的提示
    :param text: 提示的文本内容
    :param title: 提示的文本标题
    :return:
    """
    # 尝试进行win提示,若失败则使用程序内置的提示
    audio_dict = {"Mail": audio.Mail, "IM": audio.IM, "Reminder": audio.Reminder, "SMS": audio.SMS,
                  "LoopingAlarm": audio.LoopingAlarm, "LoopingAlarm2": audio.LoopingAlarm2,
                  "LoopingAlarm3": audio.LoopingAlarm3, "LoopingAlarm4": audio.LoopingAlarm4,
                  "LoopingAlarm6": audio.LoopingAlarm6,
                  "LoopingAlarm8": audio.LoopingAlarm8
        , "LoopingAlarm9": audio.LoopingAlarm9, "LoopingAlarm10": audio.LoopingAlarm10,
                  "LoopingCall": audio.LoopingCall, "LoopingCall2": audio.LoopingCall2,
                  "LoopingCall3": audio.LoopingCall3, "LoopingCall4": audio.LoopingCall4,
                  "LoopingCall5": audio.LoopingCall5,
                  "LoopingCall6": audio.LoopingCall6, "LoopingCall7": audio.LoopingCall7,
                  "LoopingCall8": audio.LoopingCall8, "LoopingCall9": audio.LoopingCall9,
                  "LoopingCall10": audio.LoopingCall10, "Silent": audio.Silent}
    try:
        toast = Notification(app_id="简单优化程序",
                             title=title,
                             msg=text,
                             icon=os.path.abspath("./图标.ico")
                             )
        toast.set_audio(audio_dict[glo_var.audio_select], loop=False)
        toast.show()
    except Exception as e:
        alarm(f"{text};错误:调用win提示失败{e}")


# 检查程序是否结束，若结束则执行回调函数
def check_program(process, callback_func):
    t1 = glo_var.polling_time  # 轮询时间
    while True:
        if process.poll() is not None:  # 检查程序是否结束
            time.sleep(glo_var.end_time)  # 结束后多久更改分辨率
            callback_func()
            break
        time.sleep(t1)


# 回调函数，更改回原本分辨率,并结束程序
def callback_function():
    global app
    resize(glo_var.end_resolution[0], glo_var.end_resolution[1])
    win_alarm("提示", "更改分辨率完成,欢迎下次使用")
    if glo_var.is_auto_close:
        app.exit(0)


def bind_game_path():
    """
    设置绑定路径
    :return:
    """
    global select_widget  # 获取组件
    # 窗口启动
    select_widget.show()
    # 简化全局变量
    g = glo_var
    # 设置文本框初始内容
    select_widget.ui.input_edit.setText(g.game_path)


def bind_show_set_resolution():
    """
    槽函数,用于显示分辨率设置窗口
    :return:
    """
    global set_resolution_widget  # 获取组件
    # 窗口启动
    g = glo_var  # 简化全局变量
    set_resolution_widget.show()
    # 设置文本框的初始内容
    set_resolution_widget.ui.input_edit_1.setText(str(g.start_resolution[0]))  # 内-长
    set_resolution_widget.ui.input_edit_2.setText(str(g.start_resolution[1]))  # 内-宽
    set_resolution_widget.ui.input_edit_4.setText(str(g.end_resolution[0]))  # 外-长
    set_resolution_widget.ui.input_edit_3.setText(str(g.end_resolution[1]))  # 外-宽


def bind_set_resolution_yes():
    """
    槽函数,用于设置分辨率界面的确定按钮
    :return:
    """
    global set_resolution_widget  # 获取窗口对象
    iLength: str = set_resolution_widget.ui.input_edit_1.text()  # 内分辨率的长
    iWidth: str = set_resolution_widget.ui.input_edit_2.text()  # 内分辨率的宽
    eLength: str = set_resolution_widget.ui.input_edit_4.text()  # 外分辨率的长
    eWidth: str = set_resolution_widget.ui.input_edit_3.text()  # 外分辨率的宽
    if "" in [iLength, iWidth, eLength, eWidth]:
        alarm("错误:请填写所有长与宽")
        return
    try:
        # 对输入类型进行判断, 不怎么高明
        # 设置分辨率并同步到全局变量
        glo_var.start_resolution = [int(iLength), int(iWidth)]
        glo_var.end_resolution = [int(eLength), int(eWidth)]
        glo_var.renew_settings()
        set_resolution_widget.hide()  # 隐藏窗口
        alarm("完成")
        return
    except Exception as e:
        alarm(f"出现错误,请检查输入的分辨率是否有误:{e}")
        return


def is_admin() -> bool:
    """
    用于检测程序是否拥有管理员权限
    :return: 是或否
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def bind_show_try_widget():
    """
    槽函数,用于显示可行性测试窗口
    :return:
    """
    global try_widget
    if glo_var.start_resolution[0] == 0 or glo_var.start_resolution[1] == 0 \
        or glo_var.end_resolution[0] == 0 or glo_var.end_resolution[1] == 0:
        alarm("请先设置好游戏内外分辨率")
        return
    elif glo_var.game_path == "":
        alarm("请先设置好游戏路径")
        return
    try_widget.show()


def bind_show_settings():
    """
    槽函数,用于展示配置菜单窗口
    :return:
    """
    global settings_widget
    settings_widget.show()
    # 简化全局变量与窗口对象
    g = glo_var
    s = settings_widget
    # 设置文本框内容
    s.ui.polling_edit.setText(str(g.polling_time))
    s.ui.time_after_start_edit.setText(str(g.start_time))
    s.ui.time_after_end_edit.setText(str(g.end_time))
    s.ui.check_box_auto_close.setChecked(bool(g.is_auto_close))
    s.ui.check_box_auto_mini.setChecked(bool(g.is_auto_mini))
    s.ui.select_audio_box.setCurrentText(g.audio_select)


def bind_test_resize():
    """
    槽函数,用于测试更改分辨率是否可行
    :return:
    """
    if not glo_var.start_resolution or not glo_var.end_resolution:
        # 检测游戏分辨率是否存在
        alarm("请先设置分辨率")
        return
    alarm("5秒后,进行游戏内分辨率更改,请查看效果(已开始计时)")
    time.sleep(5)
    resize(glo_var.start_resolution[0], glo_var.start_resolution[1])
    win_alarm("提示", "操作已完成")
    time.sleep(3)
    alarm("7秒后,进行游戏外分辨率更改,请查看效果(已开始计时)")
    time.sleep(7)
    resize(glo_var.end_resolution[0], glo_var.end_resolution[1])
    alarm("完成!如果没有任何效果,请尝试给予本程序管理员权限,然后再试一次")
    return


def bind_test_game():
    """
    槽函数,用于测试是否可以启动程序
    :return:
    """
    alarm("5秒后,执行程序,请查看是否有运行")
    try:
        subprocess.run(glo_var.game_path)  # 运行程序
        alarm("完成,请查看程序是否有运行,如无,请给予管理员权限")

    except Exception as e:
        alarm(f"错误:{e},请尝试给予本程序管理员权限,然后重试")

def bind_confirm_settings():
    """
    槽函数,用于确定配置文件
    :return:
    """
    # 简化窗口类以及全局变量
    global settings_widget
    g = glo_var
    s = settings_widget
    # 检查输入是否有效
    try:
        _ = int(s.ui.polling_edit.text() + s.ui.time_after_start_edit.text() + s.ui.time_after_end_edit.text())
    except:
        alarm("请输入正确的数据")
        return
    # 设置变量
    g.polling_time = int(s.ui.polling_edit.text())
    g.start_time = int(s.ui.time_after_start_edit.text())
    g.end_time = int(s.ui.time_after_end_edit.text())
    g.audio_select = s.ui.select_audio_box.currentText()
    g.is_auto_close = s.ui.check_box_auto_close.isChecked()
    g.is_auto_mini = s.ui.check_box_auto_mini.isChecked()
    # 更新
    g.renew_settings()
    # 提示
    win_alarm("提示", "设置成功")
    # 退出窗口并返回
    s.hide()


def select_file_path():
    """
    槽函数,用于调用系统接口来选择路径
    :return:
    """
    file_path, _ = QFileDialog.getOpenFileName(None, "Select File")
    if file_path:
        select_widget.ui.input_edit.setText(file_path)


def alarm(text: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    msg.setWindowTitle("提示")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def write_resolution():
    """
    槽函数,用于把得到的文件路径写入配置菜单
    :return:
    """
    global select_widget
    text = select_widget.ui.input_edit.text()  # 获取输入框文本内容

    # 判断并处理文本
    if "\\" not in text and "/" not in text:
        alarm("请输入正确的路径")
        return
    if text[-1:-4:-1] != "exe":
        alarm("请选择可执行文件(.exe)")
        return

    # 更新全局变量与配置文件
    glo_var.game_path = text
    glo_var.renew_settings()

    # 隐藏窗口
    select_widget.hide()

    # 提示
    alarm("完成")


def bind_start_program():
    """
    槽函数,用于启动游戏,调整分辨率
    :return:
    """
    global t_game, window
    if is_admin():
        pass
    else:
        alarm("请以管理员权限打开程序,否则可能无权限启动游戏")
        return
    # 首先,更改分辨率
    resize(glo_var.start_resolution[0], glo_var.start_resolution[1])
    # 等待数秒后
    win_alarm("提示", "准备启动")
    time.sleep(glo_var.start_time)  # 等待启动
    if glo_var.is_auto_mini:
        window.showMinimized()  # 最小化窗口

    with open("./config.txt", "w", encoding="UTF-8") as f:
        # 打开文件,准备写入参数,用于设置游戏后分辨率
        f.write(f"{glo_var.end_resolution[0]}\n{glo_var.end_resolution[1]}")

    # 启动监听程序
    possess, pid = start_program()  # 启动游戏,获取pid
    t_game = threading.Thread(target=check_program, args=(possess, callback_function))  # 设置线程
    t_game.start()
    win_alarm("提示", "启动成功")


# 主窗口启动
app = QApplication(sys.argv)
window = MyWindow()

# 实例化路径选择组件
select_widget = Path_select()

# 实例化分辨率设置组件
set_resolution_widget = Set_reso()

# 实例化可行性测试设置组件
try_widget = Try_widget()

# 实例化配置菜单组件
settings_widget = Settings_widget()

# 实例化监听线程
t_game = None

window.show()
sys.exit(app.exec_())
