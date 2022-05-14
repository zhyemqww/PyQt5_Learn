#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : zhyemqww
# @Time     : 2022/5/13 14:28
# @File     : ScreenGeometry.py
# @Project  : CalendarModule.py
# @Desc     :
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

def click():
    print("第一种")
    print("Widget.x() = %d" % widget.x())
    print("Widget.y() = %d" % widget.y())
    print("Widget.width() = %d" % widget.width())
    print("Widget.height() = %d" % widget.height())

    print("第二种")
    print("Widget.geometry().x() = %d" % widget.geometry().x())
    print("Widget.geometry().y() = %d" % widget.geometry().y())
    print("Widget.geometry().width() = %d" % widget.geometry().width())
    print("Widget.geometry().height() = %d" % widget.geometry().height())

    print("第三种")
    print("Widget.frameGeometry().x() = %d" % widget.frameGeometry().x())
    print("Widget.frameGeometry().y() = %d" % widget.frameGeometry().y())
    print("Widget.frameGeometry().width() = %d" % widget.frameGeometry().width())
    print("Widget.frameGeometry().height() = %d" % widget.frameGeometry().height())

app = QApplication(sys.argv)
widget = QWidget()
button = QPushButton(widget)
button.setText("Button")
button.clicked.connect(click)

button.move(24, 25)
# 设置工作区的尺寸
widget.resize(300, 250)
widget.move(250, 300)

widget.setWindowTitle("ScreenGeometry")

widget.show()

sys.exit(app.exec_())
