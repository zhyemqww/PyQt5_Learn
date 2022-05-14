#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/13 15:44
# @File     : Tooltip.py
# @Project  : CalendarModule.py
# @Desc     : 显示控件提示信息

import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip("Hello")
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("控件提示信息")

        self.button = QPushButton("Botton")
        self.button.setToolTip("This is a button")
        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())
