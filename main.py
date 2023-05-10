#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main
        self.setWindowTitle("Image Viewer")
        self.setMinimumSize(QSize(360, 360))
        self.setWindowIcon(QIcon("icon.png"))

        # Layout
        layout = QVBoxLayout()

        # Container
        widgets = QWidget()
        widgets.setLayout(layout)

        self.setCentralWidget(widgets)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
