#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QAction,
    QFileDialog,
)
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon, QPixmap, QImage
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self, fileName):
        super().__init__()
        self.ImageFile = (
            QImage("assets/test.jpg") if fileName == "default" else QImage(fileName)
        )

        # Main
        self.setWindowTitle("Image Viewer")
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.setMinimumSize(QSize(360, 360))

        # Image
        self.image = QLabel()
        self.image.setPixmap(QPixmap(self.ImageFile))
        self.image.setMargin(15)
        self.image.setAlignment(Qt.AlignCenter)
        # self.image.resize(self.width(), self.height())
        # self.image.setScaledContents(True)

        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        btnOpen = QAction(QIcon("assets/open.png"), "Open File", self)
        btnOpen.setStatusTip("Open a file to view.")
        btnOpen.triggered.connect(self.OpenImage)
        btnOpen.setShortcut("Ctrl+O")
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolbar.setFloatable(False)
        toolbar.addAction(btnOpen)

        self.resize(QSize(self.ImageFile.width(), self.ImageFile.height()))
        print(f"Resizing to {QSize(self.ImageFile.width(), self.ImageFile.height())}")
        print("=" * 10)
        self.setCentralWidget(self.image)

    def OpenImage(self):
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.ExistingFile)
        self.dialog.setViewMode(QFileDialog.Detail)
        selectedFileName = self.dialog.getOpenFileName(
            self,
            "Open Image",
            f"/home/{os.getlogin()}",
            "Images (*.png *.jpg *.bmp);;Any (*.*)",
        )[0]

        print(f"Selection: {selectedFileName}")
        if selectedFileName != "":
            self.ImageFile = QImage(selectedFileName)
            self.resize(QSize(self.ImageFile.width(), self.ImageFile.height()))
            print(
                f"Resizing to {QSize(self.ImageFile.width(), self.ImageFile.height())}"
            )
            self.image.setPixmap(QPixmap(self.ImageFile))


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
print("=" * 10)

app = QApplication(sys.argv)

window = MainWindow(file)
window.show()

app.exec_()
