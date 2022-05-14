#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/14 9:25
# @File     : QLineEditValidator.py
# @Project  : CalendarModule.py
# @Desc     :
"""
QLineEdit控件的输入（校验器）

"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout, QLineEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("校验器")

        # 创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow("整数类型", intLineEdit)
        formLayout.addRow("浮点类型", doubleLineEdit)
        formLayout.addRow("数字和字母", validatorLineEdit)

        # 添加提示文本
        intLineEdit.setPlaceholderText("整型")
        doubleLineEdit.setPlaceholderText("浮点型")
        validatorLineEdit.setPlaceholderText("数字与字母")

        # 整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)

        # 浮点校验器
        doubleValidator = QDoubleValidator(self)
        # 设置范围（按照位数）
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度, 小数点2位
        doubleValidator.setDecimals(2)

        # 数字与字母
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())
