#!/usr/bin/env python3

from pathlib import Path
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

Ui_MainWindow, _ = uic.loadUiType(str(Path(__file__).parent.parent.parent.joinpath('form/mainwindow.ui')))

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)