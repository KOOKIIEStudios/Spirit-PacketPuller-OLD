# @author KOOKIIE Studios
# A GUI Implementation of MaplePacketPuller by Brandon Nguyen
#
# This program uses the MVC variant: Model View architecture

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets


from src.main.python import view, constants
import sys
import os
import qdarkstyle


# Use custom fonts
def add_app_font():
    QtGui.QFontDatabase.addApplicationFont(constants.BAUH_PATH)
    QtGui.QFontDatabase.addApplicationFont(constants.FORTE_PATH)
    QtGui.QFontDatabase.addApplicationFont(constants.GARA_PATH)
    QtGui.QFontDatabase.addApplicationFont(constants.GARABD_PATH)


# Main script sequence
if __name__ == '__main__':
    appContext = ApplicationContext()  # 1. Instantiate ApplicationContext
    # Stylesheet is optional; title bar colour cannot be changed, and will remain white
    # appContext.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    add_app_font()
    window = view.MainWindow()  # ViewController module
    window.show()
    exit_code = appContext.app.exec_()  # 2. Invoke appContext.app.exec_()
    sys.exit(exit_code)
