#define WIN32_LEAN_AND_MEAN
#include <iostream>
#include <fstream>
#include <windows.h>
#include <string>

int main() {
    std::ifstream inputFile("config.txt"); // 打开名为config.txt的文件
    int width, height;

    if (inputFile.is_open()) {
        inputFile >> width;  // 读取第一个整数作为宽度
        inputFile >> height;  // 读取第二个整数作为高度
        inputFile.close();    // 关闭文件

        DEVMODE devMode;
        memset(&devMode, 0, sizeof(devMode));
        devMode.dmSize = sizeof(devMode);

        devMode.dmPelsWidth = width;    // 设置宽度
        devMode.dmPelsHeight = height;  // 设置高度
        devMode.dmFields = DM_PELSWIDTH | DM_PELSHEIGHT;

        // 修改分辨率
        if (ChangeDisplaySettings(&devMode, CDS_UPDATEREGISTRY) != DISP_CHANGE_SUCCESSFUL) {
            std::cerr << "Failed to change display settings" << std::endl;
            return 1;
        }

        std::cout << "Display settings changed successfully" << std::endl;
    }
    else {
        std::cerr << "无法打开文件" << std::endl;
    }

    return 0;
}