# -*- coding: utf-8 -*-
# rpcontacts/main.py

# This module provides RP Contacts application

import sys

from PyQt6.QtWidgets import QApplication

from .views import Window

def main():
    # RP Contacts main function
    app = QApplication(sys.argv)
    # Create the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())