#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QAction,
    QStatusBar,
)
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon, QPixmap
import sys


class MainWindow(QMainWindow):
    def __init__(self, filename):
        super().__init__()

        # Main
        self.setWindowTitle("Image Viewer")
        self.setMinimumSize(QSize(360, 360))
        self.setWindowIcon(QIcon("assets/icon.png"))

        image = QLabel()
        image.setPixmap(
            QPixmap("assets/test.jpg" if filename == "default" else filename)
        )
        image.setMargin(15)
        image.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(image)


file = "default"
args = sys.argv
print(f"All: {args}")

for arg in args:
    if arg in ["main.py", "python"] or arg.endswith("main.py"):
        args.remove(arg)
print(f"Clean: {args}")

if len(args) > 0:
    if not args[0].endswith("main.py"):
        file = args[0]
print(f"View: {file}")

app = QApplication(sys.argv)

window = MainWindow(file)
window.show()

app.exec_()
