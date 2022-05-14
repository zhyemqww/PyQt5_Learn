#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/13 9:57
# @File     : center_form.py
# @Project  : CalendarModule.py
# @Desc     :

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        self.setWindowTitle("窗口居中")

        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage("test")


    # 默认为居中状态
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()

        left = (screen.width() - size.width()) / 2
        top = (screen.width() - size.width()) / 4

        self.move(left, top)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm()
    # main.center()
    main.show()
    sys.exit(app.exec_())
