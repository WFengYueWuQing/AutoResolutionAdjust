#define WIN32_LEAN_AND_MEAN
#include <iostream>
#include <fstream>
#include <windows.h>
#include <string>

int main() {
    std::ifstream inputFile("config.txt"); // ����Ϊconfig.txt���ļ�
    int width, height;

    if (inputFile.is_open()) {
        inputFile >> width;  // ��ȡ��һ��������Ϊ���
        inputFile >> height;  // ��ȡ�ڶ���������Ϊ�߶�
        inputFile.close();    // �ر��ļ�

        DEVMODE devMode;
        memset(&devMode, 0, sizeof(devMode));
        devMode.dmSize = sizeof(devMode);

        devMode.dmPelsWidth = width;    // ���ÿ��
        devMode.dmPelsHeight = height;  // ���ø߶�
        devMode.dmFields = DM_PELSWIDTH | DM_PELSHEIGHT;

        // �޸ķֱ���
        if (ChangeDisplaySettings(&devMode, CDS_UPDATEREGISTRY) != DISP_CHANGE_SUCCESSFUL) {
            std::cerr << "Failed to change display settings" << std::endl;
            return 1;
        }

        std::cout << "Display settings changed successfully" << std::endl;
    }
    else {
        std::cerr << "�޷����ļ�" << std::endl;
    }

    return 0;
}