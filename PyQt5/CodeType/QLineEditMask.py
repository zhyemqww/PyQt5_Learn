#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/14 15:02
# @File     : QLineEditMask.py
# @Project  : CalendarModule.py
# @Desc     :
"""
通过掩码限制QLineEdit控件的输入
字符	含义
A	ASCII字母字符是必须输入的（A-Z，a-z）
a	ASCII字母字符是允许输入的，但不是必须输入的
N	ASCII字母字符是必须输入的（A-Z，a-z，0-9）
n	ASCII字母字符是允许输入的，但不是必须输入的
X	任何字符都是必须输入
x	任何字符都是允许输入的，但不是必须输入的
9	ASCII数字字符是必须输入的（0-9）
0	ASCII数字字符是允许输入的，但不是必须输入的
D	ASCII数字字符是必须输入的（1-9）
d	ASCII数字字符是允许输入的，但不是必须的（1-9）
#	ASCII数字字符与加减字符是允许输入的，但不是必须的
H	十六进制格式字符是必须输入的（A-F，a-f，0-9）
h	十六进制格式字符允许输入，但不是必须的
B	二进制格式字符是必须输入的（0,1）
b	二进制格式字符是允许输入的，但不是必须的
>	所有字母字符都大写
<	所有字母字符都小写
！	关闭大小写转换
\	使用‘\’转义上面列出的字符

"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout


class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("掩码")
        QFormLayout()

