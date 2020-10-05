# @author KOOKIIE Studios
# A GUI Implementation of MaplePacketPuller by Brandon Nguyen
#
# This program uses the MVC variant: Model View architecture
# See https://www.learnpyqt.com/courses/model-views/modelview-architecture/

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets


import view, constants, logger
import sys
import os
import qdarkstyle
spirit_logger = logger.get_logger("main")


# Use custom fonts
def addAppFont():
    spirit_logger.info("Adding application fonts...")
    QtGui.QFontDatabase.addApplicationFont(constants.BAUH_PATH)
    QtGui.QFontDatabase.addApplicationFont(constants.FORTE_PATH)
    QtGui.QFontDatabase.addApplicationFont(constants.GARA_PATH)
    QtGui.QFontDatabase.addApplicationFont(constants.GARABD_PATH)
    spirit_logger.info("Added application fonts")


# Main script sequence
if __name__ == '__main__':
    spirit_logger.info("Logger start-up...")
    appContext = ApplicationContext()  # 1. Instantiate ApplicationContext
    spirit_logger.info("Instantiated ApplicationContext")
    # Stylesheet is optional; title bar colour cannot be changed, and will remain white
    appContext.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    spirit_logger.info("Set Stylesheet: qdarkstyle")
    addAppFont()
    window = view.MainWindow()  # ViewController module
    spirit_logger.info("Imported MainWindow GUI from ViewController view")
    window.show()
    spirit_logger.info("MainWindow shown")
    exit_code = appContext.app.exec_()  # 2. Invoke appContext.app.exec_()
    spirit_logger.info("Raising system exit...")
    spirit_logger.info("Shutting down logger...")
    logger.shutdown_logger()
    sys.exit(exit_code)
