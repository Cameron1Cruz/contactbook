# -*- coding: utf-8 -*-

# This module provides views to manage the contacts table.

# Importing the required classes from PyQt6
from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

class Window(QMainWindow):
    #Main Window
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550,250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)