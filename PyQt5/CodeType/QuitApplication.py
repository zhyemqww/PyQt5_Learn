#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/13 10:33
# @File     : QuitApplication.py
# @Project  : CalendarModule.py
# @Desc     :
"""
通过点击按钮实现退出程序
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon

class QuitApplication(QMainWindow):
    def __init__(self, parent=None):
        super(QuitApplication, self).__init__(parent)

        self.setWindowTitle("退出")

        self.resize(400, 300)

        # 添加button
        self.button = QPushButton("点击退出")
        # 将信号与方法绑定
        self.button.clicked.connect(self.clickButton)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    # 点击按钮触发的方法
    def clickButton(self):
        sender = self.sender()
        print(sender.text())
        # 获取当前实例（当前窗口）
        app = QuitApplication.instance()
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:\\Users\\zhyemqww\\Pictures\\Camera Roll\\python.png"))
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())

