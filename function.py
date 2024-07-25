import subprocess
import os


def resize(screen_length: int, screen_width: int):
    """
    该函数的作用为修改屏幕分辨率
    :param screen_length: 修改后的屏幕长
    :param screen_width: 修改后的屏幕宽
    :return: 无 | 报错信息
    """
    # 判断传入参数合理性
    if screen_length <= screen_width:
        return "长度不该小于宽度"
    if screen_length * screen_width < 0:
        return "长度与宽度不应为负数"

    with open("config.txt", "w", encoding="UTF-8") as f:
        # 打开文件,准备写入参数
        f.write(f"{screen_length}\n{screen_width}")

    # 执行外部程序,修改分辨率
    subprocess.run("./resize.exe")
    return "成功!"


import psutil
import time


def monitor_process_by_path(process_path, start_callback, stop_callback):
    pid = None  # 定义pid
    while pid is None:  # 循环检测程序是否运行
        print("寻找中...")
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            if proc.info['exe'] == process_path:
                # 找到程序后,记下pid,开始监听,并调整窗口大小
                print("")
                pid = proc.info['pid']
                start_callback()
                print("\n捕获成功,正在标记...\n")

    while psutil.pid_exists(pid):
        time.sleep(1)

    stop_callback()  # 执行停止运行时的回调函数


def start():
    """
    开始运行函数
    :return:
    """
    resize(1920, 1200)


def stop():
    """
    结束运行函数
    :return:
    """
    resize(2560, 1600)


class glo_var:
    """
    全局变量类
    1.game_path:游戏路径
    2.start_resolution:游戏内分辨率
    3.end_resolution:游戏外分辨率
    4.polling_time:轮询间隔
    5.start_time:修改分辨率后多久启动游戏
    6.end_time:游戏结束后多久恢复分辨率
    7.audio_select:通知音效选择
    8.is_auto_close:在恢复分辨率后自动关闭
    9.is_auto_mini:在游戏启动后自动最小化程序
    """

    def __init__(self):
        """
        初始化函数
        """
        # 初始化各个成员
        self.game_path = ''
        self.start_resolution = [0, 0]
        self.end_resolution = [0, 0]
        self.polling_time = 2
        self.start_time = 2
        self.end_time = 2
        self.audio_select = "Reminder"
        self.is_auto_close = True
        self.is_auto_mini = True

        # 读取配置信息
        self.get_settings()

    def get_settings(self):
        """
        用于读取配置参数并创建成员
        game_path:str
        start_resolution:int x int (eg.2560x1600)
        end_resolution:int x int
        :return:
        """
        # 检测设置文件是否存在, 不存在则创建文件
        if os.path.exists("./settings.txt"):
            pass
        else:
            with open("./settings.txt", "w", encoding="UTF-8") as f:
                f.write("")
            return

        with open("./settings.txt", "r", encoding="UTF-8") as f:
            lines: list[str] = f.readlines()  # 读取每一行
            if len(lines) >= 1:
                self.game_path = lines[0].strip('\n')  # 设置游戏路径
            if len(lines) >= 2:
                start_resolution_list: list[str] = lines[1].strip('\n').split("x")  # 设置开始分辨率
                self.start_resolution: list[int] = []
                for element in start_resolution_list:
                    self.start_resolution.append(int(element))
            if len(lines) >= 3:
                end_resolution_list: list[str] = lines[2].strip('\n').split("x")  # 设置结束分辨率
                self.end_resolution: list[int] = []
                for element in end_resolution_list:
                    self.end_resolution.append(int(element))
            if len(lines) >= 4:
                self.polling_time: int = int(lines[3].strip('\n'))   # 设置轮询间隔
            if len(lines) >= 5:
                self.start_time: int = int(lines[4].strip('\n'))   # 设置修改分辨率后多久启动游戏
            if len(lines) >= 6:
                self.end_time: int = int(lines[5].strip('\n'))   # 设置游戏结束后多久恢复分辨率
            if len(lines) >= 7:
                self.audio_select: str = lines[6].strip('\n')         # 设置通知音效选择
            if len(lines) >= 8:
                self.is_auto_close: bool = bool(int(lines[7].strip('\n')))         # 设置在恢复分辨率后自动关闭
            if len(lines) >= 9:
                self.is_auto_mini: bool = bool(int(lines[8].strip('\n')))         # 设置在游戏启动后自动最小化程序


    def renew_settings(self):
        """
        更新设置文件,将其写入文件中
        :return:
        """
        with open("./settings.txt", "w", encoding="UTF-8") as f:
            f.write(f"{self.game_path}\n"
                    f"{self.start_resolution[0]}x{self.start_resolution[1]}\n"
                    f"{self.end_resolution[0]}x{self.end_resolution[1]}\n"
                    f"{self.polling_time}\n"
                    f"{self.start_time}\n"
                    f"{self.end_time}\n"
                    f"{self.audio_select}\n"
                    f"{int(self.is_auto_close)}\n"
                    f"{int(self.is_auto_mini)}\n"
                    )


glo_var = glo_var()  # 实例化,以调用同一类

if __name__ == '__main__':
    # 启动监听程序
    process_name_to_monitor = "E:\\System\\Game\\鸣潮\\Wuthering Waves\\launcher.exe"  # 替换为你要监视的程序名称
    monitor_process_by_path(process_name_to_monitor, start, stop)
