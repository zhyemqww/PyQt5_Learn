#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/13 9:37
# @File     : first_main_window.py
# @Project  : CalendarModule.py
# @Desc     :
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class FirstMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWindow, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle("First")

        # 设置窗口尺寸
        self.resize(400, 300)

        # 添加状态栏
        self.status = self.statusBar()

        self.status.showMessage("5 seconds", 5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:\\Users\\zhyemqww\\Pictures\\Camera Roll\\python.png"))
    main = FirstMainWindow()
    main.show()

    sys.exit(app.exec_())
