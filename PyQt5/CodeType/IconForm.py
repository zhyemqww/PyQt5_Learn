#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/13 15:32
# @File     : IconForm.py
# @Project  : CalendarModule.py
# @Desc     :
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口位置和大小
        self.setGeometry(300, 300, 250, 250)
        # 设置窗口标题
        self.setWindowTitle("Icon")
        # 设置窗口图标
        self.setWindowIcon(QIcon("C:\\Users\\zhyemqww\\Pictures\\Camera Roll\\python.png"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("C:\\Users\\zhyemqww\\Pictures\\Camera Roll\\python.png"))
    main = IconForm()
    main.show()
    sys.exit(app.exec_())