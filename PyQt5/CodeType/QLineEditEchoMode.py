#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/13 19:49
# @File     : QLineEditEchoMode.py
# @Project  : CalendarModule.py
# @Desc     :
"""
QLineEdit控件与回显模式

基本功能：输入单行的文本

EchoMode：回显模式
4种回显模式

1.Normal
2.NoEcho
3.Password
4.PasswordEchoOnEdit

"""

import sys
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本回显")
        # 表单布局
        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit", passwordEchoOnEditLineEdit)

        # placeholdertext
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())