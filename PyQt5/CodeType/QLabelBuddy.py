#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/13 19:29
# @File     : QLabelBuddy.py
# @Project  : CalendarModule.py
# @Desc     :
"""
QLabel与伙伴控件

mainLayout.addWidget(控件对象, rowIndex, columnIndex, row, column)
"""
import sys
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication


class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel Buddy")
        nameLabel = QLabel("&Name", self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel("&Password", self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        button_ok = QPushButton("&OK")
        button_cancel = QPushButton("&Cancel")

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(button_ok, 2, 1)
        mainLayout.addWidget(button_cancel, 2, 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())